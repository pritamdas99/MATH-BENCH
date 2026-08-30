#!/usr/bin/env python3
"""Aggregate manual 0/1 labels into Gemma-style accuracy files."""

from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path

from smoke_test_openrouter_qwen3b import read_inline_xlsx


def read_labels(path: Path) -> list[dict]:
    if path.suffix.lower() == ".csv":
        with path.open(encoding="utf-8", newline="") as f:
            return list(csv.DictReader(f))
    with path.open(encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def parse_label(value: object) -> int:
    text = str(value).strip()
    if text not in {"0", "1"}:
        raise ValueError(f"label must be 0 or 1, got {value!r}")
    return int(text)


def label_value(row: dict) -> object:
    if "label" in row:
        return row["label"]
    if "labels" in row:
        return row["labels"]
    raise KeyError("label row must contain 'label' or 'labels'")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--labels", required=True)
    parser.add_argument("--xlsx", default="data/eqb.xlsx")
    parser.add_argument("--prefix", required=True)
    args = parser.parse_args()

    chapter_by_id = {
        str(row["id"]): row["ChapterName"]
        for row in read_inline_xlsx(Path(args.xlsx))
    }
    labels = read_labels(Path(args.labels))

    per_id = []
    for row in labels:
        row_id = str(row["id"])
        label = parse_label(label_value(row))
        per_id.append(
            {
                "id": row_id,
                "ChapterName": chapter_by_id.get(row_id, ""),
                "label": label,
                "expected_final_answer": row.get("expected_final_answer", ""),
                "predicted_final_answer": row.get("predicted_final_answer", ""),
            }
        )

    total = len(per_id)
    correct = sum(row["label"] for row in per_id)
    overall = {
        "total": total,
        "correct": correct,
        "incorrect": total - correct,
        "accuracy": correct / total if total else 0,
    }

    grouped: dict[str, list[dict]] = defaultdict(list)
    for row in per_id:
        grouped[row["ChapterName"]].append(row)
    chapter_rows = []
    for chapter, rows in grouped.items():
        chapter_total = len(rows)
        chapter_correct = sum(row["label"] for row in rows)
        chapter_rows.append(
            {
                "ChapterName": chapter,
                "total": chapter_total,
                "correct": chapter_correct,
                "incorrect": chapter_total - chapter_correct,
                "accuracy": chapter_correct / chapter_total if chapter_total else 0,
            }
        )
    chapter_rows.sort(key=lambda row: row["accuracy"], reverse=True)

    prefix = Path(args.prefix)
    with Path(f"{prefix}_evaluation_per_id_with_chapter.jsonl").open(
        "w", encoding="utf-8"
    ) as out:
        for row in per_id:
            out.write(json.dumps(row, ensure_ascii=False) + "\n")

    with Path(f"{prefix}_evaluation_per_id_with_chapter.csv").open(
        "w", encoding="utf-8", newline=""
    ) as out:
        writer = csv.DictWriter(out, fieldnames=list(per_id[0].keys()))
        writer.writeheader()
        writer.writerows(per_id)

    with Path(f"{prefix}_chapter_accuracy.json").open("w", encoding="utf-8") as out:
        json.dump(chapter_rows, out, ensure_ascii=False, indent=2)
        out.write("\n")

    with Path(f"{prefix}_chapter_accuracy.csv").open(
        "w", encoding="utf-8", newline=""
    ) as out:
        writer = csv.DictWriter(out, fieldnames=list(chapter_rows[0].keys()))
        writer.writeheader()
        writer.writerows(chapter_rows)

    with Path(f"{prefix}_overall_accuracy.json").open("w", encoding="utf-8") as out:
        json.dump(overall, out, ensure_ascii=False, indent=2)
        out.write("\n")

    print(json.dumps(overall, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
