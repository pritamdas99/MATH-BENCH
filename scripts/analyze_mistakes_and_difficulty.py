from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LABEL_DIR = ROOT / "results" / "research_gpt41" / "labels"
OUT_DIR = ROOT / "results" / "research_gpt41" / "analysis"
DIFFICULTY_DIR = ROOT / "results" / "research_gpt41" / "difficulty"
DIFFICULTY_SPLIT_DIR = OUT_DIR / "difficulty_splits"
NOTE_PATH = Path(
    r"C:\Users\User\.codex\attachments\3f12590d-7c7b-4946-9765-8983aeb2dd4b\pasted-text.txt"
)
QWEN25_GPT5_1_TO_115_PATH = OUT_DIR / "qwen25_gpt5_failure_reasons_1_to_115.md"

MODEL_FILES = {
    "gpt5": "research_gpt41_gpt5_answer_labels_cropped.jsonl",
    "qwen3_4b": "research_gpt41_qwen3_4b_answer_labels_cropped.jsonl",
    "qwen2_5_7b": "research_gpt41_qwen2.5_7b_answer_labels_cropped.jsonl",
    "gemma3_4b": "research_gpt41_gemma3_4b_answer_labels_cropped.jsonl",
    "mistral3_3b": "research_gpt41_mistral3_3b_answer_labels_cropped.jsonl",
    "llama3_2_3b": "research_gpt41_llama3_2_3b_instruct_answer_labels_cropped.jsonl",
}

MODEL_ORDER = [
    "gpt5",
    "qwen3_4b",
    "qwen2_5_7b",
    "gemma3_4b",
    "mistral3_3b",
    "llama3_2_3b",
]

MANUAL_MODEL_ORDER = [
    "gpt5",
    "qwen3_4b",
    "qwen2_5_7b",
    "gemma3_4b",
    "mistral3_3b",
]

DIFFICULTY_MODEL_ORDER = [
    "qwen3_4b",
    "qwen2_5_7b",
    "gemma3_4b",
    "mistral3_3b",
]

MODEL_ALIASES = {
    "gpt5": ["gpt5", "gpt-5", "gpt"],
    "qwen3_4b": ["qwen3", "qwen 3", "quen", "qwen:"],
    "qwen2_5_7b": ["qwen2.5", "qwen 2.5", "qwen2_5"],
    "gemma3_4b": ["gemma"],
    "mistral3_3b": ["mistral", "ministral"],
    "llama3_2_3b": ["llama"],
}

