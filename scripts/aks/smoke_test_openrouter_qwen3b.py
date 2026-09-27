#!/usr/bin/env python3
"""Run a 2-question OpenRouter smoke test on the cleaned math dataset."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import threading
import time
import zipfile
from pathlib import Path
from urllib import request, error
import xml.etree.ElementTree as ET


DEFAULT_MODEL = "qwen/qwen3-30b-a3b"
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}


class OpenRouterHTTPError(RuntimeError):
    """Keep HTTP status and provider metadata for retry decisions."""

    def __init__(self, status: int, detail: str, retry_after: str | None = None) -> None:
        super().__init__(f"OpenRouter HTTP {status}: {detail}")
        self.status = status
        try:
            payload = json.loads(detail)
        except (ValueError, TypeError):
            payload = {}
        api_error = payload.get("error") if isinstance(payload, dict) else None
        metadata = api_error.get("metadata") if isinstance(api_error, dict) else None
        metadata = metadata if isinstance(metadata, dict) else {}
        self.in_flight_budget_exhausted = (
            status == 402 and metadata.get("reason") == "in_flight_budget_exhausted"
        )
        headers = metadata.get("headers")
        if retry_after is None and isinstance(headers, dict):
            retry_after = headers.get("Retry-After")
        try:
            self.retry_after = max(0, int(retry_after)) if retry_after is not None else 0
        except (ValueError, TypeError):
            self.retry_after = 0
        self.provider_auth_failure = (
            status == 401
            and isinstance(metadata, dict)
            and bool(metadata.get("provider_name"))
            and metadata.get("is_byok") is False
        )


def column_index(cell_ref: str) -> int:
    letters = "".join(ch for ch in cell_ref if ch.isalpha())
    index = 0
    for ch in letters:
        index = index * 26 + ord(ch) - 64
    return index - 1


def read_inline_xlsx(path: Path) -> list[dict[str, str]]:
    with zipfile.ZipFile(path) as zf:
        sheet = ET.fromstring(zf.read("xl/worksheets/sheet1.xml"))

    table: list[list[str | None]] = []
    for row in sheet.findall(".//m:sheetData/m:row", NS):
        values: list[str | None] = [None] * 6
        for cell in row.findall("m:c", NS):
            idx = column_index(cell.attrib["r"])
            if idx >= len(values):
                continue
            text = "".join(t.text or "" for t in cell.findall(".//m:t", NS))
            value = cell.find("m:v", NS)
            values[idx] = text or (value.text if value is not None else "")
        table.append(values)

    headers = [h or "" for h in table[0]]
    return [
        {headers[i]: row[i] or "" for i in range(len(headers))}
        for row in table[1:]
    ]


def read_dataset(path: Path) -> list[dict[str, str]]:
    """Read benchmark rows from a JSON array or inline-string XLSX file."""
    if path.suffix.lower() == ".json":
        rows = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(rows, list):
            raise ValueError(f"Expected a JSON array in {path}")
    elif path.suffix.lower() == ".xlsx":
        rows = read_inline_xlsx(path)
    else:
        raise ValueError(f"Unsupported dataset format: {path.suffix}")

    required = {"id", "Question", "FinalAnswer"}
    for index, row in enumerate(rows, start=1):
        if not isinstance(row, dict):
            raise ValueError(f"Dataset row {index} is not an object")
        missing = required - row.keys()
        if missing:
            raise ValueError(
                f"Dataset row {index} is missing: {', '.join(sorted(missing))}"
            )
    return rows


def build_prompt(question: str) -> str:
    return f"""
একটি গাণিতিক সমস্যা দেওয়া আছে। সমস্যাটি ধাপে ধাপে সমাধান করো।

প্রশ্ন:
{question}

নিম্নলিখিত ফরম্যাটে আউটপুট দাও:

DetailedAnswer:
<ধাপে ধাপে গাণিতিক সমাধান>

FinalAnswer:
<শুধু চূড়ান্ত ফলাফল>

