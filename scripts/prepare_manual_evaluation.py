#!/usr/bin/env python3
"""Prepare manual final-answer labels from a model result JSONL file."""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path


def read_jsonl(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def predicted_final_answer(text: str) -> str:
    matches = list(re.finditer(r"FinalAnswer\s*:", text, flags=re.I))
    if not matches:
        return ""
    return text[matches[-1].end() :].strip()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results", required=True)
    parser.add_argument("--jsonl-output", required=True)
    parser.add_argument("--csv-output", required=True)
    args = parser.parse_args()

    records = read_jsonl(Path(args.results))
    rows = []
    for record in records:
        rows.append(
            {
                "id": record["id"],
                "label": "",
                "expected_final_answer": record["expected_final_answer"],
                "predicted_final_answer": predicted_final_answer(
                    record.get("predicted_answer") or ""
                ),
            }
        )

    with Path(args.jsonl_output).open("w", encoding="utf-8") as out:
        for row in rows:
            out.write(json.dumps(row, ensure_ascii=False) + "\n")

    with Path(args.csv_output).open("w", encoding="utf-8", newline="") as out:
        writer = csv.DictWriter(
            out,
            fieldnames=[
                "id",
                "label",
                "expected_final_answer",
                "predicted_final_answer",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} rows to {args.jsonl_output} and {args.csv_output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
