#!/usr/bin/env python3
"""Run the Bengali math benchmark against local Hugging Face causal LMs."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path
import zipfile
from typing import Any
import xml.etree.ElementTree as ET


DEFAULT_XLSX_PATH = "/kaggle/input/eqb-math-final/eqb.xlsx"
KAGGLE_INPUT_ROOT = Path("/kaggle/input")



MODEL_ALIASES = {
    "phi4": {
        "model_id": "microsoft/Phi-4-mini-reasoning",
        "output": "/kaggle/working/phi4_local_results.jsonl",
        "chat_template_kwargs": {
            "enable_thinking": False,
        },
    },
    "numinamath": {
        "model_id": "AI-MO/NuminaMath-7B-CoT",
        "output": "/kaggle/working/numinamath_local_results.jsonl",
        "chat_template_kwargs": {
            "enable_thinking": False,
        },
    },
}

NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}

def column_index(cell_ref: str) -> int:
    letters = "".join(ch for ch in cell_ref if ch.isalpha())
    index = 0
    for ch in letters:
        index = index * 26 + ord(ch) - 64
    return index - 1


def build_prompt(question: str) -> str:
    return f"""
একটি গাণিতিক সমস্যা দেওয়া আছে। সমস্যাটি ধাপে ধাপে সমাধান করো।

প্রশ্ন:
{question}

নিম্নলিখিত ফরম্যাটে আউটপুট দাও:

DetailedAnswer:
<ধাপে ধাপে গাণিতিক সমাধান>

FinalAnswer:
<শুধু চূড়ান্ত ফলাফল>

