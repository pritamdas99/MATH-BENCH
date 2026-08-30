#!/usr/bin/env python3
"""Build the GPT-4.1 judge evaluation markdown report."""

from __future__ import annotations

import json
from pathlib import Path


MODELS = [
    {
        "key": "qwen3",
        "name": "Qwen3-4B",
        "prefix": "results/research_gpt41/summaries/research_gpt41_qwen3_4b",
        "labels": "results/research_gpt41/labels/research_gpt41_qwen3_4b_answer_labels.jsonl",
    },
    {
        "key": "gemma",
        "name": "Gemma3-4B",
        "prefix": "results/research_gpt41/summaries/research_gpt41_gemma3_4b",
        "labels": "results/research_gpt41/labels/research_gpt41_gemma3_4b_answer_labels.jsonl",
    },
    {
        "key": "mistral",
        "name": "Mistral 3B",
        "prefix": "results/research_gpt41/summaries/research_gpt41_mistral3_3b",
        "labels": "results/research_gpt41/labels/research_gpt41_mistral3_3b_answer_labels.jsonl",
    },
    {
        "key": "llama",
        "name": "Llama 3.2 3B",
        "prefix": "results/research_gpt41/summaries/research_gpt41_llama3_2_3b_instruct",
        "labels": "results/research_gpt41/labels/research_gpt41_llama3_2_3b_instruct_answer_labels.jsonl",
    },
    {
        "key": "qwen2.5",
        "name": "Qwen2.5-7B",
        "prefix": "results/research_gpt41/summaries/research_gpt41_qwen2_5_7b",
        "labels": "results/research_gpt41/labels/research_gpt41_qwen2.5_7b_answer_labels.jsonl",
    },
    {
        "key": "gpt",
        "name": "GPT-5",
        "prefix": "results/research_gpt41/summaries/research_gpt41_gpt5",
        "labels": "results/research_gpt41/labels/research_gpt41_gpt5_answer_labels.jsonl",
    },
]


def read_json(path: str) -> object:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def read_jsonl(path: str) -> list[dict]:
    with Path(path).open(encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def pct(value: float) -> str:
    return f"{value * 100:.2f}%"


def md_escape(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


def bar(value: float, width: int = 24) -> str:
    filled = round(value * width)
    return "█" * filled + "░" * (width - filled)


def main() -> int:
    overall = {}
    costs = {}
    for model in MODELS:
        overall[model["key"]] = read_json(f"{model['prefix']}_overall_accuracy.json")
        labels = read_jsonl(model["labels"])
        costs[model["key"]] = sum(float(row.get("judge_cost_usd_estimate") or 0) for row in labels)

    chapter_maps = {}
    all_chapters: dict[str, int] = {}
    for model in MODELS:
        rows = read_json(f"{model['prefix']}_chapter_accuracy.json")
        chapter_maps[model["key"]] = {row["ChapterName"]: row for row in rows}
        for row in rows:
            all_chapters[row["ChapterName"]] = int(row["total"])

    ordered_chapters = sorted(all_chapters, key=lambda item: (-all_chapters[item], item))
    total_cost = sum(costs.values())

    lines: list[str] = []
    lines.append("# GPT-4.1 LLM-as-Judge Final-Answer Evaluation")
    lines.append("")
    lines.append("This report evaluates the generated final answers from four models using `openai/gpt-4.1` through OpenRouter as an LLM-as-judge. The judge compared the expected final answer against the model-generated final-answer candidate and assigned `1` for correct and `0` for incorrect.")
    lines.append("")
    lines.append("## Method")
    lines.append("")
    lines.append("- Judge model: `openai/gpt-4.1` via OpenRouter.")
    lines.append("- Evaluation target: final-answer equivalence only.")
    lines.append("- Input to judge: expected final answer and extracted generated final-answer candidate; raw generated-answer tail was included only when extraction was missing or malformed.")
    lines.append("- Grading: `1` if complete and mathematically equivalent; `0` if wrong, incomplete, missing a required part/condition/unit, wrong sign, contradictory, or no clear final answer.")
    lines.append("- Formatting tolerance: LaTeX spacing, boxes, Bengali/English digits, equivalent exact/decimal forms, and `C`/`c` integration constants were treated as harmless.")
    lines.append("- This report is intentionally based on the LLM-as-judge pass, not on the earlier manually corrected labels.")
    lines.append(f"- Estimated OpenRouter judge cost recorded from API usage: `${total_cost:.4f}`.")
    lines.append("")
    lines.append("## Overall Accuracy")
    lines.append("")
    lines.append("| Model | Correct | Incorrect | Total | Accuracy | Judge Cost |")
    lines.append("|---|---:|---:|---:|---:|---:|")
    for model in MODELS:
        item = overall[model["key"]]
        lines.append(
            f"| {model['name']} | {item['correct']} | {item['incorrect']} | {item['total']} | {pct(item['accuracy'])} | ${costs[model['key']]:.4f} |"
        )
    lines.append("")
    lines.append("### Overall Accuracy Graph")
    lines.append("")
    lines.append("| Model | Accuracy | Bar |")
    lines.append("|---|---:|---|")
    for model in MODELS:
        accuracy = overall[model["key"]]["accuracy"]
        lines.append(f"| {model['name']} | {pct(accuracy)} | `{bar(accuracy)}` |")
    lines.append("")
    lines.append("```mermaid")
    lines.append("xychart-beta")
    lines.append('  title "Overall Accuracy by Model"')
    lines.append('  x-axis ["Qwen3-4B", "Gemma3-4B", "Mistral 3B", "Llama 3.2 3B", "Qwen2.5-7B", "GPT-5"]')
    lines.append("  y-axis \"Accuracy (%)\" 0 --> 50")
    values = ", ".join(f"{overall[model['key']]['accuracy'] * 100:.2f}" for model in MODELS)
    lines.append(f"  bar [{values}]")
    lines.append("```")
    lines.append("")
    lines.append("## Chapter-by-Chapter Accuracy")
    lines.append("")
    lines.append("| Chapter | Total | Qwen3-4B | Gemma3-4B | Mistral 3B | Llama 3.2 3B | Qwen2.5-7B | GPT-5 |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|---:|")
    for chapter in ordered_chapters:
        cells = [md_escape(chapter), str(all_chapters[chapter])]
        for model in MODELS:
            row = chapter_maps[model["key"]].get(chapter)
            if row:
                cells.append(f"{row['correct']}/{row['total']} ({pct(row['accuracy'])})")
            else:
                cells.append("0/0 (0.00%)")
        lines.append("| " + " | ".join(cells) + " |")
    lines.append("")
    lines.append("## Output Files")
    lines.append("")
    for model in MODELS:
        prefix = model["prefix"]
        lines.append(f"- `{model['labels']}`")
        lines.append(f"- `{prefix}_overall_accuracy.json`")
        lines.append(f"- `{prefix}_evaluation_per_id_with_chapter.jsonl`")
        lines.append(f"- `{prefix}_chapter_accuracy.json`")
    lines.append("")

    Path("reports/research_gpt41_evaluation_report.md").write_text(
        "\n".join(lines),
        encoding="utf-8",
    )
    print("Wrote reports/research_gpt41_evaluation_report.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
