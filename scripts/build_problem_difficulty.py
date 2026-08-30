#!/usr/bin/env python3
"""Build per-problem difficulty from cropped labels and manual failure notes."""

from __future__ import annotations

import csv
import json
import re
from collections import Counter
from pathlib import Path
from typing import NamedTuple


LABEL_DIR = Path("results/research_gpt41/labels")
OUT_DIR = Path("results/research_gpt41/difficulty")
REPORT_PATH = Path("reports/research_gpt41_problem_difficulty.md")

NOTE_PATH = Path(
    r"C:\Users\User\.codex\attachments\ae957e70-f953-47a3-bc08-817dd4af56b7\pasted-text.txt"
)

MODELS = {
    "gemma": LABEL_DIR / "research_gpt41_gemma3_4b_answer_labels_cropped.jsonl",
    "qwen": LABEL_DIR / "research_gpt41_qwen3_4b_answer_labels_cropped.jsonl",
    "mistral": LABEL_DIR / "research_gpt41_mistral3_3b_answer_labels_cropped.jsonl",
}

# Notes like "reasoning correct but final/format wrong" should not make a
# problem look mathematically difficult. These are explanation-aware overrides.
NON_REASONING_OVERRIDES: dict[str, dict[str, str]] = {
    "5": {"gemma": "correct reasoning; final answer copied incorrectly"},
    "7": {"mistral": "correct solution with contradictory extra statements"},
    "25": {
        "gemma": "reasoning ok; answer mismatch is mainly format/incomplete final",
        "qwen": "reasoning ok; answer mismatch is mainly format/incomplete final",
        "mistral": "reasoning ok; answer mismatch is mainly format/incomplete final",
    },
    "39": {"qwen": "correct solution; both roots found but final lists one"},
    "56": {
        "qwen": "definition mismatch: inclusive vs expected exclusive trapezium",
        "mistral": "definition mismatch: inclusive vs expected exclusive trapezium",
    },
    "73": {"qwen": "reasoning mostly correct; incomplete tangent/normal final"},
    "80": {
        "gemma": "reasoning and calculation correct; final did not list both requested values",
        "qwen": "reasoning and calculation correct; final did not list both requested values",
        "mistral": "reasoning and calculation correct; final did not list both requested values",
    },
    "85": {"gemma": "two roots found but final lists one"},
    "115": {"qwen": "reasoning and calculation correct; final omits angle"},
}