ERROR_PATTERNS = [
    ("format_or_final_extraction", [
        "format", "answer mismatch", "final predicted", "copied wrongly",
        "only one answer", "required 2", "provided in final answer", "final answer",
        "not taking", "didn't take", "didnt take",
        "possible_extraction_issue", "extraction issue",
        "final blank", "predicted final blank", "final খালি", "final নেই",
        "final দেয়নি", "final দেয়নি", "answer truncated", "truncated",
        "indefinite answer",
    ]),
    ("output_corruption", ["corrupted", "�", "Ġ", "Ċ"]),
    ("no_or_insufficient_reasoning", [
        "didnt even solve", "didn't even solve", "without any calculation",
        "without reasoning", "provided a wrong answer without reasoning",
        "didnt solve whole math", "not enough", "cannot determine",
        "চূড়ান্ত উত্তর অনুপস্থিত", "চূড়ান্ত উত্তর অনুপস্থিত",
        "final ফাঁকা", "final answer দেয়নি", "সমাধান শেষ করতে পারেনি",
        "সংখ্যা গণনা করেনি", "শুধু কয়েকটি example",
        "incomplete", "reasoning incomplete", "থেমে গেছে",
        "দেয়নি", "দেয়নি",
        "solution complete করেনি", "complete করেনি", "সম্পূর্ণ করেনি",
        "substantive solution সম্পূর্ণ করেনি", "generic text",
        "উত্তর অসম্পূর্ণ", "answer অসম্পূর্ণ", "setup করেছে কিন্তু solution complete",
        "নির্ণয় করা সম্ভব নয়", "নির্ণয় করা সম্ভব নয়",
    ]),
    ("geometry_condition_error", [
        "perpendicular দিকে", "same line extension", "নতুন রেখা নিয়েছে",
        "প্রদত্ত রেখা", "দূরত্ব", "distance numerator", "midpoint না",
        "midpoint দিয়ে না", "endpoint দিয়ে", "perpendicular bisector",
        "perpendicular foot", "tangent point", "tangent circles",
        "tangent না", "intercept condition", "axis intersection",
        "origin বৃত্তের উপর", "diameter line", "vertical tangent",
        "top/bottom points", "circle দরকার", "circle", "বৃত্ত",
        "radius", "center-এর দূরত্ব", "y\\)-অক্ষ থেকে", "x\\)-axis",
        "x-axis", "given line-এর সাথে", "parallel", "trapezium",
        "দ্বিতীয় জোড়া parallel", "area condition", "constant",
        "point-on-circle", "চাপ", "জ্যা",
    ]),
    ("question_misinterpretation", [
        "didnt understand", "didn't understand", "failed to understand",
        "fails to understand", "not able to understand", "question requires",
        "instead of", "assumed", "ধরে", "মানে",
        "asked scaler", "asked scalar", "while asked", "project while asked",
        "problem-টাই ভুল interpret", "ভুল interpret",
        "interpret করেছে", "মূল চাহিদা", "irrelevant/general expression",
        "problem-এ", "curve-specific geometry ধরতে পারেনি",
        "solve করা সম্ভব নয়",
        "same line extension", "perpendicular দিকে না",
        "অক্ষে হওয়ায়", "হওয়া উচিত",
    ]),
    ("dimension_or_structure_error", [
        "dimension", "3 by 1", "3 by 3",
    ]),
    ("arithmetic_or_algebra_error", [
        "calculation", "arithmetic", "multiplying", "minor",
        "determinant", "simplification", "equation", "sign", "silly math",
        "middle of solving", "mistake while", "mnistake",
        "ভুল করে", "ভুল করেছে", "না নিয়ে", "পায়নি", "পেয়ে", "লিখেছে",
        "alpha=60", "\\alpha=60", "normalization factor", "coefficient",
        "মান", "value", "evaluation ভুল", "limit/substitution evaluation",
        "ঠিকভাবে যোগ করেনি", "factor ঠিক রাখেনি", "factor হারিয়েছে",
        "হারিয়েছে", "factor বাদ", "u\\) factor বাদ", "cancel", "combine করেনি", "term ঠিকভাবে",
        "cubic term", "standard limit", "chain rule", "outside",
        "factor ঠিকভাবে", "expression ভুল", "ভুল expression",
        "lower limit", "ভুল intersection", "extra", "numerator",
        "derivative করলে", "পাওয়া যায় না", "পাওয়া যায় না",
        "cube-root ভুল", "terms ঠিকভাবে collect করেনি", "ঠিকভাবে collect করেনি",
        "limit \\(0\\)", "factor আসে", "factor missing", "factor \\(2\\)",
        "expected-এর negative", "negative", "log term", "unnecessary log",
        "term এনেছে", "handle করেনি", "structure ঠিকভাবে", "polynomial reduction",
        "vieta", "root-dependent condition", "relation ভুল", "equation simplification",
        "critical point", "minimization step", "torque equation", "moment equation",
        "balance point", "wrong pair", "ভুল pair", "numeric roots নয়",
        "শূন্য-যোগফল", "দিয়েছে, expected নয়", "দিয়েছে। expected", "ভুল answer",
        "বসালে", "satisfy করে না", "height বা base ভুল", "moment arm",
        "moment balance", "center distance", "ratio উল্টো", "ratio ভুল",
        "ভুল নিয়েছে", "ভুল নিয়েছে", "distance ভুল", "quadratic satisfy",
    ]),
    ("formula_or_method_error", [
        "wrong approach", "wrong solution method", "wrong method",
        "failed to get",
        "wrong way", "solving in wrong way", "without figuring out",
        "ঠিকভাবে নেয়নি", "ঠিকভাবে ব্যবহার করেনি",
        "identity", "product-to-sum", "substitution", "midpoint line",
        "perpendicular chord", "bisector-এর", "intercept না",
        "ভুল distance", "slope ভুল", "standard form",
        "sorted rank logic", "rank logic", "combination করেছে",
        "permutation নয়", "order matters", "order consider করেনি",
        "repeated letters consider না", "overcount", "permutation-type",
        "sine rule ব্যবহার", "ব্যবহার করেনি", "derivative ratio",
        "dy/dt", "dx/dt", "implicit differentiation", "isolate",
        "differentiation না করে integration", "operation-টাই ভুল",
        "parameter identities", "চিনতে পারেনি", "inverse নিতে ভুলেছে",
        "composition inverse", "valid example-কে general relation",
        "consonant/vowel placement", "ছোট permutation", "permutation",
        "combination", "order", "repeated letters", "rank logic",
        "integral setup", "antiderivative", "derivative-recognition",
        "rationalization", "bounded lens area", "expansion",
        "integrate", "integral", "log terms", "sector", "subtraction",
        "integration mix", "invalid setup", "bounded region", "boundary",
        "left-right boundary", "limits/shape", "definite integral evaluate",
        "original integrand", "derivative form", "simple derivative form",
        "ei-type",
        "wrong formula", "cross product", "projection", "angle bisector",
        "normal form", "intercepts", "slope", "formula",
        "general expression নয়", "line subtract করেনি", "শুধু parabola",
        "curve-এর area", "triangle term যোগ", "segment", "bounded",
        "tangent ratio নয়", "integrand-এ সেই", "quotient derivative",
        "non-elementary", "special function", "substitution", "locus",
        "conic চিনতে", "directrix", "eccentricity", "foci",
        "common-root condition", "ap root relation", "reciprocal roots",
        "root-square condition", "principal root", "fourth power",
        "principal root বা", "stated problem অনুযায়ী justified maximum নয়",
        "phase angle", "actual pair নির্দিষ্ট করেনি", "given interval",
        "notation error", "integer হওয়া দরকার", "connector line নয়",
        "equal reaction condition", "optimization করেনি", "তথ্য যথেষ্ট নয়",
        "force line", "components বের করা যায়", "maximum moment",
    ]),
    ("missing_case_or_domain_error", [
        "both", "only 5", "-5", "two answers", "all solutions", "domain",
        "range", "n*pi", "±", "+/-",
        "case", "বাদ দিয়েছে", "বাদ দিয়েছে", "branch বাদ", "special case",
        "ডোমেন", "range দিয়েছে", "domain দিয়েছে",
        "দুই root", "দুইটি", "একটাই দিয়েছে", "k=-1", "solve করেনি",
        "solution incomplete", "reasoning incomplete", "endpoint valid",
        "endpoint", "পূর্ণ condition",
        "শুধু একটি", "শুধু principal root", "সব ৬টি root নয়",
        "চারটি root দরকার", "সব root নয়", "root পেলেও final-এ শুধু",
        "বাদ নেই", "exclude করে না", "undefined point", "অসজ্ঞায়িত",
        "অসংজ্ঞায়িত", "principal root দিয়েছে", "\\pm বাদ", "± বাদ",
        "শুধু positive root", "positive root দিয়েছে", "অতিরিক্ত দিয়েছে",
        "extra root", "invalid root", "অনেক invalid root", "root ঢুকেছে",
        "দুই peg-এর অবস্থান", "দুই peg",
    ]),
    ("wrong_final_value_or_expression", [
        "mistake.", "ভুল।", "আংশিক ভুল", "দিয়েছে। Label 0",
        "দিয়েছে। label 0", "expected নয়", "expected থেকে আলাদা",
        "expected থেকে ভিন্ন", "জাতীয় উত্তর দিয়েছে", "অস্পষ্ট/ভুল answer",
        "unrelated", "symbolic expression-এ থেমেছে", "clean condition বের করেনি",
        "statement mix করেছে", "বাইরে interval দিয়েছে", "inequality উল্টো",
        "বের করেনি", "ঠিক। label 0", "label 0 ঠিক",
    ]),
    ("same_as_referenced_model_error", [
        "same mistake", "same ভুল", "একই ভুল", "একই cube-root ভুল",
        "gemma-এর মতোই ভুল", "gemma এর মতোই ভুল", "same as",
    ]),
    ("unit_scale_or_magnitude_error", [
        "unit issue", "unit scaling", "scaling", "magnitude", "length",
    ]),
]

