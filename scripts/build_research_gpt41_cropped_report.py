#!/usr/bin/env python3
"""Build an evaluation report from cropped research_gpt41 label files."""

from __future__ import annotations

import csv
import json
from collections import defaultdict
from pathlib import Path


LABEL_DIR = Path("results/research_gpt41/labels")
SUMMARY_DIR = Path("results/research_gpt41/summaries/cropped")
REPORT_PATH = Path("reports/research_gpt41_cropped_evaluation_report.md")
ACCURACY_REPORT_PATH = Path("reports/research_gpt41_cropped_accuracy.md")

MODELS = [
    {
        "key": "gpt5",
        "name": "GPT-5",
        "labels": LABEL_DIR / "research_gpt41_gpt5_answer_labels_cropped.jsonl",
        "prefix": SUMMARY_DIR / "research_gpt41_gpt5",
    },
    {
        "key": "qwen3_4b",
        "name": "Qwen3-4B",
        "labels": LABEL_DIR / "research_gpt41_qwen3_4b_answer_labels_cropped.jsonl",
        "prefix": SUMMARY_DIR / "research_gpt41_qwen3_4b",
    },
    {
        "key": "mistral3_3b",
        "name": "Mistral 3B",
        "labels": LABEL_DIR / "research_gpt41_mistral3_3b_answer_labels_cropped.jsonl",
        "prefix": SUMMARY_DIR / "research_gpt41_mistral3_3b",
    },
    {
        "key": "qwen2_5_7b",
        "name": "Qwen2.5-7B",
        "labels": LABEL_DIR / "research_gpt41_qwen2.5_7b_answer_labels_cropped.jsonl",
        "prefix": SUMMARY_DIR / "research_gpt41_qwen2_5_7b",
    },
    {
        "key": "gemma3_4b",
        "name": "Gemma3-4B",
        "labels": LABEL_DIR / "research_gpt41_gemma3_4b_answer_labels_cropped.jsonl",
        "prefix": SUMMARY_DIR / "research_gpt41_gemma3_4b",
    },
    {
        "key": "llama3_2_3b_instruct",
        "name": "Llama 3.2 3B Instruct",
        "labels": LABEL_DIR
        / "research_gpt41_llama3_2_3b_instruct_answer_labels_cropped.jsonl",
        "prefix": SUMMARY_DIR / "research_gpt41_llama3_2_3b_instruct",
    },
]


