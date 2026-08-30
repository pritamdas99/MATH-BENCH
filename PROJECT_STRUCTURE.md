# Project Structure

This workspace contains the Bengali math benchmark dataset, model generations, reruns, and final evaluation artifacts.

## Top-Level Folders

- `data/`  
  Benchmark workbooks and dataset backups.

- `scripts/`  
  Reusable Python and shell scripts for local Hugging Face inference, OpenRouter reruns, final merging, judging, summarization, and report generation.

- `results/final_model_outputs/`  
  The four final model-generation files used for evaluation:
  - `final_gemma3_4b_results.jsonl`
  - `final_mistral3_3b_results.jsonl`
  - `final_llama3_2_3b_instruct_results.jsonl`
  - `final_qwen3_4b_results.jsonl`

- `results/research_gpt41/`  
  Paper-facing GPT-4.1 LLM-as-judge labels and summaries.
  - `labels/`: per-example `0/1` labels
  - `summaries/`: overall, per-id, and chapter-level summaries

- `results/manual_labels/` and `results/manual_summaries/`  
  Earlier manually corrected / model-assisted labels and summaries. These are kept for audit history, but the research report uses `results/research_gpt41/`.

- `runs/`  
  Intermediate model runs, reruns, smoke tests, and debugging generations.
  - `gemma/`
  - `local_hf/`
  - `mistral_openrouter/`
  - `qwen_smoke/`

- `reports/`  
  Markdown reports and project notes. The main paper-facing report is:
  - `reports/research_gpt41_evaluation_report.md`

- `notebooks/`  
  Original notebook(s), including the OpenRouter key source used by the scripts.

- `logs/` and `pids/`  
  Historical run logs and PID files.

- `tmp/`  
  Temporary test outputs.

- `cache/`  
  Python bytecode cache moved out of the top-level directory.

- `.agents/`  
  Local credential files. Do not commit or share.

## Main Report

Use this file for the final side-by-side model comparison:

```text
reports/research_gpt41_evaluation_report.md
```

## Rebuilding The GPT-4.1 Report

From the project root:

```bash
.venv/bin/python scripts/build_research_gpt41_report.py
```

## Rebuilding Final Model Outputs

From the project root:

```bash
.venv/bin/python scripts/build_final_jsonl_files.py
```

## Notes

- The project root is intentionally kept small.
- Run commands from the project root unless a script says otherwise.
- The dataset default path in maintained scripts is `data/eqb.xlsx`.
