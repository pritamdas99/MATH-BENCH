#!/usr/bin/env python3
"""Label final-answer correctness for benchmark result files."""

from __future__ import annotations

import argparse
import concurrent.futures as futures
import json
import os
import re
import time
from pathlib import Path
from typing import Any

from rerun_ministral3_3b_problematic_16k import read_request_key
from smoke_test_openrouter_qwen3b import call_openrouter_with_retry, extract_message_text


FINAL_CUE_PATTERNS = [
    r"FinalAnswer\s*[:：]",
    r"Final\s*Answer\s*[:：]",
    r"ফাইনাল\s*উত্তর\s*[:：]?",
    r"চূড়ান্ত\s*উত্তর\s*[:：]?",
    r"চূড়ান্ত\s*উত্তর\s*[:：]?",
    r"উত্তর\s*[:：]",
]


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    with path.open(encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def cleanup_extracted_answer(text: str) -> str:
    text = text.strip()
    text = re.sub(r"^<[^>]{0,120}>", "", text).strip()
    text = re.sub(r"^(শুধু|শুধুমাত্র)\s+চূ[ড়ড়]ান্ত\s+ফলাফল\s*>?", "", text).strip()
    text = re.sub(r"^[:：\\-–—\s]+", "", text).strip()
    return text


def predicted_final_answer(text: str) -> str:
    if not text:
        return ""

    matches: list[re.Match[str]] = []
    for pattern in FINAL_CUE_PATTERNS:
        matches.extend(re.finditer(pattern, text, flags=re.I))
    if not matches:
        return ""

    match = max(matches, key=lambda item: item.start())
    answer = text[match.end() :].strip()

    # Some models emit "FinalAnswer: <instruction echo> actual answer".
    answer = cleanup_extracted_answer(answer)
    return answer


def judge_prompt(record: dict[str, Any], predicted: str) -> str:
    return f"""
You are grading a Bengali math benchmark.

Return ONLY valid JSON in this exact shape:
{{"label": 0 or 1, "reason": "short reason"}}

Grade rule:
- label 1 if the predicted final answer is mathematically equivalent to the expected final answer and answers every required part. also if predicted answer misses units, degree, radian sign , consider it correct since main goal is to make sure that reasoning is correct and model has got the final answer with a corect process
- label 0 if it is wrong, incomplete, contradictory, a different object, or no clear final answer.
- Ignore formatting, Bengali vs English digits, LaTeX spacing, boxes, and harmless wording.
- Do not require the detailed solution to be correct if the final answer itself is correct.

Question:
{record.get("question", "")}

Expected final answer:
{record.get("expected_final_answer", "")}

Predicted final answer:
{predicted}
""".strip()


def parse_label(response_text: str) -> tuple[int, str]:
    try:
        payload = json.loads(response_text)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", response_text, flags=re.S)
        if not match:
            raise
        payload = json.loads(match.group(0))
    label = int(payload["label"])
    if label not in {0, 1}:
        raise ValueError(f"invalid label {label!r}")
    return label, str(payload.get("reason", "")).strip()


def judge_one(
    api_key: str,
    model: str,
    record: dict[str, Any],
    timeout: int,
    retries: int,
) -> dict[str, Any]:
    predicted = predicted_final_answer(record.get("predicted_answer") or "")
    row = {
        "id": str(record["id"]),
        "label": 0,
        "predicted_answer": record.get("predicted_answer", ""),
        "expected_final_answer": record.get("expected_final_answer", ""),
        "predicted_final_answer": predicted,
        "finish_reason": record.get("finish_reason"),
    }
    if not predicted:
        row["judge_model"] = model
        row["judge_reason"] = "No generated final answer was found."
        return row

    response = call_openrouter_with_retry(
        api_key=api_key,
        model=model,
        prompt=judge_prompt(record, predicted),
        timeout=timeout,
        max_tokens=128,
        retries=retries,
    )
    response_text = extract_message_text(response)
    label, reason = parse_label(response_text)
    row["label"] = label
    row["judge_model"] = model
    row["judge_reason"] = reason
    return row


def load_existing(path: Path) -> dict[str, dict[str, Any]]:
    if not path.exists():
        return {}
    return {str(row["id"]): row for row in read_jsonl(path)}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--model", default="openai/gpt-4o-mini")
    parser.add_argument("--timeout", type=int, default=120)
    parser.add_argument("--retries", type=int, default=4)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--sleep", type=float, default=0.0)
    args = parser.parse_args()

    api_key = os.environ.get("OPENROUTER_API_KEY") or read_request_key(
        Path("notebooks/openrouter_reasoning_gpt_2 (2).ipynb")
    )
    records = read_jsonl(Path(args.results))
    if args.limit:
        records = records[: args.limit]

    output = Path(args.output)
    existing = load_existing(output)
    rows_by_id = dict(existing)
    todo = [record for record in records if str(record["id"]) not in existing]

    print(f"results={args.results}")
    print(f"output={output}")
    print(f"judge_model={args.model}")
    print(f"already_done={len(existing)} todo={len(todo)}")

    if todo:
        with futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
            submitted = {
                pool.submit(
                    judge_one,
                    api_key,
                    args.model,
                    record,
                    args.timeout,
                    args.retries,
                ): record
                for record in todo
            }
            completed = 0
            for future in futures.as_completed(submitted):
                record = submitted[future]
                try:
                    row = future.result()
                except Exception as exc:
                    row = {
                        "id": str(record["id"]),
                        "label": 0,
                        "expected_final_answer": record.get("expected_final_answer", ""),
                        "predicted_final_answer": predicted_final_answer(
                            record.get("predicted_answer") or ""
                        ),
                        "finish_reason": record.get("finish_reason"),
                        "judge_model": args.model,
                        "judge_reason": f"judge_error: {exc!r}",
                    }
                rows_by_id[str(record["id"])] = row
                completed += 1
                if completed % 25 == 0 or completed == len(todo):
                    ordered = [rows_by_id[str(item["id"])] for item in records if str(item["id"]) in rows_by_id]
                    write_jsonl(output, ordered)
                    print(f"completed={completed}/{len(todo)} total_written={len(ordered)}", flush=True)
                if args.sleep:
                    time.sleep(args.sleep)

    final_rows = [rows_by_id[str(record["id"])] for record in records]
    write_jsonl(output, final_rows)
    correct = sum(int(row["label"]) for row in final_rows)
    print(json.dumps({"total": len(final_rows), "correct": correct, "incorrect": len(final_rows) - correct, "accuracy": correct / len(final_rows)}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
