#!/usr/bin/env python3
"""Research-style LLM-as-judge final-answer evaluation."""

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

PRICES_PER_MILLION = {
    "openai/gpt-4.1": {"input": 2.00, "output": 8.00},
    "openai/gpt-4.1-mini": {"input": 0.40, "output": 1.60},
    "openai/gpt-4o-mini": {"input": 0.15, "output": 0.60},
}


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def compact_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def clean_candidate(text: str) -> str:
    text = text.strip()
    text = re.sub(r"^<[^>]{0,160}>", "", text).strip()
    text = re.sub(r"^(শুধু|শুধুমাত্র)\s+চূ[ড়ড়]ান্ত\s+ফলাফল\s*>?", "", text).strip()
    text = re.sub(r"^[:：\-\s]+", "", text).strip()
    return text


def predicted_final_answer(text: str) -> tuple[str, str]:
    """Return (candidate, extraction_method)."""
    if not text:
        return "", "empty_output"
    matches: list[re.Match[str]] = []
    for pattern in FINAL_CUE_PATTERNS:
        matches.extend(re.finditer(pattern, text, flags=re.I))
    if matches:
        match = max(matches, key=lambda item: item.start())
        return clean_candidate(text[match.end() :].strip()), "cue_after_last_marker"
    return "", "no_marker"


def tail_context(text: str, limit: int) -> str:
    text = compact_whitespace(text)
    if len(text) <= limit:
        return text
    return text[-limit:]


def judge_prompt(record: dict[str, Any], candidate: str, method: str, tail: str) -> str:
    tail_block = ""
    if tail:
        tail_block = f"""

Raw generated-answer tail, supplied only because the extracted candidate may be missing or malformed:
{tail}
""".rstrip()

    return f"""
Strict math final-answer judge. Return ONLY valid JSON:
{{"label": 0 or 1}}

Rules:
- Judge only the final answer, not reasoning.
- 1 = complete and mathematically equivalent to expected.
- 0 = wrong, incomplete, missing a required part/condition/unit, wrong sign, or contradictory extra final answer.
- Multipart expected answer: all parts required.
- Ignore harmless formatting: spacing, boxes, Bengali/English digits, exact fraction vs equal decimal, C vs c for integration constants.
- Interpret obvious transliterated LaTeX: ফ্র্যাক{{a}}{{b}} = \\frac{{a}}{{b}}, বাক্সযুক্ত{{x}} = boxed{{x}}, সি = C.
- If candidate is malformed but the raw tail clearly shows the final answer, judge from the raw tail.

Expected final answer:
{record.get("expected_final_answer", "")}

Extracted generated final-answer candidate:
{candidate if candidate else "[NO EXTRACTED FINAL ANSWER]"}

Extraction method:
{method}{tail_block}
""".strip()


def parse_label(text: str) -> tuple[int, str]:
    try:
        payload = json.loads(text)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", text, flags=re.S)
        if not match:
            raise
        cleaned = match.group(0)
        cleaned = re.sub(r"\\(?![\"\\/bfnrtu])", r"\\\\", cleaned)
        payload = json.loads(cleaned)
    label = int(payload["label"])
    if label not in {0, 1}:
        raise ValueError(f"invalid label {label}")
    return label, str(payload.get("reason", "")).strip()


def usage_cost(model: str, usage: dict[str, Any] | None) -> float:
    if not usage:
        return 0.0
    price = PRICES_PER_MILLION.get(model)
    if not price:
        return 0.0
    prompt_tokens = usage.get("prompt_tokens") or 0
    completion_tokens = usage.get("completion_tokens") or 0
    return (
        prompt_tokens * price["input"] / 1_000_000
        + completion_tokens * price["output"] / 1_000_000
    )


