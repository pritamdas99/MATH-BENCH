#!/usr/bin/env bash
set -euo pipefail

"$(dirname "$0")/_run_aks_model.sh" \
  google/gemma-3-4b-it \
  results/aks/final_model_outputs/final_gemma3_4b_results.jsonl \
  4096
