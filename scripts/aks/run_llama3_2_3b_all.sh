#!/usr/bin/env bash
set -euo pipefail

"$(dirname "$0")/_run_aks_model.sh" \
  meta-llama/llama-3.2-3b-instruct \
  results/aks/final_model_outputs/final_llama3_2_3b_instruct_results.jsonl \
  4096