def judge_one(
    api_key: str,
    model: str,
    record: dict[str, Any],
    timeout: int,
    retries: int,
    tail_limit: int,
) -> dict[str, Any]:
    candidate, method = predicted_final_answer(record.get("predicted_answer") or "")
    needs_tail = not candidate or method != "cue_after_last_marker"
    if candidate and len(candidate) < 12:
        needs_tail = True
    tail = tail_context(record.get("predicted_answer") or "", tail_limit) if needs_tail else ""
    prompt = judge_prompt(record, candidate, method, tail)
    response = call_openrouter_with_retry(
        api_key=api_key,
        model=model,
        prompt=prompt,
        timeout=timeout,
        max_tokens=16,
        retries=retries,
    )
    response_text = extract_message_text(response)
    label, reason = parse_label(response_text)
    usage = response.get("usage") or {}
    print(record, response_text,"====>>", flush=True)
    return {
        "id": str(record["id"]),
        "label": label,
        "expected_final_answer": record.get("expected_final_answer", ""),
        "predicted_final_answer": candidate,
        "extraction_method": method,
        "finish_reason": record.get("finish_reason"),
        "judge_model": model,
        "judge_reason": reason,
        "judge_usage": usage,
        "judge_cost_usd_estimate": round(usage_cost(model, usage), 8),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--model", default="openai/gpt-4.1")
    parser.add_argument("--timeout", type=int, default=120)
    parser.add_argument("--retries", type=int, default=4)
    parser.add_argument("--workers", type=int, default=3)
    parser.add_argument("--tail-limit", type=int, default=900)
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--budget-usd", type=float, default=2.0)
    args = parser.parse_args()

    api_key = os.environ.get("OPENROUTER_API_KEY") or read_request_key(
        Path("notebooks/openrouter_reasoning_gpt_2 (2).ipynb")
    )
    records = read_jsonl(Path(args.results))
    if args.limit:
        records = records[: args.limit]

    output = Path(args.output)
    existing = {str(row["id"]): row for row in read_jsonl(output)}
    rows_by_id = dict(existing)
    todo = [record for record in records if str(record["id"]) not in existing]
    spent = sum(float(row.get("judge_cost_usd_estimate") or 0) for row in existing.values())

    print(f"results={args.results}")
    print(f"output={output}")
    print(f"judge_model={args.model}")
    print(f"already_done={len(existing)} todo={len(todo)} spent_estimate={spent:.4f}")

    with futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        pending = {}
        iterator = iter(todo)

        def submit_more() -> None:
            nonlocal spent
            while len(pending) < args.workers:
                if spent >= args.budget_usd:
                    return
                try:
                    record = next(iterator)
                except StopIteration:
                    return
                fut = pool.submit(
                    judge_one,
                    api_key,
                    args.model,
                    record,
                    args.timeout,
                    args.retries,
                    args.tail_limit,
                )
                pending[fut] = record

        submit_more()
        completed = 0
        while pending:
            done, _ = futures.wait(pending, return_when=futures.FIRST_COMPLETED)
            for fut in done:
                record = pending.pop(fut)
                try:
                    row = fut.result()
                except Exception as exc:
                    candidate, method = predicted_final_answer(record.get("predicted_answer") or "")
                    row = {
                        "id": str(record["id"]),
                        "label": 0,
                        "expected_final_answer": record.get("expected_final_answer", ""),
                        "predicted_final_answer": candidate,
                        "extraction_method": method,
                        "finish_reason": record.get("finish_reason"),
                        "judge_model": args.model,
                        "judge_reason": f"judge_error: {exc!r}",
                        "judge_usage": {},
                        "judge_cost_usd_estimate": 0,
                    }
                rows_by_id[str(record["id"])] = row
                spent += float(row.get("judge_cost_usd_estimate") or 0)
                completed += 1
                
                if completed % 25 == 0 or completed == len(todo):
                    ordered = [
                        rows_by_id[str(item["id"])]
                        for item in records
                        if str(item["id"]) in rows_by_id
                    ]
                    write_jsonl(output, ordered)
                    print(
                        f"completed={completed}/{len(todo)} total_written={len(ordered)} "
                        f"spent_estimate={spent:.4f}",
                        flush=True,
                    )
                submit_more()

    final_rows = [rows_by_id[str(record["id"])] for record in records if str(record["id"]) in rows_by_id]
    write_jsonl(output, final_rows)
    correct = sum(int(row["label"]) for row in final_rows)
    summary = {
        "total": len(final_rows),
        "correct": correct,
        "incorrect": len(final_rows) - correct,
        "accuracy": correct / len(final_rows) if final_rows else 0,
        "cost_usd_estimate": round(
            sum(float(row.get("judge_cost_usd_estimate") or 0) for row in final_rows),
            6,
        ),
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    if len(final_rows) < len(records):
        print("Stopped before all rows were judged, probably due to budget limit.", flush=True)
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
