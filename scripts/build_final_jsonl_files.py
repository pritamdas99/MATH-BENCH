#!/usr/bin/env python3
"""Build final per-model JSONL files by overlaying targeted reruns."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


FINAL_SPECS = {
    "gemma": {
        "output": "results/final_model_outputs/final_gemma3_4b_results.jsonl",
        "sources": ["runs/gemma/gemma3_4b_all_results.jsonl"],
    },
    "mistral": {
        "output": "results/final_model_outputs/final_mistral3_3b_results.jsonl",
        "sources": [
            "runs/mistral_openrouter/ministral3_3b_all_results.jsonl",
            "runs/mistral_openrouter/ministral3_3b_problematic_rerun_16k.jsonl",
            "runs/mistral_openrouter/ministral3_3b_length_rerun_32k.jsonl",
            "runs/mistral_openrouter/ministral3_3b_32k_error_retry.jsonl",
        ],
    },
    "llama": {
        "output": "results/final_model_outputs/final_llama3_2_3b_instruct_results.jsonl",
        "sources": [
            "runs/local_hf/llama3_2_3b_instruct_local_model_defaults_results.jsonl",
            "runs/local_hf/llama3_2_3b_instruct_length_rerun_8192.jsonl",
        ],
    },
    "qwen": {
        "output": "results/final_model_outputs/final_qwen3_4b_results.jsonl",
        "sources": [
            "runs/local_hf/qwen3_4b_local_model_defaults_results.jsonl",
            "runs/local_hf/qwen3_4b_length_rerun_8192.jsonl",
        ],
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


def write_jsonl(path: Path, records: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as f:
        for record in records:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")


def build_one(name: str, spec: dict[str, Any]) -> tuple[Path, int]:
    sources = [Path(item) for item in spec["sources"]]
    base_records = read_jsonl(sources[0])
    if not base_records:
        raise RuntimeError(f"{name}: base source is empty or missing: {sources[0]}")

    merged_by_id = {str(record["id"]): record for record in base_records}
    order = [str(record["id"]) for record in base_records]

    for source in sources[1:]:
        for record in read_jsonl(source):
            row_id = str(record["id"])
            if row_id in merged_by_id:
                previous = merged_by_id[row_id]
                record = dict(record)
                record.setdefault("final_replaces_finish_reason", previous.get("finish_reason"))
                record.setdefault("final_replaces_source", str(source))
                merged_by_id[row_id] = record

    final_records = [merged_by_id[row_id] for row_id in order]
    output = Path(spec["output"])
    write_jsonl(output, final_records)
    return output, len(final_records)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--models",
        default="gemma,mistral,llama,qwen",
        help="Comma-separated final specs to build.",
    )
    args = parser.parse_args()

    for name in [item.strip() for item in args.models.split(",") if item.strip()]:
        if name not in FINAL_SPECS:
            raise RuntimeError(f"Unknown final spec: {name}")
        output, count = build_one(name, FINAL_SPECS[name])
        print(f"{name}: wrote {count} records to {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
