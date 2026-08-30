from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LABEL_DIR = ROOT / "results" / "research_gpt41" / "labels"
OUT_DIR = ROOT / "results" / "research_gpt41" / "analysis"

MODEL_FILES = {
    "qwen2.5": LABEL_DIR / "research_gpt41_qwen2.5_7b_answer_labels_cropped.jsonl",
    "gpt5": LABEL_DIR / "research_gpt41_gpt5_answer_labels_cropped.jsonl",
}

OUT_PATH = OUT_DIR / "qwen25_gpt5_failure_reasons_1_to_115.md"

CHAPTER_HINTS = {
    "ম্যাট্রিক্স": "ম্যাট্রিক্সের গুণ, inverse/determinant, dimension অথবা scalar factor ঠিকভাবে ব্যবহার করেনি।",
    "ভেক্টর": "ভেক্টরের component, magnitude, projection/cross product অথবা direction condition ঠিকভাবে প্রয়োগ করেনি।",
    "সরলরেখা": "রেখার slope/intercept/distance/angle/area সম্পর্কিত formula বা sign/condition ভুল প্রয়োগ করেছে।",
    "বৃত্ত": "বৃত্তের center-radius form, tangent/normal relation, অথবা point-on-circle condition ঠিকভাবে ব্যবহার করেনি।",
    "বিন্যাস": "counting case, permutation/combination formula, অথবা overcount/undercount ঠিকভাবে সামলাতে পারেনি।",
    "সমাবেশ": "counting case, permutation/combination formula, অথবা overcount/undercount ঠিকভাবে সামলাতে পারেনি।",
}


def read_jsonl(path: Path) -> dict[str, dict]:
    rows: dict[str, dict] = {}
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            row = json.loads(line)
            rows[str(row["id"])] = row
    return rows


def one_line(value: object, limit: int = 220) -> str:
    text = "" if value is None else str(value)
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= limit:
        return text
    return text[: limit - 3].rstrip() + "..."


def normalize_math(text: str) -> str:
    lowered = text.lower()
    lowered = re.sub(r"\\boxed|\\text|\\left|\\right|\\begin|\\end", "", lowered)
    lowered = re.sub(r"[^a-z0-9০-৯অ-হ+\-*/=().,^{}\\\\]", "", lowered)
    return lowered


def chapter_hint(chapter: str) -> str:
    for key, hint in CHAPTER_HINTS.items():
        if key in chapter:
            return hint
    return "প্রয়োজনীয় গাণিতিক শর্ত বা algebraic simplification ঠিকভাবে সম্পন্ন করেনি।"


def looks_like_extraction_issue(predicted_final: str, predicted_answer: str) -> bool:
    final = predicted_final.strip()
    if not final:
        return False
    if final.startswith("=") or final.startswith("}") or final.endswith("{"):
        return True
    if len(final) < 12 and len(predicted_answer) > 300:
        return True
    return False


def make_reason(row: dict | None) -> tuple[str, str]:
    if row is None:
        return "missing", "এই model-এর জন্য id-টি cropped label file-এ পাওয়া যায়নি।"

    label = int(row.get("labels", 0))
    expected = one_line(row.get("expected_final_answer", ""), 160)
    final = one_line(row.get("predicted_final_answer", ""), 180)
    full_answer = row.get("predicted_answer", "") or ""
    chapter = row.get("ChapterName", "")

    if label == 1:
        return "correct", "সঠিক; failure নেই।"

    if not final:
        return "failure", "চূড়ান্ত উত্তর অনুপস্থিত/খালি বা অসম্পূর্ণ; model সমাধান শেষ করতে পারেনি।"

    expected_norm = normalize_math(expected)
    final_norm = normalize_math(final)
    answer_norm = normalize_math(full_answer)

    if expected_norm and (expected_norm in final_norm or expected_norm in answer_norm):
        return "likely_false_negative", (
            "সমাধান/চূড়ান্ত অংশে expected উত্তর উপস্থিত বা সমতুল্য form আছে; "
            "এটি সম্ভবত formatting/final-extraction mismatch, genuine math failure নয়।"
        )

    if looks_like_extraction_issue(str(row.get("predicted_final_answer", "")), full_answer):
        return "possible_extraction_issue", (
            "predicted_final_answer কাটা/ভাঙা দেখাচ্ছে; final extraction issue হতে পারে। "
            f"তবু extracted final expected `{expected}`-এর সঙ্গে সরাসরি মেলেনি।"
        )

    return "failure", (
        f"Expected `{expected}`, কিন্তু model দিয়েছে `{final}`। "
        f"অতএব {chapter_hint(chapter)}"
    )


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    model_rows = {model: read_jsonl(path) for model, path in MODEL_FILES.items()}

    lines = [
        "# Qwen2.5 and GPT-5 Failure Reasons for IDs 1-115",
        "",
        "Scope: ids 1-115 only; models: qwen2.5 and gpt5. Llama excluded.",
        "",
        "Status legend:",
        "- correct: model answer is labelled correct; no failure recorded.",
        "- failure: expected and predicted answer do not match; reason is inferred from answer mismatch and chapter context.",
        "- likely_false_negative: expected answer appears in the model output but label/final extraction marked it wrong.",
        "- possible_extraction_issue: extracted final answer is visibly truncated or malformed.",
        "",
    ]

    for problem_id in range(1, 116):
        pid = str(problem_id)
        available = [rows.get(pid) for rows in model_rows.values() if rows.get(pid)]
        if not available:
            lines.extend([f"## id {pid}", "", "Record not found in qwen2.5 or gpt5 cropped files.", ""])
            continue

        base = available[0]
        lines.extend([
            f"## id {pid}",
            "",
            f"Chapter: {base.get('ChapterName', '')}",
            "",
            f"Question: {one_line(base.get('question', ''), 360)}",
            "",
            f"Expected: {one_line(base.get('expected_final_answer', ''), 260)}",
            "",
        ])

        for model in ["qwen2.5", "gpt5"]:
            row = model_rows[model].get(pid)
            status, reason = make_reason(row)
            if row is None:
                predicted = ""
                label = "missing"
            else:
                predicted = one_line(row.get("predicted_final_answer", ""), 260)
                label = str(row.get("labels", ""))
            lines.extend([
                f"### {model}",
                "",
                f"Label: {label}",
                "",
                f"Status: {status}",
                "",
                f"Predicted final: {predicted}",
                "",
                f"Failure reason: {reason}",
                "",
            ])

    OUT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(OUT_PATH)


if __name__ == "__main__":
    main()
