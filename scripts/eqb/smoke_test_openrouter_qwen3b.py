#!/usr/bin/env python3
"""Run a 2-question OpenRouter smoke test on the cleaned math dataset."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import zipfile
from pathlib import Path
from urllib import request, error
import xml.etree.ElementTree as ET


DEFAULT_MODEL = "qwen/qwen3-30b-a3b"
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}


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
    try:
        with request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"OpenRouter HTTP {exc.code}: {detail}") from exc


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
            retryable = "HTTP 429" in message or "HTTP 5" in message
            if not retryable or attempt >= retries:
                raise
            wait = min(120, 10 * (2**attempt))
            print(f"Retryable API error. Retry {attempt + 1}/{retries} after {wait}s", flush=True)
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
    parser.add_argument("--xlsx", default="data/eqb.xlsx", help="Dataset workbook path")
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

    rows = read_inline_xlsx(Path(args.xlsx))[args.start : args.start + args.limit]
    if not rows:
        print("No rows found in dataset.", file=sys.stderr)
        return 1

    output_path = Path(args.output)
    mode = "a" if args.append else "w"
    retry_finish_reasons = {
        item.strip()
        for item in args.retry_finish_reasons.split(",")
        if item.strip()
    }
    with output_path.open(mode, encoding="utf-8") as out:
        for index, row in enumerate(rows, start=1):
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
