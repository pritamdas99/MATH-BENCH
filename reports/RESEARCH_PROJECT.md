# Benchmarking Small Open-Source LLMs on Bengali Higher-Secondary Mathematics

## Project Summary

This project evaluates small open-source instruction-tuned language models on a Bengali mathematics benchmark dataset. The goal is to measure how well compact LLMs can solve curriculum-style mathematical problems written in Bangla and return a structured solution with a final answer.

The benchmark focuses on models with small parameter counts, mainly models around or below 7B parameters, because these models are more practical for low-cost deployment, edge inference, classroom tools, and regional-language educational systems.

## Research Motivation

Most mathematical reasoning benchmarks are written in English. This project asks a more specific question:

> Can small open-source LLMs solve Bengali mathematical problems reliably enough to be useful for educational reasoning tasks?

This is important because Bangla math problems combine several hard requirements:

- Understanding Bengali problem statements.
- Handling mathematical notation mixed with Bangla text.
- Performing symbolic or numeric reasoning.
- Producing a step-by-step solution.
- Returning a concise final answer in a consistent format.

The project therefore tests not only mathematical reasoning, but also multilingual robustness and output discipline.

## Dataset

The main dataset file is:

```text
eqb.xlsx
```

Current dataset state:

```text
Actual rows: 528
ID range: 1 to 550
Missing IDs: 22 IDs are absent from the workbook
```

Each dataset row contains:

- `id`
- `Question`
- `FinalAnswer`
- `ChapterName`
- other workbook fields used during processing

The dataset was cleaned before benchmarking. Important cleaning steps included:

- fixing malformed or inconsistent source text,
- normalizing final-answer formatting,
- correcting chapter grouping,
- preserving backups of previous workbook states.

## Chapter Grouping Rules

Several chapters were merged to make chapter-wise evaluation more meaningful:

| Original Chapters | Final Group |
|---|---|
| ম্যাট্রিক্স, নির্ণায়ক | ম্যাট্রিক্স ও নির্ণায়ক |
| স্থানাঙ্ক জ্যামিতি, সরলরেখা | সরলরেখা |
| সীমা, অন্তরীকরণ | অন্তরীকরণ |
| দ্বিঘাত সমীকরণ, বহুপদী ও সমীকরণ | বহুপদী ও সমীকরণ |
| সূচক ও লগারিদম, জটিল সংখ্যা | জটিল সংখ্যা |
| অসমতা, সেট | বাস্তব সংখ্যা ও অসমতা |

## Prompt Format

All benchmarked models use the same prompt structure. The prompt asks the model to solve the math problem step by step and return two sections:

```text
DetailedAnswer:
<ধাপে ধাপে গাণিতিক সমাধান>

FinalAnswer:
<শুধু চূড়ান্ত ফলাফল>
```

The prompt must remain unchanged across models so that comparisons are fair. Only runtime parameters such as `max_tokens`, `timeout`, retry count, and model ID are allowed to change.

## Models Tested So Far

### Gemma 3 4B

Model:

```text
google/gemma-3-4b-it
```

Result file:

```text
gemma3_4b_all_results.jsonl
```

Status:

```text
Completed rows: 528 / 528
finish=stop: 528
```

Gemma produced a complete clean generation file with no truncation or provider-error finish states.

### Ministral 3B 2512

Model:

```text
mistralai/ministral-3b-2512
```

Main result file:

```text
ministral3_3b_all_results.jsonl
```

First-pass status:

```text
Completed rows: 528 / 528
finish=stop: 403
finish=error: 33
finish=length: 91
finish=None: 1
```

The Ministral run completed ID coverage, but many generations were not clean. The main problems were:

- over-generation until `finish=length`,
- provider/model-side `finish=error`,
- occasional malformed or incomplete final answers,
- fluent Bengali text that was sometimes mathematically unreliable.

A targeted rerun was started only for problematic records:

```text
ministral3_3b_problematic_rerun_16k.jsonl
```

Current targeted-rerun status at the time this document was written:

```text
Rerun rows completed: 46 / 125 problematic records
finish=stop: 28
finish=length: 18
```

This rerun uses the same prompt but higher generation settings:

```text
max_tokens: 16384
timeout: 600
finish=error retries: 2
```

### Meta Llama 3.2 3B Instruct

Model checked:

```text
meta-llama/llama-3.2-3b-instruct
```

Access status:

- The model is accessible through OpenRouter for a tiny probe.
- A real one-question Bengali math benchmark call failed.

Observed one-ID benchmark result:

```text
id: 1
finish_reason: error
response fragment: ধাপ
```

Conclusion: the route exists, but it is not yet stable enough for a full benchmark run under the current setup.

### Qwen Models

Checked routes:

- OpenRouter
- Requesty

Findings:

- `qwen/qwen3-4b` was not available through the checked routes.
- `qwen/qwen3-8b` appeared on OpenRouter but was rate-limited during probing.
- `deepinfra/Qwen/Qwen3.5-2B` was accessible through Requesty, but it uses reasoning tokens and needs enough output budget before normal content appears.

