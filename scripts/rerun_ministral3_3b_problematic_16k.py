#!/usr/bin/env python3
"""Rerun only problematic Ministral records from the completed benchmark."""

from __future__ import annotations

import argparse
import json
import os
import re
import time
from pathlib import Path

from smoke_test_openrouter_qwen3b import (
    build_prompt,
    call_openrouter_with_retry,
    compact,
    extract_message_text,
    read_inline_xlsx,
)


def read_request_key(notebook_path: Path) -> str:
    nb = json.loads(notebook_path.read_text(encoding="utf-8"))
    text = "\n".join("".join(cell.get("source", [])) for cell in nb.get("cells", []))
    patterns = [
        r"OPENROUTER_API_KEY\s*=\s*['\"]([^'\"]+)['\"]",
        r"api[_-]?key\s*=\s*['\"]([^'\"]+)['\"]",
        r"sk-or-v1-[A-Za-z0-9_-]+",
    ]
    for pattern in patterns:
        match = re.search(pattern, text, re.I)
        if match:
            return (match.group(1) if match.lastindex else match.group(0)).strip()
    raise RuntimeError("OpenRouter key not found in notebook")


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    records = []
    with path.open(encoding="utf-8") as f:
        for line in f:
            if line.strip():
                records.append(json.loads(line))
    return records


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default="runs/mistral_openrouter/ministral3_3b_all_results.jsonl")
    parser.add_argument("--xlsx", default="data/eqb.xlsx")
    parser.add_argument("--output", default="runs/mistral_openrouter/ministral3_3b_problematic_rerun_16k.jsonl")
    parser.add_argument("--model", default="mistralai/ministral-3b-2512")
    parser.add_argument("--max-tokens", type=int, default=16384)
    parser.add_argument("--timeout", type=int, default=600)
    parser.add_argument("--sleep", type=float, default=8)
    parser.add_argument("--retries", type=int, default=5)
    parser.add_argument("--finish-reason-retries", type=int, default=2)
    parser.add_argument("--limit", type=int, default=0, help="Optional number of bad IDs to run")
    args = parser.parse_args()

    api_key = os.environ.get("OPENROUTER_API_KEY") or read_request_key(
        Path("notebooks/openrouter_reasoning_gpt_2 (2).ipynb")
    )

    source_records = read_jsonl(Path(args.source))
    bad_ids = [str(r["id"]) for r in source_records if r.get("finish_reason") != "stop"]
    if args.limit:
        bad_ids = bad_ids[: args.limit]

    already_done = {str(r["id"]) for r in read_jsonl(Path(args.output))}
    rows_by_id = {str(row["id"]): row for row in read_inline_xlsx(Path(args.xlsx))}
    todo_ids = [item for item in bad_ids if item not in already_done]

    if not todo_ids:
        print("No problematic IDs left to rerun.")
        return 0

    with Path(args.output).open("a", encoding="utf-8") as out:
        for index, row_id in enumerate(todo_ids, start=1):
            row = rows_by_id[row_id]
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
                if finish_reason != "error" or finish_attempt >= args.finish_reason_retries:
                    break
                print(
                    f"Retrying id={row_id} because finish_reason=error "
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
                "rerun_source": args.source,
            }
            out.write(json.dumps(record, ensure_ascii=False) + "\n")
            out.flush()
            print(
                f"[{index}/{len(todo_ids)}] id={row_id} finish={choice.get('finish_reason')} "
                f"expected={row['FinalAnswer']}",
                flush=True,
            )
            print(f"prediction: {compact(predicted)}", flush=True)
            if index < len(todo_ids):
                time.sleep(args.sleep)

    print(f"Saved rerun results to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