def read_jsonl(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as infile:
        return [json.loads(line) for line in infile if line.strip()]


def label_value(row: dict) -> int:
    value = row.get("label", row.get("labels"))
    text = str(value).strip()
    if text not in {"0", "1"}:
        raise ValueError(f"label must be 0 or 1, got {value!r}")
    return int(text)


def pct(value: float) -> str:
    return f"{value * 100:.2f}%"


def md_escape(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


def bar(value: float, width: int = 24) -> str:
    filled = round(value * width)
    return "#" * filled + "." * (width - filled)


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_csv(path: Path, rows: list[dict], fieldnames: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def summarize_model(model: dict) -> tuple[dict, list[dict], list[dict]]:
    labels = read_jsonl(model["labels"])
    per_id = []
    for row in labels:
        per_id.append(
            {
                "id": str(row["id"]),
                "ChapterName": row.get("ChapterName", row.get("chapterName", "")),
                "label": label_value(row),
                "expected_final_answer": row.get("expected_final_answer", ""),
                "predicted_final_answer": row.get("predicted_final_answer", ""),
            }
        )

    total = len(per_id)
    correct = sum(row["label"] for row in per_id)
    overall = {
        "model": model["name"],
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
    chapter_rows.sort(key=lambda row: (-row["accuracy"], row["ChapterName"]))

    prefix = model["prefix"]
    with Path(f"{prefix}_evaluation_per_id_with_chapter.jsonl").open(
        "w", encoding="utf-8"
    ) as outfile:
        for row in per_id:
            outfile.write(json.dumps(row, ensure_ascii=False) + "\n")
    write_csv(
        Path(f"{prefix}_evaluation_per_id_with_chapter.csv"),
        per_id,
        ["id", "ChapterName", "label", "expected_final_answer", "predicted_final_answer"],
    )
    write_json(Path(f"{prefix}_overall_accuracy.json"), overall)
    write_json(Path(f"{prefix}_chapter_accuracy.json"), chapter_rows)
    write_csv(
        Path(f"{prefix}_chapter_accuracy.csv"),
        chapter_rows,
        ["ChapterName", "total", "correct", "incorrect", "accuracy"],
    )

    return overall, chapter_rows, per_id


def build_combined_chapter_rows(chapter_maps: dict[str, dict[str, dict]]) -> list[dict]:
    totals: dict[str, int] = {}
    for chapter_map in chapter_maps.values():
        for chapter, row in chapter_map.items():
            totals[chapter] = max(totals.get(chapter, 0), int(row["total"]))

    combined_rows = []
    for chapter in sorted(totals, key=lambda item: (-totals[item], item)):
        row = {"ChapterName": chapter, "total": totals[chapter]}
        for model in MODELS:
            item = chapter_maps[model["key"]].get(chapter)
            row[f"{model['key']}_correct"] = item["correct"] if item else 0
            row[f"{model['key']}_total"] = item["total"] if item else 0
            row[f"{model['key']}_accuracy"] = item["accuracy"] if item else 0
        combined_rows.append(row)
    return combined_rows


def write_report(overall_rows: list[dict], combined_chapter_rows: list[dict]) -> None:
    ranked = sorted(overall_rows, key=lambda row: row["accuracy"], reverse=True)

    lines: list[str] = []
    lines.append("# Research GPT-4.1 Cropped Label Evaluation Report")
    lines.append("")
    lines.append(
        "This report summarizes all `*_cropped.jsonl` label files in "
        "`results/research_gpt41/labels`. Labels are treated as binary final-answer "
        "accuracy scores, where `1` is correct and `0` is incorrect."
    )
    lines.append("")
    lines.append("## Overall Accuracy")
    lines.append("")
    lines.append("| Rank | Model | Correct | Incorrect | Total | Accuracy |")
    lines.append("|---:|---|---:|---:|---:|---:|")
    for index, row in enumerate(ranked, start=1):
        lines.append(
            f"| {index} | {row['model']} | {row['correct']} | {row['incorrect']} | "
            f"{row['total']} | {pct(row['accuracy'])} |"
        )
    lines.append("")
    lines.append("## Overall Accuracy Graph")
    lines.append("")
    lines.append("| Model | Accuracy | Bar |")
    lines.append("|---|---:|---|")
    for row in ranked:
        lines.append(f"| {row['model']} | {pct(row['accuracy'])} | `{bar(row['accuracy'])}` |")
    lines.append("")
    lines.append("```mermaid")
    lines.append("xychart-beta")
    lines.append('  title "Overall Accuracy by Model"')
    lines.append("  x-axis [" + ", ".join(json.dumps(row["model"]) for row in ranked) + "]")
    lines.append('  y-axis "Accuracy (%)" 0 --> 75')
    lines.append("  bar [" + ", ".join(f"{row['accuracy'] * 100:.2f}" for row in ranked) + "]")
    lines.append("```")
    lines.append("")
    lines.append("## Chapter-Based Accuracy")
    lines.append("")
    lines.append(
        "| Chapter | Total | GPT-5 | Qwen3-4B | Mistral 3B | Qwen2.5-7B | "
        "Gemma3-4B | Llama 3.2 3B Instruct |"
    )
    lines.append("|---|---:|---:|---:|---:|---:|---:|---:|")
    for chapter_row in combined_chapter_rows:
        cells = [md_escape(chapter_row["ChapterName"]), str(chapter_row["total"])]
        for model in MODELS:
            correct = chapter_row[f"{model['key']}_correct"]
            total = chapter_row[f"{model['key']}_total"]
            accuracy = chapter_row[f"{model['key']}_accuracy"]
            cells.append(f"{correct}/{total} ({pct(accuracy)})")
        lines.append("| " + " | ".join(cells) + " |")
    lines.append("")
    lines.append("## Output Files")
    lines.append("")
    lines.append(f"- `{SUMMARY_DIR / 'all_models_overall_accuracy.csv'}`")
    lines.append(f"- `{SUMMARY_DIR / 'all_models_overall_accuracy.json'}`")
    lines.append(f"- `{SUMMARY_DIR / 'all_models_chapter_accuracy.csv'}`")
    lines.append(f"- `{SUMMARY_DIR / 'all_models_chapter_accuracy.json'}`")
    for model in MODELS:
        lines.append(f"- `{model['labels']}`")
        lines.append(f"- `{model['prefix']}_overall_accuracy.json`")
        lines.append(f"- `{model['prefix']}_chapter_accuracy.csv`")
    lines.append("")

    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def write_accuracy_report(overall_rows: list[dict], combined_chapter_rows: list[dict]) -> None:
    ranked = sorted(overall_rows, key=lambda row: row["accuracy"], reverse=True)

    lines: list[str] = []
    lines.append("# Research GPT-4.1 Cropped Accuracy")
    lines.append("")
    lines.append("## Overall Accuracy")
    lines.append("")
    lines.append("| Rank | Model | Correct | Incorrect | Total | Accuracy |")
    lines.append("|---:|---|---:|---:|---:|---:|")
    for index, row in enumerate(ranked, start=1):
        lines.append(
            f"| {index} | {row['model']} | {row['correct']} | {row['incorrect']} | "
            f"{row['total']} | {pct(row['accuracy'])} |"
        )
    lines.append("")
    lines.append("## Chapter Accuracy")
    lines.append("")
    lines.append(
        "| Chapter | Total | GPT-5 | Qwen3-4B | Mistral 3B | Qwen2.5-7B | "
        "Gemma3-4B | Llama 3.2 3B Instruct |"
    )
    lines.append("|---|---:|---:|---:|---:|---:|---:|---:|")
    for chapter_row in combined_chapter_rows:
        cells = [md_escape(chapter_row["ChapterName"]), str(chapter_row["total"])]
        for model in MODELS:
            correct = chapter_row[f"{model['key']}_correct"]
            total = chapter_row[f"{model['key']}_total"]
            accuracy = chapter_row[f"{model['key']}_accuracy"]
            cells.append(f"{correct}/{total} ({pct(accuracy)})")
        lines.append("| " + " | ".join(cells) + " |")
    lines.append("")

    ACCURACY_REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    SUMMARY_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)

    overall_rows = []
    chapter_maps = {}
    for model in MODELS:
        overall, chapter_rows, _ = summarize_model(model)
        overall_rows.append(overall)
        chapter_maps[model["key"]] = {row["ChapterName"]: row for row in chapter_rows}

    combined_chapter_rows = build_combined_chapter_rows(chapter_maps)

    write_json(SUMMARY_DIR / "all_models_overall_accuracy.json", overall_rows)
    write_csv(
        SUMMARY_DIR / "all_models_overall_accuracy.csv",
        overall_rows,
        ["model", "total", "correct", "incorrect", "accuracy"],
    )

    chapter_fieldnames = ["ChapterName", "total"]
    for model in MODELS:
        chapter_fieldnames.extend(
            [
                f"{model['key']}_correct",
                f"{model['key']}_total",
                f"{model['key']}_accuracy",
            ]
        )
    write_json(SUMMARY_DIR / "all_models_chapter_accuracy.json", combined_chapter_rows)
    write_csv(
        SUMMARY_DIR / "all_models_chapter_accuracy.csv",
        combined_chapter_rows,
        chapter_fieldnames,
    )
    write_report(overall_rows, combined_chapter_rows)
    write_accuracy_report(overall_rows, combined_chapter_rows)

    print(f"Wrote {REPORT_PATH}")
    print(f"Wrote {ACCURACY_REPORT_PATH}")
    print(f"Wrote {SUMMARY_DIR / 'all_models_overall_accuracy.csv'}")
    print(f"Wrote {SUMMARY_DIR / 'all_models_chapter_accuracy.csv'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
