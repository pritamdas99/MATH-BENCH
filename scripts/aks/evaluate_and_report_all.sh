#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/../.."

evaluate_model() {
  local result_name="$1"
  local summary_name="$2"

  python3 scripts/aks/evaluate_research_llm_judge.py \
    --results "results/aks/final_model_outputs/${result_name}.jsonl" \
    --output "results/aks/research_gpt41/labels/research_gpt41_${summary_name}_answer_labels.jsonl" \
    --limit 0 \
    --budget-usd 20

  python3 scripts/aks/summarize_manual_evaluation.py \
    --labels "results/aks/research_gpt41/labels/research_gpt41_${summary_name}_answer_labels.jsonl" \
    --dataset data/aks_eqb_style_merged.json \
    --prefix "results/aks/research_gpt41/summaries/research_gpt41_${summary_name}"
}

evaluate_model final_gemma3_4b_results gemma3_4b
evaluate_model final_llama3_2_3b_instruct_results llama3_2_3b_instruct
evaluate_model final_ministral3_3b_results ministral3_3b
evaluate_model final_qwen3_4b_results qwen3_4b
evaluate_model final_qwen2_5_7b_instruct_results qwen2_5_7b_instruct
evaluate_model final_gpt5_5_results gpt5_5

python3 scripts/aks/build_research_gpt41_report.py