def read_jsonl(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as infile:
        return [json.loads(line) for line in infile if line.strip()]


def parse_label(row: dict) -> int:
    value = row.get("labels", row.get("label"))
    text = str(value).strip()
    if text not in {"0", "1"}:
        raise ValueError(f"Bad label {value!r} for id={row.get('id')}")
    return int(text)


class Note(NamedTuple):
    body: str
    mentioned_models: set[str]
    applies_to_all: bool


def models_mentioned(body: str) -> set[str]:
    text = body.lower()
    mentioned: set[str] = set()
    if "gemma" in text:
        mentioned.add("gemma")
    if "qwen" in text or "quen" in text:
        mentioned.add("qwen")
    if "mistral" in text:
        mentioned.add("mistral")
    return mentioned


def note_applies_to_all(body: str) -> bool:
    text = body.lower()
    return any(
        marker in text
        for marker in [
            "all the models",
            "all models",
            "all 3",
            "all three",
            "model solutions",
            "models are not",
        ]
    )


def parse_notes(path: Path) -> dict[str, Note]:
    if not path.exists():
        return {}

    text = path.read_text(encoding="utf-8", errors="replace")
    pattern = re.compile(
        r"(?ims)^\s*id\s*:?\s*([0-9]+(?:\s*,\s*[0-9]+)*)\s*:?\s*"
        r"(.*?)(?=^\s*id\s*:?\s*[0-9]|\Z)"
    )
    notes: dict[str, Note] = {}
    for match in pattern.finditer(text):
        ids = [item.strip() for item in match.group(1).split(",")]
        body = " ".join(line.strip() for line in match.group(2).splitlines() if line.strip())
        note = Note(
            body=body,
            mentioned_models=models_mentioned(body),
            applies_to_all=note_applies_to_all(body),
        )
        for row_id in ids:
            notes[row_id] = note
    return notes


def compact(text: str, max_len: int = 260) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= max_len:
        return text
    return text[: max_len - 3].rstrip() + "..."


def difficulty_from_count(genuine_failures: int) -> str:
    if genuine_failures <= 1:
        return "Easy"
    if genuine_failures == 2:
        return "Medium"
    return "Hard"


def build_rows() -> list[dict]:
    by_id: dict[str, dict] = {}
    for model, path in MODELS.items():
        for row in read_jsonl(path):
            row_id = str(row["id"])
            item = by_id.setdefault(
                row_id,
                {
                    "id": row_id,
                    "ChapterName": row.get("ChapterName", ""),
                    "expected_final_answer": row.get("expected_final_answer", ""),
                },
            )
            item[f"{model}_label"] = parse_label(row)

    notes = parse_notes(NOTE_PATH)

    rows: list[dict] = []
    for row_id in sorted(by_id, key=lambda value: int(value)):
        item = by_id[row_id]
        failed_models = [
            model for model in MODELS if item.get(f"{model}_label", 0) == 0
        ]
        note = notes.get(row_id)
        if note is None:
            listed_failure_models = set(failed_models)
        elif not note.body:
            listed_failure_models = set()
        elif note.applies_to_all or not note.mentioned_models:
            listed_failure_models = set(failed_models)
        else:
            listed_failure_models = note.mentioned_models & set(failed_models)

        non_reasoning = {
            model: "not listed in manual mistake notes; treated as correct/false-positive label"
            for model in failed_models
            if model not in listed_failure_models
        }
        non_reasoning.update(
            {
            model: reason
            for model, reason in NON_REASONING_OVERRIDES.get(row_id, {}).items()
            if model in failed_models
            }
        )
        genuine_models = [
            model for model in failed_models if model not in non_reasoning
        ]

        raw_failure_count = len(failed_models)
        genuine_failure_count = len(genuine_models)
        difficulty = difficulty_from_count(genuine_failure_count)
        note_text = note.body if note else ""
        if note is None:
            source = "model_labels_only"
        elif note.body:
            source = "manual_note_plus_labels"
        else:
            source = "manual_blank_note_plus_labels"

        if genuine_failure_count == 0:
            rationale = "All three target models solved it, or failures are final-format/non-reasoning only."
        elif genuine_failure_count == 1:
            rationale = "Only one target model has a genuine failure; most models solved the reasoning."
        elif genuine_failure_count == 2:
            rationale = "Two target models have genuine failures, so the problem has moderate reasoning difficulty."
        else:
            rationale = "All three target models have genuine failures, indicating a hard reasoning problem."

        rows.append(
            {
                "id": row_id,
                "ChapterName": item["ChapterName"],
                "difficulty": difficulty,
                "genuine_failure_count": genuine_failure_count,
                "raw_failure_count": raw_failure_count,
                "failed_models": ",".join(failed_models),
                "non_reasoning_models": ",".join(non_reasoning),
                "genuine_failed_models": ",".join(genuine_models),
                "gemma_label": item["gemma_label"],
                "qwen_label": item["qwen_label"],
                "mistral_label": item["mistral_label"],
                "source": source,
                "rationale": rationale,
                "manual_note": compact(note_text),
                "non_reasoning_reason": compact("; ".join(non_reasoning.values())),
            }
        )

    return rows


def write_csv(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8", newline="") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def write_jsonl(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8") as outfile:
        for row in rows:
            outfile.write(json.dumps(row, ensure_ascii=False) + "\n")


def write_report(rows: list[dict]) -> None:
    counts = Counter(row["difficulty"] for row in rows)
    genuine_counts = Counter(row["genuine_failure_count"] for row in rows)
    source_counts = Counter(row["source"] for row in rows)

    lines = [
        "# Research GPT-4.1 Cropped Problem Difficulty",
        "",
        "Difficulty is assigned from the Gemma, Qwen, and Mistral cropped labels, "
        "then corrected with the attached manual explanations where a wrong label "
        "is actually a final-format or non-reasoning issue.",
        "",
        "Rules:",
        "",
        "- Easy: 0 or 1 genuine reasoning failure among the three target models.",
        "- Medium: 2 genuine reasoning failures.",
        "- Hard: 3 genuine reasoning failures.",
        "- Explicit false positives and final-format-only misses are excluded from the genuine failure count.",
        "",
        "## Summary",
        "",
        "| Difficulty | Problems |",
        "|---|---:|",
    ]
    for label in ["Easy", "Medium", "Hard"]:
        lines.append(f"| {label} | {counts[label]} |")

    lines.extend(
        [
            "",
            "## Genuine Failure Counts",
            "",
            "| Genuine failures | Problems |",
            "|---:|---:|",
        ]
    )
    for count in [0, 1, 2, 3]:
        lines.append(f"| {count} | {genuine_counts[count]} |")

    lines.extend(
        [
            "",
            "## Source Coverage",
            "",
            "| Source | Problems |",
            "|---|---:|",
        ]
    )
    for source, count in sorted(source_counts.items()):
        lines.append(f"| {source} | {count} |")

    lines.extend(
        [
            "",
            "## Output Files",
            "",
            f"- `{OUT_DIR / 'problem_difficulty_cropped.csv'}`",
            f"- `{OUT_DIR / 'problem_difficulty_cropped.jsonl'}`",
            "",
        ]
    )
    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)

    rows = build_rows()
    write_csv(OUT_DIR / "problem_difficulty_cropped.csv", rows)
    write_jsonl(OUT_DIR / "problem_difficulty_cropped.jsonl", rows)
    write_report(rows)

    print(f"Wrote {OUT_DIR / 'problem_difficulty_cropped.csv'}")
    print(f"Wrote {OUT_DIR / 'problem_difficulty_cropped.jsonl'}")
    print(f"Wrote {REPORT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