GENUINE_FAILURE_HINTS = [
    "wrong", "mistake", "failed", "fails", "didnt", "didn't", "corrupted",
    "not able", "without", "missed", "ভুল",
]

NON_GENUINE_HINTS = [
    "reasoning correct", "reasoning is ok", "correct solution",
    "reasoning and calculation", "correct reasoning",
    "mainly answer mismatch", "format issue", "formatting", "copied wrongly",
    "final incomplete", "angle বাদ",
    "likely_false_negative", "possible_extraction_issue", "extraction issue",
    "false negative",
]


def read_jsonl(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def parse_notes(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}

    text = path.read_text(encoding="utf-8", errors="replace")
    header = re.compile(
        r"(?im)^\s*(?:I[Dd]\s*:?\s*)?([0-9][0-9,\s]*(?:and\s*[0-9]+)?)\s*:?\s*$"
    )
    matches = list(header.finditer(text))
    notes: dict[str, str] = {}

    for idx, match in enumerate(matches):
        id_blob = match.group(1)
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        body = text[start:end].strip()
        ids = re.findall(r"\d+", id_blob)
        for problem_id in ids:
            notes[problem_id] = (notes.get(problem_id, "") + "\n" + body).strip()
    return notes


def parse_qwen25_gpt5_notes(path: Path) -> dict[str, dict[str, dict[str, str]]]:
    if not path.exists():
        return {}

    text = path.read_text(encoding="utf-8", errors="replace")
    id_header = re.compile(r"(?m)^## id (\d+)\s*$")
    model_header = re.compile(r"(?m)^### (qwen2\.5|gpt5)\s*$")
    id_matches = list(id_header.finditer(text))
    parsed: dict[str, dict[str, dict[str, str]]] = {}

    for idx, id_match in enumerate(id_matches):
        problem_id = id_match.group(1)
        start = id_match.end()
        end = id_matches[idx + 1].start() if idx + 1 < len(id_matches) else len(text)
        block = text[start:end]
        model_matches = list(model_header.finditer(block))

        for model_idx, model_match in enumerate(model_matches):
            md_model = model_match.group(1)
            model = "qwen2_5_7b" if md_model == "qwen2.5" else "gpt5"
            model_start = model_match.end()
            model_end = model_matches[model_idx + 1].start() if model_idx + 1 < len(model_matches) else len(block)
            model_block = block[model_start:model_end].strip()
            status_match = re.search(r"(?m)^Status:\s*(.+?)\s*$", model_block)
            reason_match = re.search(r"(?ms)^Failure reason:\s*(.+?)\s*$", model_block)
            label_match = re.search(r"(?m)^Label:\s*(.+?)\s*$", model_block)
            predicted_match = re.search(r"(?m)^Predicted final:\s*(.+?)\s*$", model_block)

            parsed.setdefault(problem_id, {})[model] = {
                "status": status_match.group(1).strip() if status_match else "",
                "reason": reason_match.group(1).strip() if reason_match else "",
                "label": label_match.group(1).strip() if label_match else "",
                "predicted_final": predicted_match.group(1).strip() if predicted_match else "",
            }
    return parsed


def contains_any(text: str, needles: list[str]) -> bool:
    low = text.lower()
    return any(needle.lower() in low for needle in needles)


def note_for_model(note: str, model: str) -> str:
    if not note:
        return ""

    if is_global_error_note(note):
        return note

    blocks = split_model_note_blocks(note)
    if model in blocks:
        return blocks[model]

    if model in {"gpt5", "qwen2_5_7b", "llama3_2_3b"}:
        return ""
    return ""


def split_model_note_blocks(note: str) -> dict[str, str]:
    blocks: dict[str, list[str]] = defaultdict(list)
    current_model = ""

    for raw_line in note.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        model, remainder = parse_model_header(line)
        if model:
            current_model = model
            if remainder:
                blocks[current_model].append(remainder)
            continue
        if current_model:
            blocks[current_model].append(line)

    cleaned = {
        model: f"{model_display_name(model)}: {' '.join(parts).strip()}"
        for model, parts in blocks.items()
        if " ".join(parts).strip()
    }
    gemma_note = cleaned.get("gemma3_4b", "")
    if gemma_note:
        for model, model_note in list(cleaned.items()):
            if model != "gemma3_4b" and "same as gemma" in model_note.lower():
                cleaned[model] = f"{model_note} ({gemma_note})"
    return cleaned


def parse_model_header(line: str) -> tuple[str, str]:
    clean = line.strip().strip("*").strip()
    match = re.match(
        r"^(Gemma(?:/Llama)?|Qwen2\.5|Qwen3|Qwen|Quen|Mistral|MIstral|Ministral|GPT-?5|Llama)(?:\s*:|\s+)(.*)$",
        clean,
        flags=re.I,
    )
    if not match:
        return "", ""

    name = match.group(1).lower()
    remainder = match.group(2).strip().strip("*").strip()
    if name.startswith("gemma"):
        return "gemma3_4b", remainder
    if name in {"qwen2.5"}:
        return "qwen2_5_7b", remainder
    if name in {"qwen3", "qwen", "quen"}:
        return "qwen3_4b", remainder
    if "mistral" in name:
        return "mistral3_3b", remainder
    if name in {"gpt5", "gpt-5"}:
        return "gpt5", remainder
    return "llama3_2_3b", remainder


def model_display_name(model: str) -> str:
    return {
        "gpt5": "GPT-5",
        "qwen3_4b": "Qwen3",
        "qwen2_5_7b": "Qwen2.5",
        "gemma3_4b": "Gemma",
        "mistral3_3b": "Mistral",
        "llama3_2_3b": "Llama",
    }.get(model, model)


def is_global_error_note(note: str) -> bool:
    low = note.lower()
    return any(phrase in low for phrase in [
        "all models",
        "model fails",
        "models are",
        "models failed",
        "model solutions",
    ])


def covered_models(problem_id: str) -> list[str]:
    # Llama was not manually reviewed. GPT-5/Qwen2.5 for ids 1-115 come from
    # qwen25_gpt5_failure_reasons_1_to_115.md.
    return MANUAL_MODEL_ORDER


def label_from_qwen25_gpt5_status(status: str) -> int:
    normalized = status.strip().lower()
    if normalized in {"correct", "likely_false_negative", "possible_extraction_issue"}:
        return 1
    return 0


def manual_label_from_note(model_note: str) -> tuple[int, str]:
    if not model_note:
        return 1, "correct"
    if note_says_correct(model_note):
        return 1, "correct"
    if failure_is_genuine(model_note, 0):
        return 0, "failure"
    return 1, "non_genuine"


def note_says_correct(model_note: str) -> bool:
    text = re.sub(r"\s+", " ", model_note).strip()
    text = re.sub(r"^(Gemma|Qwen3|Qwen2\.5|Qwen|Mistral|GPT-?5)\s*:\s*", "", text, flags=re.I).strip()
    normalized = text.strip(" .।*")
    if normalized in {"সঠিক", "correct", "ঠিক"}:
        return True
    low = normalized.lower()
    if any(phrase in low for phrase in [
        "no mistake",
        "label 1 ঠিক",
        "stated problem অনুযায়ী ঠিক",
        "literal question অনুযায়ী সঠিক",
        "expected answer সম্ভবত ভুল",
        "dataset mismatch",
        "সঠিক; final extraction",
        "সঠিক equation",
        "সঠিক but extra root",
    ]):
        return True
    failure_markers = [
        "কিন্তু", "ভুল", "wrong", "mistake", "failed", "failure",
        "বাদ", "নয়", "does not", "incorrect",
    ]
    if ("সঠিক" in normalized or "correct" in low) and not any(marker in low for marker in failure_markers):
        return True
    return False


def classify_error(text: str, predicted: str) -> str:
    if text:
        for category, needles in ERROR_PATTERNS:
            if contains_any(text, needles):
                return category

    if not predicted:
        return "manual_failure_note_uncategorized"

    # Prediction-only classification is intentionally conservative. Full model
    # outputs repeat broad words like "matrix", "value", "formula", and
    # "calculate", which are not reliable mistake-type signals by themselves.
    low = predicted.lower()
    if any(token in predicted for token in ["�", "Ġ", "Ċ"]):
        return "output_corruption"
    if any(phrase in low for phrase in ["cannot determine", "not enough information", "insufficient information"]):
        return "question_misinterpretation"
    if len(predicted.strip()) < 80:
        return "no_or_insufficient_reasoning"
    return "manual_failure_note_uncategorized"


def is_non_genuine_failure(model_note: str) -> bool:
    low = model_note.lower()
    if not model_note:
        return False

    if any(phrase in low for phrase in [
        "global context",
        "final expected form",
        "expected answer local/practical",
    ]):
        return False

    if any(phrase in low for phrase in [
        "false negative",
        "likely_false_negative",
        "possible_extraction_issue",
        "extraction issue",
        "extraction/form issue",
        "final extraction",
        "format issue",
        "formatting",
        "copied wrongly",
        "mainly answer mismatch",
    ]) and "false positive" not in low:
        return True

    if not contains_any(low, NON_GENUINE_HINTS):
        return False

    if any(phrase in low for phrase in [
        "wrong solution", "wrong approach", "wrong formula", "wrong method",
        "mistake in", "made mistake", "failed to", "not equivalent",
        "false positive", "\u09ad\u09c1\u09b2", "equivalent \u09a8\u09df",
        "equivalent \u09a8\u09af\u09bc",
    ]):
        return False

    return not any(phrase in low for phrase in [
        "wrong solution", "wrong approach", "wrong formula", "wrong method",
        "mistake in", "made mistake", "failed to",
    ])


def failure_is_genuine(model_note: str, label: int) -> bool:
    if label == 1:
        return False
    if is_non_genuine_failure(model_note):
        return False
    return True


def difficulty_rating(solved: int, gpt5_correct: bool, has_concept_error: bool) -> tuple[int, str]:
    # Base scale from six models: more correct solutions means easier.
    if solved >= 6:
        rating = 1
    elif solved >= 4:
        rating = 2
    elif solved >= 2:
        rating = 3
    elif solved == 1:
        rating = 4
    else:
        rating = 5

    if not gpt5_correct:
        rating = max(rating, 4)
    if has_concept_error and solved <= 3:
        rating = min(5, rating + 1)

    reason = f"{solved}/6 models solved"
    if not gpt5_correct:
        reason += "; GPT-5 failed"
    if has_concept_error:
        reason += "; conceptual/question-interpretation failure present"
    return rating, reason


def difficulty_rating_from_ratio(
    solved: int,
    total_models: int,
    gpt5_available: bool,
    gpt5_correct: bool,
    has_concept_error: bool,
) -> tuple[int, str]:
    ratio = solved / total_models if total_models else 0
    if ratio >= 1:
        rating = 1
    elif ratio >= 0.67:
        rating = 2
    elif ratio >= 0.34:
        rating = 3
    elif solved >= 1:
        rating = 4
    else:
        rating = 5

    if gpt5_available and not gpt5_correct:
        rating = max(rating, 4)
    if has_concept_error and ratio <= 0.6:
        rating = min(5, rating + 1)

    reason = f"{solved}/{total_models} covered models solved with proper reasoning"
    if gpt5_available and not gpt5_correct:
        reason += "; GPT-5 failed"
    elif not gpt5_available:
        reason += "; GPT-5 not manually available for this id"
    if has_concept_error:
        reason += "; conceptual/question-interpretation failure present"
    return rating, reason


def difficulty_rating_small_models(
    solved: int,
    total_models: int,
    small_failed_models: list[str],
    small_error_types: list[str],
) -> tuple[int, str]:
    if solved >= total_models:
        rating = 1
    elif solved == total_models - 1:
        rating = 2
    elif solved == total_models - 2:
        rating = 3
    elif solved == 1:
        rating = 4
    else:
        rating = 5

    severe_errors = {
        "question_misinterpretation",
        "formula_or_method_error",
        "dimension_or_structure_error",
        "no_or_insufficient_reasoning",
    }
    severe_present = any(error_type in severe_errors for error_type in small_error_types)

    reason = f"{solved}/{total_models} small models solved with proper reasoning"
    if small_failed_models:
        reason += f"; failed small models: {','.join(small_failed_models)}"
    if severe_present:
        reason += "; severe reasoning/interpretation failure present"
    reason += "; GPT-5 excluded from difficulty score"
    return rating, reason


def short(text: str, limit: int = 260) -> str:
    clean = re.sub(r"\s+", " ", text).strip()
    return clean if len(clean) <= limit else clean[: limit - 3] + "..."


def pct(num: int, den: int) -> str:
    return f"{(100 * num / den):.1f}%" if den else "0.0%"


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    notes = parse_notes(NOTE_PATH)
    qwen25_gpt5_notes = parse_qwen25_gpt5_notes(QWEN25_GPT5_1_TO_115_PATH)

    model_rows = {
        model: {row["id"]: row for row in read_jsonl(LABEL_DIR / filename)}
        for model, filename in MODEL_FILES.items()
    }
    ids = sorted(model_rows["gpt5"], key=lambda x: int(x))

    problem_rows = []
    detail_rows = []
    chapter_stats = defaultdict(lambda: {
        "total": 0,
        "difficulty_sum": 0,
        "rating_counts": Counter(),
        "model_correct": Counter(),
        "model_total": Counter(),
        "errors": Counter(),
        "gpt5_failures": 0,
    })

    for problem_id in ids:
        base = model_rows["gpt5"][problem_id]
        note = notes.get(problem_id, "")
        models_for_problem = covered_models(problem_id)
        judge_labels = {model: int(model_rows[model][problem_id]["labels"]) for model in MODEL_ORDER}

        categories = []
        categories_by_model = {}
        failed_models = []
        non_genuine = []
        manual_labels = {}
        for model in models_for_problem:
            row = model_rows[model][problem_id]
            model_note = note_for_model(note, model)
            manual_label, manual_status = manual_label_from_note(model_note)
            md_note = qwen25_gpt5_notes.get(problem_id, {}).get(model)
            if md_note and int(problem_id) <= 115 and model in {"gpt5", "qwen2_5_7b"}:
                manual_status = md_note["status"] or "failure"
                manual_label = label_from_qwen25_gpt5_status(manual_status)
                model_note = "" if manual_status == "correct" else f"{manual_status}: {md_note['reason']}"
            manual_labels[model] = manual_label
            category = "correct" if manual_label == 1 else classify_error(model_note, row.get("predicted_answer", ""))
            genuine = failure_is_genuine(model_note, manual_label)

            if manual_label == 0:
                failed_models.append(model)
                categories.append(category)
                categories_by_model[model] = category
            elif model_note and manual_status != "correct":
                non_genuine.append(model)

            detail_rows.append({
                "id": problem_id,
                "ChapterName": base["ChapterName"],
                "model": model,
                "manual_label": manual_label,
                "manual_status": manual_status,
                "judge_label": judge_labels[model],
                "genuine_failure": int(genuine),
                "error_type": category,
                "model_note": short(model_note, 500),
                "expected_final_answer": base.get("expected_final_answer", ""),
                "predicted_final_answer": short(row.get("predicted_final_answer", ""), 500),
            })

        has_concept_error = any(cat in {
            "question_misinterpretation",
            "formula_or_method_error",
            "dimension_or_structure_error",
        } for cat in categories)
        raw_solved = sum(manual_labels.values())
        reasoning_solved = raw_solved
        denominator = len(models_for_problem)
        difficulty_solved = sum(manual_labels[model] for model in DIFFICULTY_MODEL_ORDER)
        difficulty_failed_models = [model for model in DIFFICULTY_MODEL_ORDER if manual_labels[model] == 0]
        difficulty_error_types = [categories_by_model[model] for model in difficulty_failed_models]
        rating, reason = difficulty_rating_small_models(
            difficulty_solved,
            len(DIFFICULTY_MODEL_ORDER),
            difficulty_failed_models,
            difficulty_error_types,
        )

        problem_rows.append({
            "id": problem_id,
            "ChapterName": base["ChapterName"],
            "difficulty_1_to_5": rating,
            "difficulty_reason": reason,
            "covered_model_count": denominator,
            "difficulty_model_count": len(DIFFICULTY_MODEL_ORDER),
            "raw_solved_count": raw_solved,
            "solved_with_reasoning_count": reasoning_solved,
            "small_model_solved_count": difficulty_solved,
            "failed_count": denominator - raw_solved,
            "difficulty_failed_models": ",".join(difficulty_failed_models),
            "gpt5_manual_label": manual_labels.get("gpt5", ""),
            "qwen3_4b_manual_label": manual_labels.get("qwen3_4b", ""),
            "qwen2_5_7b_manual_label": manual_labels.get("qwen2_5_7b", ""),
            "gemma3_4b_manual_label": manual_labels.get("gemma3_4b", ""),
            "mistral3_3b_manual_label": manual_labels.get("mistral3_3b", ""),
            "gpt5_judge_label": judge_labels["gpt5"],
            "qwen3_4b_judge_label": judge_labels["qwen3_4b"],
            "qwen2_5_7b_judge_label": judge_labels["qwen2_5_7b"],
            "gemma3_4b_judge_label": judge_labels["gemma3_4b"],
            "mistral3_3b_judge_label": judge_labels["mistral3_3b"],
            "llama3_2_3b_judge_label": judge_labels["llama3_2_3b"],
            "failed_models": ",".join(failed_models),
            "non_genuine_failure_models_from_notes": ",".join(non_genuine),
            "dominant_error_types": ",".join(cat for cat, _ in Counter(categories).most_common(3)),
            "manual_note": short(note, 900),
            "expected_final_answer": base.get("expected_final_answer", ""),
        })

        chapter = base["ChapterName"]
        stats = chapter_stats[chapter]
        stats["total"] += 1
        stats["difficulty_sum"] += rating
        stats["rating_counts"][rating] += 1
        if manual_labels["gpt5"] == 0:
            stats["gpt5_failures"] += 1
        for model, label in manual_labels.items():
            stats["model_total"][model] += 1
            if label == 1:
                stats["model_correct"][model] += 1
        for cat in categories:
            stats["errors"][cat] += 1

    chapter_rows = []
    for chapter, stats in sorted(chapter_stats.items(), key=lambda kv: (-kv[1]["difficulty_sum"] / kv[1]["total"], kv[0])):
        total = stats["total"]
        top_errors = "; ".join(f"{cat}:{count}" for cat, count in stats["errors"].most_common(5))
        chapter_rows.append({
            "ChapterName": chapter,
            "problems": total,
            "avg_difficulty": round(stats["difficulty_sum"] / total, 2),
            "rating_1": stats["rating_counts"][1],
            "rating_2": stats["rating_counts"][2],
            "rating_3": stats["rating_counts"][3],
            "rating_4": stats["rating_counts"][4],
            "rating_5": stats["rating_counts"][5],
            "gpt5_failures": stats["gpt5_failures"],
            "top_error_types": top_errors,
            **{
                f"{model}_accuracy": (
                    round(stats["model_correct"][model] / stats["model_total"][model], 4)
                    if stats["model_total"][model]
                    else ""
                )
                for model in MANUAL_MODEL_ORDER
            },
        })

    chapter_model_rows = build_chapter_model_rows(detail_rows)
    write_csv(OUT_DIR / "problem_difficulty_1_to_5.csv", problem_rows)
    write_jsonl(OUT_DIR / "problem_difficulty_1_to_5.jsonl", problem_rows)
    write_csv(OUT_DIR / "problem_difficulty_1_to_4.csv", problem_rows)
    write_jsonl(OUT_DIR / "problem_difficulty_1_to_4.jsonl", problem_rows)
    write_csv(OUT_DIR / "model_mistake_details.csv", detail_rows)
    write_jsonl(OUT_DIR / "model_mistake_details.jsonl", detail_rows)
    write_csv(OUT_DIR / "chapter_mistake_difficulty_summary.csv", chapter_rows)
    write_csv(OUT_DIR / "chapter_model_mistake_summary.csv", chapter_model_rows)
    write_difficulty_outputs(problem_rows, detail_rows)
    write_report(OUT_DIR / "mistake_type_and_difficulty_report.md", problem_rows, detail_rows, chapter_rows, chapter_model_rows)


def build_chapter_model_rows(detail_rows: list[dict]) -> list[dict]:
    grouped = defaultdict(lambda: {
        "total": 0,
        "correct": 0,
        "mistakes": 0,
        "errors": Counter(),
    })
    for row in detail_rows:
        key = (row["ChapterName"], row["model"])
        grouped[key]["total"] += 1
        if int(row["manual_label"]) == 1:
            grouped[key]["correct"] += 1
        else:
            grouped[key]["mistakes"] += 1
            grouped[key]["errors"][row["error_type"]] += 1

    output = []
    for (chapter, model), stats in sorted(grouped.items(), key=lambda kv: (kv[0][0], kv[0][1])):
        total = stats["total"]
        output.append({
            "ChapterName": chapter,
            "model": model,
            "total": total,
            "correct": stats["correct"],
            "mistakes": stats["mistakes"],
            "accuracy": round(stats["correct"] / total, 4) if total else "",
            "top_error_types": "; ".join(f"{cat}:{count}" for cat, count in stats["errors"].most_common(5)),
        })
    return output


def write_difficulty_outputs(problem_rows: list[dict], detail_rows: list[dict]) -> None:
    DIFFICULTY_SPLIT_DIR.mkdir(parents=True, exist_ok=True)
    DIFFICULTY_DIR.mkdir(parents=True, exist_ok=True)

    for difficulty in range(1, 6):
        rows = [row for row in problem_rows if int(row["difficulty_1_to_5"]) == difficulty]
        write_jsonl(DIFFICULTY_SPLIT_DIR / f"difficulty_{difficulty}_problems.jsonl", rows)
        write_jsonl(DIFFICULTY_DIR / f"difficulty_{difficulty}_problems.jsonl", rows)

    problem_by_id = {row["id"]: row for row in problem_rows}
    for model in MANUAL_MODEL_ORDER:
        failed = []
        details_by_id = {
            row["id"]: row
            for row in detail_rows
            if row["model"] == model and int(row["manual_label"]) == 0
        }
        for problem_id, detail in sorted(details_by_id.items(), key=lambda kv: int(kv[0])):
            problem = problem_by_id[problem_id]
            failed.append({
                "id": problem_id,
                "ChapterName": problem["ChapterName"],
                "difficulty_1_to_5": problem["difficulty_1_to_5"],
                "small_model_solved_count": problem["small_model_solved_count"],
                "difficulty_failed_models": problem["difficulty_failed_models"],
                "model": model,
                "error_type": detail["error_type"],
                "failure_reason": detail["model_note"],
                "expected_final_answer": detail["expected_final_answer"],
                "predicted_final_answer": detail["predicted_final_answer"],
            })
        write_jsonl(DIFFICULTY_SPLIT_DIR / f"{model}_failed_problems.jsonl", failed)
        write_jsonl(DIFFICULTY_DIR / f"{model}_failed_problems.jsonl", failed)


def write_csv(path: Path, rows: list[dict]) -> None:
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_jsonl(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def write_report(
    path: Path,
    problem_rows: list[dict],
    detail_rows: list[dict],
    chapter_rows: list[dict],
    chapter_model_rows: list[dict],
) -> None:
    total = len(problem_rows)
    rating_counts = Counter(row["difficulty_1_to_5"] for row in problem_rows)
    error_counts = Counter(row["error_type"] for row in detail_rows if row["error_type"] != "correct")
    model_totals = Counter(row["model"] for row in detail_rows)
    model_correct = Counter(row["model"] for row in detail_rows if row["manual_label"] == 1)
    hard_examples = sorted(
        problem_rows,
        key=lambda r: (-r["difficulty_1_to_5"], int(r["id"])),
    )[:20]

    lines = [
        "# Mistake Type Analytics and Problem Difficulty",
        "",
        "## Method",
        "",
        "- Scope: 528 cropped problems using manual notes as the primary correctness source.",
        "- For Qwen3, Gemma, and Mistral, if a covered model is mentioned under an id, the comment is checked for whether it is a genuine math/reasoning failure. Non-genuine final-format/extraction comments count as solved.",
        "- For GPT-5 and Qwen2.5 on ids 1-115, correctness comes from `qwen25_gpt5_failure_reasons_1_to_115.md`: `correct`, `likely_false_negative`, and `possible_extraction_issue` count as solved; only `failure` counts as wrong.",
        "- Llama is excluded because it was not manually reviewed in the pasted notes.",
        "- The analysis covers GPT-5, Qwen3-4B, Qwen2.5-7B, Gemma3-4B, and Mistral3-3B.",
        "- Difficulty is rated from 1 to 5 using only the small models: Qwen3-4B, Qwen2.5-7B, Gemma3-4B, and Mistral3-3B.",
        "- GPT-5 is excluded from the difficulty score because it is a much stronger model, but GPT-5 failures are still tracked separately.",
        "- Difficulty mapping: 1 = all 4 small models solved, 2 = 3 solved, 3 = 2 solved, 4 = 1 solved, 5 = 0 solved.",
        "- Failure reasons explain why a problem is difficult: question misunderstanding, wrong method/formula, dimension/structure mistakes, no reasoning, algebra/calculation slips, and missing cases are preserved in the error fields.",
        "- Format-only/final-answer-copying notes are recorded separately and do not overstate mathematical difficulty.",
        "- Error counts are model-failure counts, not problem counts. One problem can contribute several errors if several models are listed as wrong.",
        "- Caveat: the analysis assumes each pasted-note id refers to the same problem id in the cropped label files. Any duplicated or shifted note id will affect that row.",
        "",
        "## Overall Difficulty Distribution",
        "",
        "| Difficulty | Problems | Share |",
        "|---:|---:|---:|",
    ]
    for rating in range(1, 6):
        lines.append(f"| {rating} | {rating_counts[rating]} | {pct(rating_counts[rating], total)} |")

    lines += [
        "",
        "## Model Accuracy Signal",
        "",
        "| Model | Correct | Total | Accuracy |",
        "|---|---:|---:|---:|",
    ]
    for model in MANUAL_MODEL_ORDER:
        lines.append(
            f"| {model} | {model_correct[model]} | {model_totals[model]} | {pct(model_correct[model], model_totals[model])} |"
        )

    lines += [
        "",
        "## Error Type Counts",
        "",
        "| Error type | Model-failure count |",
        "|---|---:|",
    ]
    for error_type, count in error_counts.most_common():
        lines.append(f"| {error_type} | {count} |")

    lines += [
        "",
        "## Uncategorized Notes",
        "",
        "Actually unclassified or missing-explanation failures: `0`.",
        "",
        "`manual_failure_note_uncategorized` means your note is present and is preserved as the failure explanation, but the automatic classifier did not map it to one of the narrower categories. It is not a missing explanation.",
        "",
        "Counts are per model, not per problem. One problem can contribute several model-level failure notes.",
        "",
        "## Chapter Summary",
        "",
        "| Chapter | Problems | Avg difficulty | GPT-5 failures | Top error types |",
        "|---|---:|---:|---:|---|",
    ]
    for row in chapter_rows:
        lines.append(
            f"| {row['ChapterName']} | {row['problems']} | {row['avg_difficulty']} | "
            f"{row['gpt5_failures']} | {row['top_error_types']} |"
        )

    lines += [
        "",
        "## Chapter Model Mistakes",
        "",
        "| Chapter | Model | Mistakes | Total | Accuracy | Top error types |",
        "|---|---|---:|---:|---:|---|",
    ]
    for row in sorted(chapter_model_rows, key=lambda r: (r["ChapterName"], -r["mistakes"], r["model"])):
        if row["mistakes"] == 0:
            continue
        lines.append(
            f"| {row['ChapterName']} | {row['model']} | {row['mistakes']} | {row['total']} | "
            f"{pct(row['correct'], row['total'])} | {row['top_error_types']} |"
        )

    lines += [
        "",
        "## Hardest Problem Examples",
        "",
        "| Id | Chapter | Difficulty | Small models solved | Difficulty failed models | Dominant error types | Note |",
        "|---:|---|---:|---:|---|---|---|",
    ]
    for row in hard_examples:
        note = row["manual_note"].replace("|", "\\|")
        lines.append(
            f"| {row['id']} | {row['ChapterName']} | {row['difficulty_1_to_5']} | "
            f"{row['small_model_solved_count']}/{row['difficulty_model_count']} | {row['difficulty_failed_models']} | {row['dominant_error_types']} | {note} |"
        )

    lines += [
        "",
        "## Main Failure Patterns",
        "",
        "1. Calculation errors dominate in matrix, determinant, vector, differentiation, and integration problems where one wrong sign or minor changes the final answer.",
        "2. Question-interpretation failures are concentrated in geometry/vector wording: coplanar vs perpendicular vectors, extended line segments, normal angle vs line angle, and what exactly is being asked.",
        "3. Formula/method errors appear when models choose a familiar template too early, such as using cross product for scalar quantities, direct inverse computation when a product identity is available, or the wrong angle-bisector/sign case.",
        "4. Missing cases lower correctness even when the main path is reasonable: lost negative roots, one branch of trigonometric/general solutions, or only one of multiple required answers.",
        "5. Output/format failures should be separated from genuine math failures, especially where the detailed reasoning is correct but the final extracted answer is incomplete or copied incorrectly.",
        "",
        "## Output Files",
        "",
        "- `problem_difficulty_1_to_5.csv/jsonl`: per-problem difficulty and model labels.",
        "- `problem_difficulty_1_to_4.csv/jsonl`: compatibility copy using the same 1-5 difficulty field.",
        "- `model_mistake_details.csv/jsonl`: per-model failure category, notes, and final answer excerpts.",
        "- `chapter_mistake_difficulty_summary.csv`: chapter-level difficulty and error aggregates.",
        "- `chapter_model_mistake_summary.csv`: per-chapter, per-model mistake counts and error types.",
        "- `difficulty_splits/difficulty_*.jsonl`: per-difficulty problem files using the small-model difficulty score.",
        "- `difficulty_splits/{model}_failed_problems.jsonl`: problems each reviewed model genuinely failed, including GPT-5.",
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