## Evaluation Method

The Gemma result was manually evaluated against the expected final answers.

Labeling rule:

```text
1 = correct
0 = incorrect
```

The evaluation was semantic rather than exact string matching. Equivalent mathematical forms were accepted when clearly correct, including:

- reordered roots,
- equivalent fractions or simplified expressions,
- equivalent trigonometric forms,
- equivalent matrix/vector notation,
- minor formatting differences.

The evaluation outputs are:

```text
gemma3_4b_evaluation_labels.csv
gemma3_4b_evaluation_labels.jsonl
gemma3_4b_evaluation_per_id_with_chapter.csv
gemma3_4b_evaluation_per_id_with_chapter.jsonl
gemma3_4b_chapter_accuracy.csv
gemma3_4b_chapter_accuracy.json
gemma3_4b_overall_accuracy.json
```

## Gemma 3 4B Results

Overall accuracy:

```text
Correct: 188
Incorrect: 340
Total: 528
Accuracy: 35.61%
```

Chapter-wise accuracy:

| Chapter | Correct / Total | Accuracy |
|---|---:|---:|
| রৈখিক প্রোগ্রামিং | 2 / 3 | 66.67% |
| অন্তরীকরণ | 46 / 74 | 62.16% |
| ফাংশন | 6 / 10 | 60.00% |
| সম্ভাবনা | 19 / 33 | 57.58% |
| বহুপদী ও সমীকরণ | 12 / 22 | 54.55% |
| ম্যাট্রিক্স ও নির্ণায়ক | 6 / 12 | 50.00% |
| ভেক্টর | 8 / 18 | 44.44% |
| জটিল সংখ্যা | 8 / 19 | 42.11% |
| সমাকলন | 30 / 78 | 38.46% |
| সরলরেখা | 13 / 35 | 37.14% |
| বাস্তব সংখ্যা ও অসমতা | 3 / 9 | 33.33% |
| ত্রিকোণমিতি | 13 / 41 | 31.71% |
| দ্বিপদী বিস্তৃতি | 4 / 20 | 20.00% |
| বিন্যাস ও সমাবেশ | 4 / 20 | 20.00% |
| বৃত্ত | 4 / 25 | 16.00% |
| গতিবিদ্যা | 4 / 38 | 10.53% |
| স্থিতিবিদ্যা | 3 / 34 | 8.82% |
| কণিক | 3 / 37 | 8.11% |

## Preliminary Interpretation

Gemma 3 4B is currently the cleanest completed model run. It follows the required output format reliably and generated complete responses for every dataset row. Its accuracy, however, is still modest at 35.61%, showing that Bengali mathematical reasoning remains difficult for this model size.

Ministral 3B 2512 shows stronger instability in generation. It can produce Bengali text, but it often over-generates, loops, or returns incomplete answers. This suggests that surface Bengali fluency is not enough for reliable benchmark performance.

Llama 3.2 3B Instruct is accessible through OpenRouter but failed on the real Bengali math prompt during a one-ID test. More provider testing is needed before using it in the full benchmark.

Qwen small-model access remains unresolved for the exact desired Qwen3 4B model. Qwen3 8B may be a candidate if rate limits are resolved, but it is above the stricter 7B threshold.

## Current Project Files

Important files:

```text
eqb.xlsx
gemma3_4b_all_results.jsonl
gemma3_4b_evaluation_labels.csv
gemma3_4b_evaluation_per_id_with_chapter.csv
gemma3_4b_chapter_accuracy.csv
gemma3_4b_overall_accuracy.json
ministral3_3b_all_results.jsonl
ministral3_3b_problematic_rerun_16k.jsonl
smoke_test_openrouter_qwen3b.py
rerun_ministral3_3b_problematic_16k.py
```

Sensitive files:

```text
requestly_api.txt
openrouter_reasoning_gpt_2 (2).ipynb
```

These files contain API credentials or credential-related code and should not be uploaded publicly.

## Next Steps

Recommended next research actions:

1. Finish the targeted Ministral rerun for the remaining problematic records.
2. Merge improved Ministral rerun answers into a clean final Ministral result file.
3. Evaluate Ministral using the same manual labeling protocol used for Gemma.
4. Re-test Llama 3.2 3B using a more stable provider route before launching a full run.
5. Re-check Qwen availability, especially if Qwen3 4B or a comparable <=7B instruct model becomes available.
6. Add a symbolic or semi-automatic verifier for answer types where exact checking is possible.
7. Report results by model, chapter, and error type.

## Research Question Restated

The core research question is:

> How well can small open-source instruction-tuned LLMs solve Bengali curriculum mathematics problems, and where do they fail?

The current evidence suggests that small models can produce plausible Bengali mathematical explanations, but correctness varies sharply by chapter and by model. A reliable benchmark therefore needs both answer accuracy and generation-quality tracking, including truncation, provider errors, and format compliance.
