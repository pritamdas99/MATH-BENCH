#!/usr/bin/env python3
"""Run the Bengali math benchmark against local Hugging Face causal LMs."""

from __future__ import annotations

import argparse
import json
import os
import re
import time
from pathlib import Path
from typing import Any

from smoke_test_openrouter_qwen3b import build_prompt, compact, read_inline_xlsx


MODEL_ALIASES = {
    "llama3_2_3b": {
        "model_id": "meta-llama/Llama-3.2-3B-Instruct",
        "output": "runs/local_hf/llama3_2_3b_instruct_local_results.jsonl",
    },
    "qwen3_4b": {
        "model_id": "Qwen/Qwen3-4B",
        "output": "runs/local_hf/qwen3_4b_local_results.jsonl",
        "chat_template_kwargs": {"enable_thinking": False},
    },
}


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


def load_model(model_id: str):
    os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")

    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer

    if not torch.cuda.is_available():
        raise RuntimeError("CUDA is not available; refusing to run because GPU was requested")

    tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        device_map={"": "cuda:0"},
        dtype=torch.bfloat16,
        low_cpu_mem_usage=True,
        trust_remote_code=True,
    )
    model.eval()
    return tokenizer, model, torch


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
    parser.add_argument("--model-alias", choices=sorted(MODEL_ALIASES), required=True)
    parser.add_argument("--model-id", default="")
    parser.add_argument("--xlsx", default="data/eqb.xlsx")
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
    args = parser.parse_args()

    alias = MODEL_ALIASES[args.model_alias]
    model_id = args.model_id or alias["model_id"]
    output_path = Path(args.output or alias["output"])
    chat_template_kwargs = (
        {}
        if args.use_model_chat_template_defaults
        else dict(alias.get("chat_template_kwargs", {}))
    )

    done_ids = {str(record["id"]) for record in read_jsonl(output_path)}
    rows = read_inline_xlsx(Path(args.xlsx))
    if args.start:
        rows = rows[args.start :]
    if args.limit:
        rows = rows[: args.limit]
    if args.ids:
        requested_ids = {item.strip() for item in args.ids.split(",") if item.strip()}
        rows = [row for row in rows if str(row["id"]) in requested_ids]
    rows = [row for row in rows if str(row["id"]) not in done_ids]

    print(f"model={model_id}")
    print(f"output={output_path}")
    print(f"rows_to_run={len(rows)}")
    print(f"max_new_tokens={args.max_new_tokens}")
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

    tokenizer, model, torch = load_model(model_id)
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
                "torch_dtype": "bfloat16",
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
    raise SystemExit(main())
