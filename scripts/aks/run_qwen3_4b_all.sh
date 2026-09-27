#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/../.."

PYTHON=".venv-aks/bin/python"
if [[ ! -x "$PYTHON" ]]; then
  echo "Missing .venv-aks. Install with:" >&2
  echo "  python3 -m venv .venv-aks" >&2
  echo "  .venv-aks/bin/python -m pip install -r scripts/aks/requirements.txt" >&2
  exit 2
fi

if [[ -z "${HF_TOKEN:-}" ]]; then
  echo "HF_TOKEN is not set." >&2
  echo "Create a Hugging Face token with Inference Providers permission." >&2
  exit 3
fi

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Starting hosted AKS model run"
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Model: Qwen/Qwen3-4B"
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Provider: Hugging Face / Featherless AI"
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Credentials loaded"
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Model is loading: Qwen/Qwen3-4B"
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Hosted client initialization completed"
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Starting evaluation"

"$PYTHON" -u scripts/aks/huggingface_qwen3_4b.py \
  --dataset data/aks_eqb_style_merged.json \
  --output results/aks/final_model_outputs/final_qwen3_4b_results.jsonl \
  --model Qwen/Qwen3-4B \
  --provider featherless-ai \
  --max-tokens 8192 \
  --timeout 60 \
  --sleep 6 \
  --retries 5

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Hosted Qwen3-4B run completed"
