#!/usr/bin/env bash
set -euo pipefail

"$(dirname "$0")/_run_aks_model.sh" \
  qwen/qwen-2.5-7b-instruct \
  results/aks/final_model_outputs/final_qwen2_5_7b_instruct_results.jsonl \
  4096