গুরুত্বপূর্ণ:
DetailedAnswer অংশে শুধুমাত্র গাণিতিক বিশ্লেষণ থাকবে।
FinalAnswer অংশে শুধুমাত্র চূড়ান্ত ফলাফল থাকবে।
""".strip()


def read_shared_strings(zf: zipfile.ZipFile) -> list[str]:
    if "xl/sharedStrings.xml" not in zf.namelist():
        return []

    root = ET.fromstring(zf.read("xl/sharedStrings.xml"))
    return [
        "".join(text.text or "" for text in item.findall(".//m:t", NS))
        for item in root.findall("m:si", NS)
    ]


def cell_text(cell: ET.Element, shared_strings: list[str]) -> str:
    cell_type = cell.attrib.get("t")
    if cell_type == "inlineStr":
        return "".join(t.text or "" for t in cell.findall(".//m:t", NS))

    value = cell.find("m:v", NS)
    if value is None or value.text is None:
        return ""

    if cell_type == "s":
        index = int(value.text)
        return shared_strings[index] if index < len(shared_strings) else ""

    return value.text


def read_inline_xlsx(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(f"Workbook not found: {path}")

    with zipfile.ZipFile(path) as zf:
        shared_strings = read_shared_strings(zf)
        sheet = ET.fromstring(zf.read("xl/worksheets/sheet1.xml"))

    table: list[list[str | None]] = []
    for row in sheet.findall(".//m:sheetData/m:row", NS):
        values: list[str | None] = [None] * 6
        for cell in row.findall("m:c", NS):
            idx = column_index(cell.attrib["r"])
            if idx >= len(values):
                continue
            values[idx] = cell_text(cell, shared_strings)
        table.append(values)

    if not table:
        return []

    headers = [h or "" for h in table[0]]
    rows = [
        {headers[i]: row[i] or "" for i in range(len(headers))}
        for row in table[1:]
    ]
    required_columns = {"id", "Question", "FinalAnswer"}
    missing_columns = sorted(required_columns - set(headers))
    if missing_columns:
        raise ValueError(
            f"Workbook is missing required columns: {', '.join(missing_columns)}"
        )
    return rows


def resolve_xlsx_path(path: str) -> Path:
    candidate = Path(path)
    if candidate.exists():
        return candidate

    fallback = Path(DEFAULT_XLSX_PATH)
    if candidate.as_posix().startswith("/kaggle/input/") and fallback.exists():
        print(f"Workbook not found at {candidate}; using {fallback}", flush=True)
        return fallback

    return candidate


def looks_like_model_dir(path: Path) -> bool:
    return path.is_dir() and (path / "config.json").exists()


def local_model_candidates(model_id: str) -> list[Path]:
    repo_name = model_id.split("/")[-1]
    repo_slug = re.sub(r"[^a-z0-9]+", "-", repo_name.lower()).strip("-")
    full_slug = re.sub(r"[^a-z0-9]+", "-", model_id.lower()).strip("-")

    candidates: list[Path] = []
    for name in (repo_name, repo_name.lower(), repo_slug, full_slug):
        base = KAGGLE_INPUT_ROOT / name
        candidates.extend(
            [
                base,
                base / "transformers" / "default" / "1",
                base / "pytorch" / "default" / "1",
            ]
        )
    return candidates


def discover_attached_model_dir(model_id: str) -> Path | None:
    if not KAGGLE_INPUT_ROOT.exists():
        return None

    repo_name = model_id.split("/")[-1].lower()
    best_match: Path | None = None
    for config_path in KAGGLE_INPUT_ROOT.rglob("config.json"):
        model_dir = config_path.parent
        path_text = model_dir.as_posix().lower()
        if repo_name in path_text:
            return model_dir
        if best_match is None:
            try:
                config = json.loads(config_path.read_text(encoding="utf-8"))
            except Exception:
                continue
            architectures = config.get("architectures") or []
            model_type = config.get("model_type")
            if "Phi3ForCausalLM" in architectures or model_type == "phi3":
                best_match = model_dir
    return best_match


def resolve_model_source(model_id: str, model_path: str) -> str:
    if model_path:
        path = Path(model_path)
        if not looks_like_model_dir(path):
            raise FileNotFoundError(
                f"--model-path must point to a directory containing config.json: {path}"
            )
        return str(path)

    for candidate in local_model_candidates(model_id):
        if looks_like_model_dir(candidate):
            print(f"Using local model path: {candidate}", flush=True)
            return str(candidate)

    discovered = discover_attached_model_dir(model_id)
    if discovered is not None:
        print(f"Using discovered local model path: {discovered}", flush=True)
        return str(discovered)

    return model_id


def is_network_resolution_error(exc: Exception) -> bool:
    message = repr(exc)
    patterns = (
        "Temporary failure in name resolution",
        "NameResolutionError",
        "Failed to resolve",
        "getaddrinfo failed",
        "nodename nor servname provided",
    )
    return any(pattern in message for pattern in patterns)


def compact(text: str, limit: int = 220) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    return text if len(text) <= limit else text[: limit - 3] + "..."


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    records: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as f:
        for line in f:
            if line.strip():
                records.append(json.loads(line))
    return records


def eos_ids(tokenizer: Any) -> set[int]:
    ids: set[int] = set()
    value = getattr(tokenizer, "eos_token_id", None)
    if isinstance(value, int):
        ids.add(value)
    elif isinstance(value, list):
        ids.update(item for item in value if isinstance(item, int))
    for token in ("<|eot_id|>", "<|end_of_text|>", "<|im_end|>"):
        token_id = tokenizer.convert_tokens_to_ids(token)
        if isinstance(token_id, int) and token_id >= 0:
            ids.add(token_id)
    return ids


def load_model(
    model_source: str,
    dtype_name: str,
    quantization: str,
    max_memory_gb: float,
):
    os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
    os.environ.setdefault("PYTORCH_CUDA_ALLOC_CONF", "expandable_segments:True")

    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

    if not torch.cuda.is_available():
        raise RuntimeError("CUDA is not available; refusing to run because GPU was requested")

    torch.cuda.empty_cache()

    if dtype_name == "auto":
        dtype = torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16
    else:
        dtype_map = {
            "bfloat16": torch.bfloat16,
            "float16": torch.float16,
            "float32": torch.float32,
        }
        dtype = dtype_map[dtype_name]

    total_gpu_gb = torch.cuda.get_device_properties(0).total_memory / (1024**3)
    if quantization == "auto":
        quantization = "4bit" if total_gpu_gb < 24 else "none"
    if max_memory_gb <= 0:
        max_memory_gb = max(1, int(total_gpu_gb - 1.5))

    local_files_only = Path(model_source).exists()
    tokenizer = AutoTokenizer.from_pretrained(
        model_source,
        trust_remote_code=True,
        local_files_only=local_files_only,
    )
    model_kwargs = {
        "device_map": "auto",
        "max_memory": {0: f"{max_memory_gb:g}GiB", "cpu": "48GiB"},
        "low_cpu_mem_usage": True,
        "trust_remote_code": True,
        "local_files_only": local_files_only,
    }
    if quantization == "4bit":
        model_kwargs["quantization_config"] = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=dtype,
            bnb_4bit_use_double_quant=True,
        )
    elif quantization == "8bit":
        model_kwargs["quantization_config"] = BitsAndBytesConfig(load_in_8bit=True)

    try:
        model = AutoModelForCausalLM.from_pretrained(
            model_source,
            dtype=None if quantization in {"4bit", "8bit"} else dtype,
            **model_kwargs,
        )
    except TypeError:
        model = AutoModelForCausalLM.from_pretrained(
            model_source,
            torch_dtype=None if quantization in {"4bit", "8bit"} else dtype,
            **model_kwargs,
        )
    model.eval()
    return (
        tokenizer,
        model,
        torch,
        str(dtype).replace("torch.", ""),
        quantization,
        max_memory_gb,
    )


def format_input(tokenizer: Any, prompt: str, chat_template_kwargs: dict[str, Any]) -> str:
    messages = [{"role": "user", "content": prompt}]
    try:
        return tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True,
            **chat_template_kwargs,
        )
    except TypeError:
        return tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True,
        )


def generate_one(
    tokenizer: Any,
    model: Any,
    torch: Any,
    prompt: str,
    max_new_tokens: int,
    chat_template_kwargs: dict[str, Any],
    generation_kwargs: dict[str, Any],
    seed: int,
) -> tuple[str, str, dict[str, int]]:
    text = format_input(tokenizer, prompt, chat_template_kwargs)
    inputs = tokenizer(text, return_tensors="pt").to("cuda:0")
    prompt_tokens = int(inputs["input_ids"].shape[-1])
    stop_ids = eos_ids(tokenizer)

    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    with torch.inference_mode():
        generated = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            pad_token_id=tokenizer.eos_token_id,
            eos_token_id=sorted(stop_ids) if stop_ids else tokenizer.eos_token_id,
            **generation_kwargs,
        )

    output_ids = generated[0][prompt_tokens:]
    output_list = output_ids.tolist()
    finish_reason = "stop" if output_list and output_list[-1] in stop_ids else "length"
    text_out = tokenizer.decode(output_ids, skip_special_tokens=True).strip()
    usage = {
        "prompt_tokens": prompt_tokens,
        "completion_tokens": len(output_list),
        "total_tokens": prompt_tokens + len(output_list),
    }
    return text_out, finish_reason, usage


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-alias", choices=MODEL_ALIASES.keys(), default="phi4",)
    parser.add_argument("--model-id", default="")
    parser.add_argument(
        "--model-path",
        default="",
        help="Local Kaggle model directory containing config.json; avoids Hugging Face network.",
    )
    parser.add_argument("--xlsx", default=DEFAULT_XLSX_PATH)
    parser.add_argument("--output", default="")
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument(
        "--ids",
        default="",
        help="Comma-separated dataset IDs to run; applied after start/limit.",
    )
    parser.add_argument("--max-new-tokens", type=int, default=2048)
    parser.add_argument("--sleep", type=float, default=0)
    parser.add_argument("--require-stop", action="store_true")
    parser.add_argument("--retry-length-once", action="store_true")
    parser.add_argument(
        "--use-model-generation-config",
        action="store_true",
        help="Do not override decoding params; use the model repo generation_config.",
    )
    parser.add_argument(
        "--use-model-chat-template-defaults",
        action="store_true",
        help="Do not pass model-specific chat template kwargs such as enable_thinking.",
    )
    parser.add_argument("--do-sample", action="store_true")
    parser.add_argument("--temperature", type=float, default=1.0)
    parser.add_argument("--top-p", type=float, default=1.0)
    parser.add_argument("--top-k", type=int, default=0)
    parser.add_argument("--min-p", type=float, default=0.0)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument(
        "--torch-dtype",
        choices=("auto", "bfloat16", "float16", "float32"),
        default="auto",
        help="Model dtype. auto uses bfloat16 only when the GPU supports it.",
    )
    parser.add_argument(
        "--quantization",
        choices=("auto", "none", "8bit", "4bit"),
        default="auto",
        help="Quantization mode. auto uses 4bit on GPUs below 24 GB.",
    )
    parser.add_argument(
        "--max-memory-gb",
        type=float,
        default=0,
        help="GPU memory cap for model loading. 0 leaves about 1.5 GiB free.",
    )
    # args = parser.parse_args()

    args, unknown_args = parser.parse_known_args()

    if unknown_args:
        print(f"Ignoring notebook arguments: {unknown_args}")

    alias = MODEL_ALIASES[args.model_alias]
    model_id = args.model_id or alias["model_id"]
    try:
        model_source = resolve_model_source(model_id, args.model_path)
    except Exception as exc:
        print(f"Failed to resolve model path: {exc}", file=sys.stderr, flush=True)
        return 2
    output_path = Path(args.output or alias["output"])
    if args.output and (args.output.endswith(("/", "\\")) or output_path.is_dir()):
        output_path = output_path / Path(alias["output"]).name
    chat_template_kwargs = (
        {}
        if args.use_model_chat_template_defaults
        else dict(alias.get("chat_template_kwargs", {}))
    )

    done_ids = {str(record["id"]) for record in read_jsonl(output_path)}
    rows = read_inline_xlsx(resolve_xlsx_path(args.xlsx))
    if args.start:
        rows = rows[args.start :]
    if args.limit:
        rows = rows[: args.limit]
    if args.ids:
        requested_ids = {item.strip() for item in args.ids.split(",") if item.strip()}
        rows = [row for row in rows if str(row["id"]) in requested_ids]
    rows = [row for row in rows if str(row["id"]) not in done_ids]

    print(f"model={model_id}")
    if model_source != model_id:
        print(f"model_source={model_source}")
    print(f"output={output_path}")
    print(f"rows_to_run={len(rows)}")
    print(f"max_new_tokens={args.max_new_tokens}")
    print(f"torch_dtype={args.torch_dtype}")
    print(f"quantization={args.quantization}")
    print(f"max_memory_gb={args.max_memory_gb or 'auto'}")
    print("device=cuda:0")

    generation_kwargs: dict[str, Any] = {}
    if not args.use_model_generation_config:
        generation_kwargs["do_sample"] = args.do_sample
    if args.do_sample and not args.use_model_generation_config:
        generation_kwargs.update(
            {
                "temperature": args.temperature,
                "top_p": args.top_p,
                "top_k": args.top_k,
                "min_p": args.min_p,
            }
        )

    if not rows:
        print("No rows left to run.")
        return 0

    try:
        tokenizer, model, torch, torch_dtype, quantization, max_memory_gb = load_model(
            model_source,
            args.torch_dtype,
            args.quantization,
            args.max_memory_gb,
        )
    except Exception as exc:
        print(f"Failed to load model: {exc}", file=sys.stderr, flush=True)
        if model_source == model_id and is_network_resolution_error(exc):
            print(
                "Kaggle cannot resolve huggingface.co. Enable Internet in the notebook "
                "settings, or attach/download the model as a Kaggle input and run with "
                "--model-path /kaggle/input/<model-dir>/...",
                file=sys.stderr,
                flush=True,
            )
        return 2
    print(f"resolved_torch_dtype={torch_dtype}", flush=True)
    print(f"resolved_quantization={quantization}", flush=True)
    print(f"resolved_max_memory_gb={max_memory_gb:g}", flush=True)

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("a", encoding="utf-8") as out:
        for index, row in enumerate(rows, start=1):
            prompt = build_prompt(row["Question"])
            started = time.time()
            try:
                predicted, finish_reason, usage = generate_one(
                    tokenizer,
                    model,
                    torch,
                    prompt,
                    args.max_new_tokens,
                    chat_template_kwargs,
                    generation_kwargs,
                    args.seed,
                )
                if args.retry_length_once and finish_reason == "length":
                    retry_tokens = args.max_new_tokens * 2
                    print(
                        f"Retrying id={row['id']} because finish_reason=length "
                        f"with max_new_tokens={retry_tokens}",
                        flush=True,
                    )
                    predicted, finish_reason, usage = generate_one(
                        tokenizer,
                        model,
                        torch,
                        prompt,
                        retry_tokens,
                        chat_template_kwargs,
                        generation_kwargs,
                        args.seed,
                    )
                error = None
            except Exception as exc:
                predicted = ""
                finish_reason = "error"
                usage = {}
                error = repr(exc)

            record = {
                "id": row["id"],
                "model": model_id,
                "question": row["Question"],
                "expected_final_answer": row["FinalAnswer"],
                "predicted_answer": predicted,
                "finish_reason": finish_reason,
                "usage": usage,
                "runtime_seconds": round(time.time() - started, 3),
                "device": "cuda:0",
                "torch_dtype": torch_dtype,
                "quantization": quantization,
                "max_memory_gb": max_memory_gb,
                "max_new_tokens": args.max_new_tokens,
                "generation_kwargs": generation_kwargs,
                "seed": args.seed,
            }
            if error:
                record["error"] = error
            out.write(json.dumps(record, ensure_ascii=False) + "\n")
            out.flush()

            print(
                f"[{index}/{len(rows)}] id={row['id']} finish={finish_reason} "
                f"tokens={usage.get('completion_tokens')} seconds={record['runtime_seconds']} "
                f"expected={row['FinalAnswer']}",
                flush=True,
            )
            print(f"prediction: {compact(predicted)}", flush=True)

            if args.require_stop and finish_reason != "stop":
                print("Stopping because --require-stop was set.", flush=True)
                return 3
            if index < len(rows) and args.sleep:
                time.sleep(args.sleep)

    print(f"Saved results to {output_path}")
    return 0


if __name__ == "__main__":
    exit_code = main()
    if exit_code and "ipykernel" not in sys.modules:
        raise SystemExit(exit_code)