গুরুত্বপূর্ণ:
DetailedAnswer অংশে শুধুমাত্র গাণিতিক বিশ্লেষণ থাকবে।
FinalAnswer অংশে শুধুমাত্র চূড়ান্ত ফলাফল থাকবে।
""".strip()


def call_openrouter(
    api_key: str,
    model: str,
    prompt: str,
    timeout: int,
    max_tokens: int,
) -> dict:
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0,
        "max_tokens": max_tokens,
    }
    body = json.dumps(payload).encode("utf-8")
    req = request.Request(
        OPENROUTER_URL,
        data=body,
        method="POST",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost/math-bench-smoke-test",
            "X-Title": "MATH-BENCH Smoke Test",
        },
    )
    request_finished = threading.Event()

    def report_wait() -> None:
        elapsed = 0
        while not request_finished.wait(10):
            elapsed += 10
            print(
                f"Still waiting for {model} response ({elapsed}s elapsed)...",
                flush=True,
            )

    threading.Thread(target=report_wait, daemon=True).start()
    try:
        with request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise OpenRouterHTTPError(exc.code, detail, exc.headers.get("Retry-After") if exc.headers else None) from exc
    except (error.URLError, TimeoutError) as exc:
        raise RuntimeError(f"OpenRouter network error: {exc}") from exc
    finally:
        request_finished.set()


def call_openrouter_with_retry(
    api_key: str,
    model: str,
    prompt: str,
    timeout: int,
    max_tokens: int,
    retries: int,
) -> dict:
    last_error: Exception | None = None
    for attempt in range(retries + 1):
        try:
            return call_openrouter(api_key, model, prompt, timeout, max_tokens)
        except RuntimeError as exc:
            last_error = exc
            message = str(exc)
            if isinstance(exc, OpenRouterHTTPError):
                retryable = (
                    exc.status == 429
                    or 500 <= exc.status < 600
                    or exc.provider_auth_failure
                    or exc.in_flight_budget_exhausted
                )
            else:
                retryable = "network error" in message
            print(
                f"API error on attempt {attempt + 1}/{retries + 1}: {message}",
                file=sys.stderr,
                flush=True,
            )
            if not retryable:
                print("Error is not retryable; stopping.", file=sys.stderr, flush=True)
                raise
            if attempt >= retries:
                print("Retry limit reached; stopping.", file=sys.stderr, flush=True)
                raise
            wait = min(120, 10 * (2**attempt))
            if isinstance(exc, OpenRouterHTTPError):
                wait = max(wait, exc.retry_after)
            print(
                f"Retryable API error; next attempt in {wait}s.",
                file=sys.stderr,
                flush=True,
            )
            time.sleep(wait)
    raise last_error or RuntimeError("API request failed")


def compact(text: str, limit: int = 220) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    return text if len(text) <= limit else text[: limit - 3] + "..."


def extract_message_text(response: dict) -> str:
    choice = response.get("choices", [{}])[0]
    message = choice.get("message") or {}
    for key in ("content", "reasoning", "reasoning_content"):
        value = message.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    return json.dumps(message, ensure_ascii=False)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--dataset",
        default="data/aks_eqb_style_merged.json",
        help="Dataset path (.json or .xlsx)",
    )
    parser.add_argument("--limit", type=int, default=2, help="Number of questions to run")
    parser.add_argument("--model", default=DEFAULT_MODEL, help="OpenRouter model ID")
    parser.add_argument("--output", default="smoke_results_qwen3b.jsonl")
    parser.add_argument("--timeout", type=int, default=120)
    parser.add_argument("--max-tokens", type=int, default=4096)
    parser.add_argument("--sleep", type=float, default=1.0)
    parser.add_argument("--start", type=int, default=0, help="Zero-based row offset")
    parser.add_argument("--append", action="store_true", help="Append to output instead of overwriting")
    parser.add_argument("--retries", type=int, default=4)
    parser.add_argument(
        "--retry-finish-reasons",
        default="",
        help="Comma-separated finish reasons to retry before writing a record",
    )
    parser.add_argument("--finish-reason-retries", type=int, default=0)
    args = parser.parse_args()

    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        print("Set OPENROUTER_API_KEY before running this script.", file=sys.stderr)
        return 2

    dataset_path = Path(args.dataset)
    print(f"Loading dataset: {dataset_path}", flush=True)
    all_rows = read_dataset(dataset_path)
    print(f"Dataset loaded: {len(all_rows)} records", flush=True)
    rows = all_rows[args.start : args.start + args.limit]
    if not rows:
        print(
            f"No rows left after start offset {args.start}; run is already complete.",
            flush=True,
        )
        return 0

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    mode = "a" if args.append else "w"
    completed_ids: set[str] = set()
    if args.append and output_path.exists():
        with output_path.open(encoding="utf-8") as existing_file:
            completed_ids = {
                str(json.loads(line)["id"])
                for line in existing_file
                if line.strip()
            }
        rows = [row for row in rows if str(row["id"]) not in completed_ids]
    print(f"Remote model ready: {args.model}", flush=True)
    print(f"Already completed: {len(completed_ids)}", flush=True)
    print(
        f"Starting generation: {len(rows)} records, max_tokens={args.max_tokens}",
        flush=True,
    )
    print(f"Writing results to: {output_path}", flush=True)
    if not rows:
        print("No rows left to run.", flush=True)
        return 0
    retry_finish_reasons = {
        item.strip()
        for item in args.retry_finish_reasons.split(",")
        if item.strip()
    }
    with output_path.open(mode, encoding="utf-8") as out:
        for index, row in enumerate(rows, start=1):
            print(
                f"[{index}/{len(rows)}] id={row['id']} sending request to {args.model}",
                flush=True,
            )
            prompt = build_prompt(row["Question"])
            for finish_attempt in range(args.finish_reason_retries + 1):
                response = call_openrouter_with_retry(
                    api_key,
                    args.model,
                    prompt,
                    args.timeout,
                    args.max_tokens,
                    args.retries,
                )
                choice = response.get("choices", [{}])[0]
                finish_reason = choice.get("finish_reason")
                if (
                    finish_reason not in retry_finish_reasons
                    or finish_attempt >= args.finish_reason_retries
                ):
                    break
                print(
                    f"Retrying id={row['id']} because finish_reason={finish_reason} "
                    f"({finish_attempt + 1}/{args.finish_reason_retries})",
                    flush=True,
                )
                time.sleep(args.sleep)
            predicted = extract_message_text(response)
            record = {
                "id": row["id"],
                "model": args.model,
                "question": row["Question"],
                "expected_final_answer": row["FinalAnswer"],
                "predicted_answer": predicted,
                "finish_reason": choice.get("finish_reason"),
                "usage": response.get("usage"),
            }
            out.write(json.dumps(record, ensure_ascii=False) + "\n")
            out.flush()
            print(
                f"[{index}/{len(rows)}] id={row['id']} "
                f"finish={choice.get('finish_reason')} expected={row['FinalAnswer']}"
            , flush=True)
            print(f"prediction: {compact(predicted)}", flush=True)
            if index < len(rows):
                time.sleep(args.sleep)

    print(f"Saved results to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
