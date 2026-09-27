#!/usr/bin/env python3
"""Run the AKS benchmark using hosted Qwen3-4B via Hugging Face."""

from __future__ import annotations

import argparse
import json
import os
import time
from pathlib import Path

from huggingface_hub import InferenceClient

from smoke_test_openrouter_qwen3b import build_prompt, compact, read_dataset


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as infile:
        return [json.loads(line) for line in infile if line.strip()]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", default="data/aks_eqb_style_merged.json")
    parser.add_argument(
        "--output",
        default="results/aks/final_model_outputs/final_qwen3_4b_results.jsonl",
    )
    parser.add_argument("--model", default="Qwen/Qwen3-4B")
    parser.add_argument("--provider", default="featherless-ai")
    parser.add_argument("--max-tokens", type=int, default=8192)
    parser.add_argument("--timeout", type=int, default=60)
    parser.add_argument("--retries", type=int, default=5)
    parser.add_argument("--sleep", type=float, default=6)
    args = parser.parse_args()

    token = (os.environ.get("HF_TOKEN") or "").strip()
    if not token:
        raise SystemExit("HF_TOKEN is not set")

    if not token.startswith("hf_"):
        raise SystemExit("HF_TOKEN has an invalid format; expected a token starting with 'hf_'")
    print("HF_TOKEN found; authentication will occur with the first request", flush=True)

    print(f"Loading dataset: {args.dataset}", flush=True)
    rows = read_dataset(Path(args.dataset))
    print(f"Dataset loaded: {len(rows)} records", flush=True)

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    existing = {str(row["id"]) for row in read_jsonl(output)}
    rows = [row for row in rows if str(row["id"]) not in existing]

    print(f"Hosted model: {args.model}", flush=True)
    print(f"Hugging Face provider: {args.provider}", flush=True)
    print(f"Already completed: {len(existing)}", flush=True)
    print(f"Rows to run: {len(rows)}", flush=True)
    print(f"Output: {output}", flush=True)
    print("Starting evaluation", flush=True)

    client = InferenceClient(
        model=args.model,
        provider=args.provider,
        token=token,
        timeout=args.timeout,
    )

    with output.open("a", encoding="utf-8") as outfile:
        for index, row in enumerate(rows, start=1):
            print(
                f"[{index}/{len(rows)}] id={row['id']} sending hosted request",
                flush=True,
            )
            started = time.time()
            for attempt in range(1, args.retries + 2):
                try:
                    response = client.chat_completion(
                        messages=[
                            {"role": "user", "content": build_prompt(row["Question"])}
                        ],
                        max_tokens=args.max_tokens,
                        temperature=0.7,
                        top_p=0.8,
                    )
                    break
                except Exception as exc:
                    print(
                        f"HF error on attempt {attempt}/{args.retries + 1}: "
                        f"{type(exc).__name__}: {exc}",
                        flush=True,
                    )
                    status_code = getattr(getattr(exc, "response", None), "status_code", None)
                    if type(exc).__name__ == "LocalProtocolError":
                        raise SystemExit(
                            "HF_TOKEN produced an invalid HTTP header. Remove embedded "
                            "newlines/whitespace and export the token again."
                        ) from exc
                    if status_code in {401, 403}:
                        raise SystemExit(
                            f"Hugging Face authorization failed with HTTP {status_code}. "
                            "Check that HF_TOKEN is valid and has Inference Providers permission."
                        ) from exc
                    if attempt > args.retries:
                        raise
                    wait = min(120, 10 * (2 ** (attempt - 1)))
                    print(f"Retrying in {wait}s", flush=True)
                    time.sleep(wait)

            choice = response.choices[0]
            predicted = choice.message.content or ""
            usage = response.usage
            record = {
                "id": row["id"],
                "model": args.model,
                "provider": args.provider,
                "question": row["Question"],
                "expected_final_answer": row["FinalAnswer"],
                "predicted_answer": predicted,
                "finish_reason": choice.finish_reason,
                "usage": dict(usage) if usage is not None else None,
                "runtime_seconds": round(time.time() - started, 3),
            }
            outfile.write(json.dumps(record, ensure_ascii=False) + "\n")
            outfile.flush()
            print(
                f"[{index}/{len(rows)}] id={row['id']} "
                f"finish={choice.finish_reason} seconds={record['runtime_seconds']}",
                flush=True,
            )
            print(f"prediction: {compact(predicted)}", flush=True)
            if index < len(rows):
                time.sleep(args.sleep)

    print(f"Completed. Results saved to {output}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
