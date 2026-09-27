#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

"$SCRIPT_DIR/run_gemma3_4b_all.sh"
"$SCRIPT_DIR/run_llama3_2_3b_all.sh"
"$SCRIPT_DIR/run_ministral3_3b_all.sh"
"$SCRIPT_DIR/run_qwen3_4b_all.sh"
"$SCRIPT_DIR/run_qwen2_5_7b_all.sh"
"$SCRIPT_DIR/run_qwen3_8_27b_all.sh"
"$SCRIPT_DIR/run_gpt5_5_all.sh"
