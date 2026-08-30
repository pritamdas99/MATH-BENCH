# Mistake Type Analytics and Problem Difficulty

## Method

- Scope: 528 cropped problems using manual notes as the primary correctness source.
- For Qwen3, Gemma, and Mistral, if a covered model is mentioned under an id, the comment is checked for whether it is a genuine math/reasoning failure. Non-genuine final-format/extraction comments count as solved.
- For GPT-5 and Qwen2.5 on ids 1-115, correctness comes from `qwen25_gpt5_failure_reasons_1_to_115.md`: `correct`, `likely_false_negative`, and `possible_extraction_issue` count as solved; only `failure` counts as wrong.
- Llama is excluded because it was not manually reviewed in the pasted notes.
- The analysis covers GPT-5, Qwen3-4B, Qwen2.5-7B, Gemma3-4B, and Mistral3-3B.
- Difficulty is rated from 1 to 5 using only the small models: Qwen3-4B, Qwen2.5-7B, Gemma3-4B, and Mistral3-3B.
- GPT-5 is excluded from the difficulty score because it is a much stronger model, but GPT-5 failures are still tracked separately.
- Difficulty mapping: 1 = all 4 small models solved, 2 = 3 solved, 3 = 2 solved, 4 = 1 solved, 5 = 0 solved.
- Failure reasons explain why a problem is difficult: question misunderstanding, wrong method/formula, dimension/structure mistakes, no reasoning, algebra/calculation slips, and missing cases are preserved in the error fields.
- Format-only/final-answer-copying notes are recorded separately and do not overstate mathematical difficulty.
- Error counts are model-failure counts, not problem counts. One problem can contribute several errors if several models are listed as wrong.
- Caveat: the analysis assumes each pasted-note id refers to the same problem id in the cropped label files. Any duplicated or shifted note id will affect that row.

## Overall Difficulty Distribution

| Difficulty | Problems | Share |
|---:|---:|---:|
| 1 | 94 | 17.8% |
| 2 | 86 | 16.3% |
| 3 | 96 | 18.2% |
| 4 | 111 | 21.0% |
| 5 | 141 | 26.7% |

## Model Accuracy Signal

| Model | Correct | Total | Accuracy |
|---|---:|---:|---:|
| gpt5 | 449 | 528 | 85.0% |
| qwen3_4b | 300 | 528 | 56.8% |
| qwen2_5_7b | 204 | 528 | 38.6% |
| gemma3_4b | 203 | 528 | 38.4% |
| mistral3_3b | 230 | 528 | 43.6% |

## Error Type Counts

| Error type | Model-failure count |
|---|---:|
| arithmetic_or_algebra_error | 403 |
| question_misinterpretation | 180 |
| formula_or_method_error | 154 |
| no_or_insufficient_reasoning | 122 |
| wrong_final_value_or_expression | 120 |
| geometry_condition_error | 101 |
| format_or_final_extraction | 77 |
| missing_case_or_domain_error | 48 |
| manual_failure_note_uncategorized | 33 |
| dimension_or_structure_error | 10 |
| unit_scale_or_magnitude_error | 4 |
| output_corruption | 1 |
| same_as_referenced_model_error | 1 |

## Uncategorized Notes

Actually unclassified or missing-explanation failures: `0`.

`manual_failure_note_uncategorized` means your note is present and is preserved as the failure explanation, but the automatic classifier did not map it to one of the narrower categories. It is not a missing explanation.

Counts are per model, not per problem. One problem can contribute several model-level failure notes.

## Chapter Summary

| Chapter | Problems | Avg difficulty | GPT-5 failures | Top error types |
|---|---:|---:|---:|---|
| স্থিতিবিদ্যা | 34 | 4.47 | 9 | arithmetic_or_algebra_error:48; no_or_insufficient_reasoning:22; wrong_final_value_or_expression:17; question_misinterpretation:11; manual_failure_note_uncategorized:9 |
| গতিবিদ্যা | 38 | 4.29 | 12 | wrong_final_value_or_expression:38; arithmetic_or_algebra_error:37; no_or_insufficient_reasoning:14; manual_failure_note_uncategorized:12; formula_or_method_error:12 |
| কণিক | 37 | 4.24 | 11 | arithmetic_or_algebra_error:35; question_misinterpretation:28; formula_or_method_error:26; geometry_condition_error:14; no_or_insufficient_reasoning:10 |
| বৃত্ত | 25 | 3.6 | 6 | geometry_condition_error:48; question_misinterpretation:8; formula_or_method_error:6; arithmetic_or_algebra_error:5; no_or_insufficient_reasoning:2 |
| দ্বিপদী বিস্তৃতি | 20 | 3.55 | 1 | wrong_final_value_or_expression:21; arithmetic_or_algebra_error:17; format_or_final_extraction:8; geometry_condition_error:2; question_misinterpretation:2 |
| বিন্যাস ও সমাবেশ | 20 | 3.45 | 1 | question_misinterpretation:15; formula_or_method_error:13; arithmetic_or_algebra_error:11; missing_case_or_domain_error:5; format_or_final_extraction:3 |
| সমাকলন | 78 | 3.17 | 7 | arithmetic_or_algebra_error:71; formula_or_method_error:34; question_misinterpretation:21; format_or_final_extraction:18; no_or_insufficient_reasoning:14 |
| ত্রিকোণমিতি | 41 | 3.05 | 3 | arithmetic_or_algebra_error:30; question_misinterpretation:16; wrong_final_value_or_expression:10; no_or_insufficient_reasoning:9; missing_case_or_domain_error:8 |
| সরলরেখা | 35 | 3.03 | 5 | arithmetic_or_algebra_error:29; geometry_condition_error:16; formula_or_method_error:12; question_misinterpretation:10; no_or_insufficient_reasoning:5 |
| বহুপদী ও সমীকরণ | 22 | 3.0 | 2 | arithmetic_or_algebra_error:17; question_misinterpretation:7; no_or_insufficient_reasoning:6; formula_or_method_error:4; wrong_final_value_or_expression:3 |
| ম্যাট্রিক্স ও নির্ণায়ক | 12 | 3.0 | 0 | arithmetic_or_algebra_error:6; dimension_or_structure_error:5; no_or_insufficient_reasoning:4; question_misinterpretation:3; format_or_final_extraction:3 |
| রৈখিক প্রোগ্রামিং | 3 | 3.0 | 0 | arithmetic_or_algebra_error:3; formula_or_method_error:2; question_misinterpretation:1 |
| জটিল সংখ্যা | 19 | 2.63 | 2 | arithmetic_or_algebra_error:13; no_or_insufficient_reasoning:7; formula_or_method_error:6; missing_case_or_domain_error:3; question_misinterpretation:2 |
| ফাংশন | 10 | 2.6 | 0 | missing_case_or_domain_error:5; arithmetic_or_algebra_error:5; question_misinterpretation:3; formula_or_method_error:1; geometry_condition_error:1 |
| ভেক্টর | 18 | 2.56 | 4 | formula_or_method_error:12; arithmetic_or_algebra_error:8; question_misinterpretation:5; no_or_insufficient_reasoning:4; wrong_final_value_or_expression:3 |
| অন্তরীকরণ | 74 | 2.55 | 12 | arithmetic_or_algebra_error:56; question_misinterpretation:27; no_or_insufficient_reasoning:13; format_or_final_extraction:11; formula_or_method_error:8 |
| সম্ভাবনা | 33 | 2.45 | 3 | wrong_final_value_or_expression:15; question_misinterpretation:10; arithmetic_or_algebra_error:9; manual_failure_note_uncategorized:6; no_or_insufficient_reasoning:5 |
| বাস্তব সংখ্যা ও অসমতা | 9 | 2.22 | 1 | no_or_insufficient_reasoning:4; arithmetic_or_algebra_error:3; format_or_final_extraction:1; missing_case_or_domain_error:1; question_misinterpretation:1 |

## Chapter Model Mistakes

| Chapter | Model | Mistakes | Total | Accuracy | Top error types |
|---|---|---:|---:|---:|---|
| অন্তরীকরণ | qwen2_5_7b | 37 | 74 | 50.0% | arithmetic_or_algebra_error:20; no_or_insufficient_reasoning:7; question_misinterpretation:6; format_or_final_extraction:3; missing_case_or_domain_error:1 |
| অন্তরীকরণ | mistral3_3b | 32 | 74 | 56.8% | arithmetic_or_algebra_error:13; question_misinterpretation:9; formula_or_method_error:4; no_or_insufficient_reasoning:3; format_or_final_extraction:1 |
| অন্তরীকরণ | gemma3_4b | 29 | 74 | 60.8% | arithmetic_or_algebra_error:12; question_misinterpretation:8; geometry_condition_error:5; format_or_final_extraction:2; formula_or_method_error:1 |
| অন্তরীকরণ | qwen3_4b | 17 | 74 | 77.0% | arithmetic_or_algebra_error:10; format_or_final_extraction:2; question_misinterpretation:2; no_or_insufficient_reasoning:1; geometry_condition_error:1 |
| অন্তরীকরণ | gpt5 | 12 | 74 | 83.8% | missing_case_or_domain_error:3; format_or_final_extraction:3; question_misinterpretation:2; formula_or_method_error:2; arithmetic_or_algebra_error:1 |
| কণিক | gemma3_4b | 34 | 37 | 8.1% | arithmetic_or_algebra_error:14; question_misinterpretation:11; formula_or_method_error:5; wrong_final_value_or_expression:2; geometry_condition_error:1 |
| কণিক | mistral3_3b | 33 | 37 | 10.8% | geometry_condition_error:7; formula_or_method_error:7; arithmetic_or_algebra_error:6; no_or_insufficient_reasoning:5; question_misinterpretation:4 |
| কণিক | qwen2_5_7b | 32 | 37 | 13.5% | arithmetic_or_algebra_error:9; formula_or_method_error:6; question_misinterpretation:6; geometry_condition_error:3; wrong_final_value_or_expression:3 |
| কণিক | qwen3_4b | 21 | 37 | 43.2% | arithmetic_or_algebra_error:6; question_misinterpretation:4; geometry_condition_error:3; formula_or_method_error:3; missing_case_or_domain_error:2 |
| কণিক | gpt5 | 11 | 37 | 70.3% | formula_or_method_error:5; question_misinterpretation:3; no_or_insufficient_reasoning:2; format_or_final_extraction:1 |
| গতিবিদ্যা | gemma3_4b | 34 | 38 | 10.5% | arithmetic_or_algebra_error:10; wrong_final_value_or_expression:10; formula_or_method_error:6; no_or_insufficient_reasoning:3; manual_failure_note_uncategorized:3 |
| গতিবিদ্যা | qwen2_5_7b | 33 | 38 | 13.2% | wrong_final_value_or_expression:10; arithmetic_or_algebra_error:7; no_or_insufficient_reasoning:5; formula_or_method_error:4; manual_failure_note_uncategorized:4 |
| গতিবিদ্যা | mistral3_3b | 29 | 38 | 23.7% | arithmetic_or_algebra_error:8; wrong_final_value_or_expression:8; no_or_insufficient_reasoning:4; manual_failure_note_uncategorized:3; question_misinterpretation:3 |
| গতিবিদ্যা | qwen3_4b | 29 | 38 | 23.7% | wrong_final_value_or_expression:10; arithmetic_or_algebra_error:9; manual_failure_note_uncategorized:2; format_or_final_extraction:2; formula_or_method_error:2 |
| গতিবিদ্যা | gpt5 | 12 | 38 | 68.4% | question_misinterpretation:3; arithmetic_or_algebra_error:3; missing_case_or_domain_error:3; format_or_final_extraction:2; no_or_insufficient_reasoning:1 |
| জটিল সংখ্যা | mistral3_3b | 10 | 19 | 47.4% | arithmetic_or_algebra_error:4; no_or_insufficient_reasoning:2; geometry_condition_error:1; formula_or_method_error:1; question_misinterpretation:1 |
| জটিল সংখ্যা | gemma3_4b | 8 | 19 | 57.9% | formula_or_method_error:3; arithmetic_or_algebra_error:2; missing_case_or_domain_error:1; question_misinterpretation:1; no_or_insufficient_reasoning:1 |
| জটিল সংখ্যা | qwen2_5_7b | 7 | 19 | 63.2% | arithmetic_or_algebra_error:5; formula_or_method_error:1; no_or_insufficient_reasoning:1 |
| জটিল সংখ্যা | qwen3_4b | 6 | 19 | 68.4% | no_or_insufficient_reasoning:3; arithmetic_or_algebra_error:2; formula_or_method_error:1 |
| জটিল সংখ্যা | gpt5 | 2 | 19 | 89.5% | missing_case_or_domain_error:1; format_or_final_extraction:1 |
| ত্রিকোণমিতি | gemma3_4b | 25 | 41 | 39.0% | arithmetic_or_algebra_error:11; question_misinterpretation:5; missing_case_or_domain_error:3; wrong_final_value_or_expression:3; formula_or_method_error:1 |
| ত্রিকোণমিতি | qwen2_5_7b | 22 | 41 | 46.3% | arithmetic_or_algebra_error:7; question_misinterpretation:5; formula_or_method_error:3; wrong_final_value_or_expression:3; missing_case_or_domain_error:3 |
| ত্রিকোণমিতি | mistral3_3b | 19 | 41 | 53.7% | no_or_insufficient_reasoning:5; question_misinterpretation:4; arithmetic_or_algebra_error:3; formula_or_method_error:2; wrong_final_value_or_expression:2 |
| ত্রিকোণমিতি | qwen3_4b | 18 | 41 | 56.1% | arithmetic_or_algebra_error:8; format_or_final_extraction:4; no_or_insufficient_reasoning:3; wrong_final_value_or_expression:2; question_misinterpretation:1 |
| ত্রিকোণমিতি | gpt5 | 3 | 41 | 92.7% | question_misinterpretation:1; format_or_final_extraction:1; arithmetic_or_algebra_error:1 |
| দ্বিপদী বিস্তৃতি | gemma3_4b | 17 | 20 | 15.0% | wrong_final_value_or_expression:10; arithmetic_or_algebra_error:4; formula_or_method_error:1; geometry_condition_error:1; no_or_insufficient_reasoning:1 |
| দ্বিপদী বিস্তৃতি | qwen2_5_7b | 14 | 20 | 30.0% | wrong_final_value_or_expression:5; arithmetic_or_algebra_error:4; format_or_final_extraction:4; question_misinterpretation:1 |
| দ্বিপদী বিস্তৃতি | mistral3_3b | 12 | 20 | 40.0% | arithmetic_or_algebra_error:5; wrong_final_value_or_expression:3; format_or_final_extraction:2; geometry_condition_error:1; question_misinterpretation:1 |
| দ্বিপদী বিস্তৃতি | qwen3_4b | 8 | 20 | 60.0% | arithmetic_or_algebra_error:4; wrong_final_value_or_expression:3; format_or_final_extraction:1 |
| দ্বিপদী বিস্তৃতি | gpt5 | 1 | 20 | 95.0% | format_or_final_extraction:1 |
| ফাংশন | qwen2_5_7b | 6 | 10 | 40.0% | missing_case_or_domain_error:2; question_misinterpretation:2; geometry_condition_error:1; arithmetic_or_algebra_error:1 |
| ফাংশন | gemma3_4b | 4 | 10 | 60.0% | arithmetic_or_algebra_error:1; formula_or_method_error:1; question_misinterpretation:1; format_or_final_extraction:1 |
| ফাংশন | mistral3_3b | 3 | 10 | 70.0% | missing_case_or_domain_error:2; arithmetic_or_algebra_error:1 |
| ফাংশন | qwen3_4b | 3 | 10 | 70.0% | arithmetic_or_algebra_error:2; missing_case_or_domain_error:1 |
| বহুপদী ও সমীকরণ | qwen2_5_7b | 14 | 22 | 36.4% | arithmetic_or_algebra_error:5; formula_or_method_error:2; question_misinterpretation:2; wrong_final_value_or_expression:1; no_or_insufficient_reasoning:1 |
| বহুপদী ও সমীকরণ | gemma3_4b | 11 | 22 | 50.0% | arithmetic_or_algebra_error:5; no_or_insufficient_reasoning:2; question_misinterpretation:2; wrong_final_value_or_expression:1; manual_failure_note_uncategorized:1 |
| বহুপদী ও সমীকরণ | mistral3_3b | 11 | 22 | 50.0% | arithmetic_or_algebra_error:4; geometry_condition_error:1; manual_failure_note_uncategorized:1; question_misinterpretation:1; formula_or_method_error:1 |
| বহুপদী ও সমীকরণ | qwen3_4b | 8 | 22 | 63.6% | no_or_insufficient_reasoning:2; arithmetic_or_algebra_error:2; geometry_condition_error:1; formula_or_method_error:1; question_misinterpretation:1 |
| বহুপদী ও সমীকরণ | gpt5 | 2 | 22 | 90.9% | arithmetic_or_algebra_error:1; question_misinterpretation:1 |
| বাস্তব সংখ্যা ও অসমতা | gemma3_4b | 4 | 9 | 55.6% | no_or_insufficient_reasoning:2; wrong_final_value_or_expression:1; arithmetic_or_algebra_error:1 |
| বাস্তব সংখ্যা ও অসমতা | mistral3_3b | 3 | 9 | 66.7% | arithmetic_or_algebra_error:2; missing_case_or_domain_error:1 |
| বাস্তব সংখ্যা ও অসমতা | qwen2_5_7b | 2 | 9 | 77.8% | formula_or_method_error:1; no_or_insufficient_reasoning:1 |
| বাস্তব সংখ্যা ও অসমতা | qwen3_4b | 2 | 9 | 77.8% | format_or_final_extraction:1; no_or_insufficient_reasoning:1 |
| বাস্তব সংখ্যা ও অসমতা | gpt5 | 1 | 9 | 88.9% | question_misinterpretation:1 |
| বিন্যাস ও সমাবেশ | mistral3_3b | 16 | 20 | 20.0% | arithmetic_or_algebra_error:6; formula_or_method_error:4; question_misinterpretation:2; missing_case_or_domain_error:2; no_or_insufficient_reasoning:1 |
| বিন্যাস ও সমাবেশ | gemma3_4b | 15 | 20 | 25.0% | question_misinterpretation:9; arithmetic_or_algebra_error:4; format_or_final_extraction:1; formula_or_method_error:1 |
| বিন্যাস ও সমাবেশ | qwen3_4b | 13 | 20 | 35.0% | question_misinterpretation:4; missing_case_or_domain_error:3; formula_or_method_error:3; arithmetic_or_algebra_error:1; format_or_final_extraction:1 |
| বিন্যাস ও সমাবেশ | qwen2_5_7b | 5 | 20 | 75.0% | formula_or_method_error:4; no_or_insufficient_reasoning:1 |
| বিন্যাস ও সমাবেশ | gpt5 | 1 | 20 | 95.0% | formula_or_method_error:1 |
| বৃত্ত | gemma3_4b | 20 | 25 | 20.0% | geometry_condition_error:9; question_misinterpretation:4; formula_or_method_error:3; arithmetic_or_algebra_error:2; missing_case_or_domain_error:1 |
| বৃত্ত | qwen2_5_7b | 20 | 25 | 20.0% | geometry_condition_error:19; no_or_insufficient_reasoning:1 |
| বৃত্ত | qwen3_4b | 13 | 25 | 48.0% | geometry_condition_error:8; question_misinterpretation:3; formula_or_method_error:1; arithmetic_or_algebra_error:1 |
| বৃত্ত | mistral3_3b | 12 | 25 | 52.0% | geometry_condition_error:6; formula_or_method_error:2; arithmetic_or_algebra_error:2; format_or_final_extraction:1; question_misinterpretation:1 |
| বৃত্ত | gpt5 | 6 | 25 | 76.0% | geometry_condition_error:6 |
| ভেক্টর | qwen2_5_7b | 10 | 18 | 44.4% | formula_or_method_error:7; no_or_insufficient_reasoning:1; arithmetic_or_algebra_error:1; wrong_final_value_or_expression:1 |
| ভেক্টর | gemma3_4b | 7 | 18 | 61.1% | arithmetic_or_algebra_error:3; no_or_insufficient_reasoning:1; question_misinterpretation:1; formula_or_method_error:1; wrong_final_value_or_expression:1 |
| ভেক্টর | mistral3_3b | 6 | 18 | 66.7% | arithmetic_or_algebra_error:3; question_misinterpretation:2; no_or_insufficient_reasoning:1 |
| ভেক্টর | qwen3_4b | 5 | 18 | 72.2% | question_misinterpretation:2; no_or_insufficient_reasoning:1; arithmetic_or_algebra_error:1; wrong_final_value_or_expression:1 |
| ভেক্টর | gpt5 | 4 | 18 | 77.8% | formula_or_method_error:4 |
| ম্যাট্রিক্স ও নির্ণায়ক | qwen2_5_7b | 8 | 12 | 33.3% | dimension_or_structure_error:5; no_or_insufficient_reasoning:3 |
| ম্যাট্রিক্স ও নির্ণায়ক | mistral3_3b | 7 | 12 | 41.7% | arithmetic_or_algebra_error:3; formula_or_method_error:2; question_misinterpretation:1; format_or_final_extraction:1 |
| ম্যাট্রিক্স ও নির্ণায়ক | gemma3_4b | 5 | 12 | 58.3% | arithmetic_or_algebra_error:2; question_misinterpretation:2; format_or_final_extraction:1 |
| ম্যাট্রিক্স ও নির্ণায়ক | qwen3_4b | 4 | 12 | 66.7% | no_or_insufficient_reasoning:1; arithmetic_or_algebra_error:1; format_or_final_extraction:1; output_corruption:1 |
| রৈখিক প্রোগ্রামিং | gemma3_4b | 2 | 3 | 33.3% | question_misinterpretation:1; formula_or_method_error:1 |
| রৈখিক প্রোগ্রামিং | mistral3_3b | 2 | 3 | 33.3% | arithmetic_or_algebra_error:1; formula_or_method_error:1 |
| রৈখিক প্রোগ্রামিং | qwen2_5_7b | 1 | 3 | 66.7% | arithmetic_or_algebra_error:1 |
| রৈখিক প্রোগ্রামিং | qwen3_4b | 1 | 3 | 66.7% | arithmetic_or_algebra_error:1 |
| সমাকলন | qwen2_5_7b | 52 | 78 | 33.3% | arithmetic_or_algebra_error:21; formula_or_method_error:11; format_or_final_extraction:9; no_or_insufficient_reasoning:5; question_misinterpretation:5 |
| সমাকলন | gemma3_4b | 45 | 78 | 42.3% | arithmetic_or_algebra_error:20; formula_or_method_error:7; question_misinterpretation:7; geometry_condition_error:5; no_or_insufficient_reasoning:4 |
| সমাকলন | mistral3_3b | 43 | 78 | 44.9% | arithmetic_or_algebra_error:20; formula_or_method_error:9; question_misinterpretation:5; format_or_final_extraction:3; no_or_insufficient_reasoning:2 |
| সমাকলন | qwen3_4b | 29 | 78 | 62.8% | arithmetic_or_algebra_error:10; formula_or_method_error:7; question_misinterpretation:4; format_or_final_extraction:3; no_or_insufficient_reasoning:3 |
| সমাকলন | gpt5 | 7 | 78 | 91.0% | missing_case_or_domain_error:4; format_or_final_extraction:3 |
| সম্ভাবনা | mistral3_3b | 15 | 33 | 54.5% | wrong_final_value_or_expression:4; arithmetic_or_algebra_error:4; question_misinterpretation:3; manual_failure_note_uncategorized:2; format_or_final_extraction:1 |
| সম্ভাবনা | qwen2_5_7b | 15 | 33 | 54.5% | wrong_final_value_or_expression:7; arithmetic_or_algebra_error:3; no_or_insufficient_reasoning:2; question_misinterpretation:2; manual_failure_note_uncategorized:1 |
| সম্ভাবনা | gemma3_4b | 12 | 33 | 63.6% | wrong_final_value_or_expression:3; missing_case_or_domain_error:2; arithmetic_or_algebra_error:2; manual_failure_note_uncategorized:2; formula_or_method_error:1 |
| সম্ভাবনা | qwen3_4b | 6 | 33 | 81.8% | question_misinterpretation:3; wrong_final_value_or_expression:1; missing_case_or_domain_error:1; manual_failure_note_uncategorized:1 |
| সম্ভাবনা | gpt5 | 3 | 33 | 90.9% | question_misinterpretation:1; formula_or_method_error:1; no_or_insufficient_reasoning:1 |
| সরলরেখা | gemma3_4b | 22 | 35 | 37.1% | geometry_condition_error:8; arithmetic_or_algebra_error:5; formula_or_method_error:4; question_misinterpretation:3; format_or_final_extraction:1 |
| সরলরেখা | mistral3_3b | 17 | 35 | 51.4% | geometry_condition_error:6; arithmetic_or_algebra_error:4; formula_or_method_error:3; question_misinterpretation:2; format_or_final_extraction:1 |
| সরলরেখা | qwen2_5_7b | 16 | 35 | 54.3% | arithmetic_or_algebra_error:13; no_or_insufficient_reasoning:3 |
| সরলরেখা | qwen3_4b | 16 | 35 | 54.3% | question_misinterpretation:5; formula_or_method_error:5; arithmetic_or_algebra_error:3; geometry_condition_error:2; format_or_final_extraction:1 |
| সরলরেখা | gpt5 | 5 | 35 | 85.7% | arithmetic_or_algebra_error:4; no_or_insufficient_reasoning:1 |
| স্থিতিবিদ্যা | gemma3_4b | 31 | 34 | 8.8% | arithmetic_or_algebra_error:15; wrong_final_value_or_expression:7; question_misinterpretation:4; formula_or_method_error:2; format_or_final_extraction:1 |
| স্থিতিবিদ্যা | qwen2_5_7b | 30 | 34 | 11.8% | arithmetic_or_algebra_error:8; no_or_insufficient_reasoning:6; wrong_final_value_or_expression:5; manual_failure_note_uncategorized:4; question_misinterpretation:2 |
| স্থিতিবিদ্যা | qwen3_4b | 29 | 34 | 14.7% | arithmetic_or_algebra_error:10; question_misinterpretation:4; no_or_insufficient_reasoning:4; formula_or_method_error:3; wrong_final_value_or_expression:3 |
| স্থিতিবিদ্যা | mistral3_3b | 28 | 34 | 17.6% | arithmetic_or_algebra_error:12; no_or_insufficient_reasoning:7; format_or_final_extraction:3; wrong_final_value_or_expression:2; manual_failure_note_uncategorized:2 |
| স্থিতিবিদ্যা | gpt5 | 9 | 34 | 73.5% | no_or_insufficient_reasoning:4; arithmetic_or_algebra_error:3; format_or_final_extraction:2 |

## Hardest Problem Examples

| Id | Chapter | Difficulty | Small models solved | Difficulty failed models | Dominant error types | Note |
|---:|---|---:|---:|---|---|---|
| 1 | ম্যাট্রিক্স ও নির্ণায়ক | 5 | 0/4 | qwen3_4b,qwen2_5_7b,gemma3_4b,mistral3_3b | no_or_insufficient_reasoning,dimension_or_structure_error,arithmetic_or_algebra_error | Gemma: calculation mistake while mul;tiplying matrix. Specifically (AB)_12 Qwen: didnt even solve. Just said there is a relation between A and B. also wrote B^-1=A. Without anycalculation Mistral: solving in wrong way. Calculating B^-1 first without figuring out AB=BA. Since AB=x^2I. So B^-1 is simple from there. |
| 10 | ম্যাট্রিক্স ও নির্ণায়ক | 5 | 0/4 | qwen3_4b,qwen2_5_7b,gemma3_4b,mistral3_3b | format_or_final_extraction,dimension_or_structure_error | Model solutions are not taking n*pi-pi/6 as answers. |
| 15 | ভেক্টর | 5 | 0/4 | qwen3_4b,qwen2_5_7b,gemma3_4b,mistral3_3b | no_or_insufficient_reasoning | Gemma: তারা \(\vec a\times\vec b\) নিয়েছে, যা \(\vec a,\vec b\)-এর সমতলের লম্ব, কিন্তু প্রশ্নে চাওয়া vectorটি ওই সমতলের মধ্যেই থাকবে। Mistral: same as Gemma Qwen: didnt solve whole math. Provided a wrong answer without reasoning. May be models are not able to understand what does it mean by “\(\vec a\) ও \(\vec b\)-এর সমতলীয় মানে হলো: ভেক্টরটি \(\vec a\) এবং \(\vec b\) দিয়ে গঠিত একই plane-এর মধ্যে থাকবে। ” |
| 20 | ভেক্টর | 5 | 0/4 | qwen3_4b,qwen2_5_7b,gemma3_4b,mistral3_3b | question_misinterpretation,formula_or_method_error | Model fails to understand the question properly. Codex can understand. |
| 32 | ভেক্টর | 5 | 0/4 | qwen3_4b,qwen2_5_7b,gemma3_4b,mistral3_3b | formula_or_method_error,arithmetic_or_algebra_error,question_misinterpretation | Gemma: make mistake while calculating cross product. Wrong formula Qwen: solves cross product but question requires magnitude Mistral: wrong calculation in case of cross product |
| 37 | সরলরেখা | 5 | 0/4 | qwen3_4b,qwen2_5_7b,gemma3_4b,mistral3_3b | arithmetic_or_algebra_error,no_or_insufficient_reasoning,question_misinterpretation | Gemma: প্রদত্ত কর্ণের \(x\)-axis ও \(y\)-axis intercept-কে কর্ণের প্রান্তবিন্দু ধরে নিয়েছে। রেখার intercept কর্ণের endpoint নয়। Qwen: সে প্রদত্ত কর্ণকেই একটি বাহু/রেখা হিসেবে ধরে দিয়েছে, কিন্তু \(A(1,2)\) এই রেখাতেই নেই। তাই এটি \(A\)-গামী বাহু হতে পারে না Mistral: Mistral কর্ণের slope \(\frac34\) বের করেছে, কিন্তু বাহুর দিক নির্ণয়ে ভুল করেছে। বর্গের বাহু কর্ণের সাথে সরাসরি লম্ব নয়; বাহু কর্ণের সাথে \(45^\circ\) কোণ করে |
| 43 | সরলরেখা | 5 | 0/4 | qwen3_4b,qwen2_5_7b,gemma3_4b,mistral3_3b | formula_or_method_error,arithmetic_or_algebra_error,question_misinterpretation | Gemma: intersection ঠিক, কিন্তু wrong slope formula। Qwen: slope derivation ভুল, intersection point ব্যবহার করেনি। Mistral: slope যোগ করে bisector ধরেছে, formula ভুল। |
| 44 | সরলরেখা | 5 | 0/4 | qwen3_4b,qwen2_5_7b,gemma3_4b,mistral3_3b | question_misinterpretation,arithmetic_or_algebra_error | Gemma: \(x\)-অক্ষের সাথে দুই রেখার কোণ \(\alpha\) ও \(\frac{\pi}{2}-\alpha\) না বের করে সরাসরি অন্তর্গত কোণ \(2\alpha\) ধরে নিয়েছে; slope/angle formula ব্যবহার করেনি। Qwen: মূল ধারণা ঠিক ধরেছে: \(\theta=90^\circ-2\alpha\), কোণ দুটিও ঠিক। কিন্তু expected answer ছিল \(\tan\theta=\pm\cot2\alpha\); Qwen tangent form ও \(\pm\) case স্পষ্ট করেনি। Mistral: \(x\)-অক্ষের সাথে কোণ দুটো ঠিক বললেও অন্তর্গত কোণকে ভুলভাবে fixed \(\frac{\pi}{4}\) ধরেছে; অথচ কোণটি \(\alpha\)-এর উপর নির্ভরশীল। |
| 50 | সরলরেখা | 5 | 0/4 | qwen3_4b,qwen2_5_7b,gemma3_4b,mistral3_3b | question_misinterpretation,arithmetic_or_algebra_error,geometry_condition_error | Gemma: \((1,9)\)-কে রেখার উপর ধরে ফেলেছে, distance \(6\) condition মানেনি। Qwen: \((7,17)\) দিয়ে যাওয়ার condition মানেনি। Mistral: distance numerator \(8-6m\) না নিয়ে \(10-6m\) করেছে। |
| 56 | সরলরেখা | 5 | 0/4 | qwen3_4b,qwen2_5_7b,gemma3_4b,mistral3_3b | geometry_condition_error,arithmetic_or_algebra_error | Gemma: শুধু এক জোড়া parallel দেখে থেমেছে; দ্বিতীয় জোড়া parallel check করেনি। Qwen: parallelogram/square-কে trapezium ধরে নিয়েছে, কিন্তু expected exclusive definition ব্যবহার করেছে। Mistral: parallelogram/square-কে trapezium ধরে নিয়েছে, কিন্তু expected exclusive definition ব্যবহার করেছে। |
| 57 | সরলরেখা | 5 | 0/4 | qwen3_4b,qwen2_5_7b,gemma3_4b,mistral3_3b | arithmetic_or_algebra_error,no_or_insufficient_reasoning,missing_case_or_domain_error | Gemma: \(p\)-এর জন্য normalization factor \(2\sqrt3\) বাদ দিয়েছে। Qwen: \(\cos=\sqrt3/2,\sin=1/2\) থেকেও \(\alpha=60^\circ\) লিখেছে। Mistral: একটি branch ঠিক, কিন্তু দ্বিতীয় branch বাদ। |
| 72 | বৃত্ত | 5 | 0/4 | qwen3_4b,qwen2_5_7b,gemma3_4b,mistral3_3b | geometry_condition_error,question_misinterpretation,format_or_final_extraction | Gemma: \(C=(0,0)\) ধরেছে, কিন্তু \(AC\) ও \(BC\) তখন লম্ব হয় না। পরে circle equation-ও ভুল/অস্পষ্ট। Qwen: \(C\) কে \((c,0)\) লিখেছে, অথচ \(C\) \(y\)-অক্ষে হওয়ায় হওয়া উচিত \((0,t)\)। সেখান থেকেই solution ভেঙেছে। Mistral: final answer দেয়নি। |
| 74 | বৃত্ত | 5 | 0/4 | qwen3_4b,qwen2_5_7b,gemma3_4b,mistral3_3b | geometry_condition_error,arithmetic_or_algebra_error,formula_or_method_error | All 3 wrong Gemma/Llama: chord equation বের করেনি। Qwen: radius \(OM\)-কেই chord ধরে ফেলেছে। Mistral: midpoint line নিয়েছে, কিন্তু correct perpendicular chord নয়। |
| 76 | বৃত্ত | 5 | 0/4 | qwen3_4b,qwen2_5_7b,gemma3_4b,mistral3_3b | geometry_condition_error,question_misinterpretation,arithmetic_or_algebra_error | Gemma: circumcenter-কে centroid ধরে নিয়েছে। Qwen: perpendicular bisector midpoint দিয়ে না নিয়ে endpoint দিয়ে নিয়েছে। Mistral: center equations expand করতে arithmetic ভুল করেছে। |
| 78 | বৃত্ত | 5 | 0/4 | qwen3_4b,qwen2_5_7b,gemma3_4b,mistral3_3b | geometry_condition_error | Gemma: \(y\)-অক্ষ থেকে center-এর দূরত্ব \(\|x\|\), এটা ভুল নিয়েছে। Qwen: \(y\)-অক্ষ থেকে center-এর দূরত্ব \(\|x\|\), এটা ভুল নিয়েছে। Mistral: \(y\)-অক্ষ থেকে center-এর দূরত্ব \(\|x\|\), এটা ভুল নিয়েছে। |
| 82 | বৃত্ত | 5 | 0/4 | qwen3_4b,qwen2_5_7b,gemma3_4b,mistral3_3b | formula_or_method_error,geometry_condition_error | Gemma: সব ভুল model-ই \(y\)-অক্ষের chord length condition \(2\sqrt{k^2-16}=6\) ঠিকভাবে ব্যবহার করেনি। Qwen: সব ভুল model-ই \(y\)-অক্ষের chord length condition \(2\sqrt{k^2-16}=6\) ঠিকভাবে ব্যবহার করেনি। Mistral: সব ভুল model-ই \(y\)-অক্ষের chord length condition \(2\sqrt{k^2-16}=6\) ঠিকভাবে ব্যবহার করেনি। |
| 84 | বৃত্ত | 5 | 0/4 | qwen3_4b,qwen2_5_7b,gemma3_4b,mistral3_3b | geometry_condition_error | Gemma: tangent না বের করে axis intersection বের করেছে। Qwen: equal and opposite intercept condition \(x-y+c=0\) ব্যবহার করেনি। Mistral: equal and opposite intercept condition \(x-y+c=0\) ব্যবহার করেনি। |
| 86 | বৃত্ত | 5 | 0/4 | qwen3_4b,qwen2_5_7b,gemma3_4b,mistral3_3b | geometry_condition_error | Gemma: quadratic-এর দুই root থেকে দুইটি circle দরকার, কিন্তু একটাই দিয়েছে। Qwen: quadratic-এর দুই root থেকে দুইটি circle দরকার, কিন্তু একটাই দিয়েছে। Mistral: quadratic-এর দুই root থেকে দুইটি circle দরকার, কিন্তু একটাই দিয়েছে। |
| 90 | বৃত্ত | 5 | 0/4 | qwen3_4b,qwen2_5_7b,gemma3_4b,mistral3_3b | geometry_condition_error,question_misinterpretation | Gemma: tangent-কে diameter-এর same line ধরে নিয়েছে। Qwen: origin বৃত্তের উপর আছে বুঝতে পারেনি। Mistral: origin দিয়ে যাওয়া diameter line বের করেনি। |
| 100 | বিন্যাস ও সমাবেশ | 5 | 0/4 | qwen3_4b,qwen2_5_7b,gemma3_4b,mistral3_3b | question_misinterpretation,no_or_insufficient_reasoning | Gemma: problem-টি “কোনো দুই consonant পাশাপাশি থাকবে না” হিসেবে interpret করেছে। কিন্তু ৫ consonant ও ৩ vowel থাকলে সেটি সম্ভবই নয়। Expected অনুযায়ী শুধু সব consonant একসাথে থাকা বাদ দিতে হবে। Qwen: total \(8!\) নিয়েছে, কিন্তু repeated \(r\) এর জন্য \(2!\) দিয়ে ভাগ করেনি। আবার bad case হিসাবেও শুধু \(5!\) বাদ দিয়েছে; consonant block + vowels arrangement \(4!\) ধরেনি। তাই \(40200\) অসম্ভব, কারণ unique total arrangement-ই \(20160\)। Mistral: সংখ্যা গণনা করেনি; শুধু কয়েকটি example দিয়েছে, তাও কিছু example-এ ভুল অক্ষ আছে/গণনা নেই। |

## Main Failure Patterns

1. Calculation errors dominate in matrix, determinant, vector, differentiation, and integration problems where one wrong sign or minor changes the final answer.
2. Question-interpretation failures are concentrated in geometry/vector wording: coplanar vs perpendicular vectors, extended line segments, normal angle vs line angle, and what exactly is being asked.
3. Formula/method errors appear when models choose a familiar template too early, such as using cross product for scalar quantities, direct inverse computation when a product identity is available, or the wrong angle-bisector/sign case.
4. Missing cases lower correctness even when the main path is reasonable: lost negative roots, one branch of trigonometric/general solutions, or only one of multiple required answers.
5. Output/format failures should be separated from genuine math failures, especially where the detailed reasoning is correct but the final extracted answer is incomplete or copied incorrectly.

## Output Files

- `problem_difficulty_1_to_5.csv/jsonl`: per-problem difficulty and model labels.
- `problem_difficulty_1_to_4.csv/jsonl`: compatibility copy using the same 1-5 difficulty field.
- `model_mistake_details.csv/jsonl`: per-model failure category, notes, and final answer excerpts.
- `chapter_mistake_difficulty_summary.csv`: chapter-level difficulty and error aggregates.
- `chapter_model_mistake_summary.csv`: per-chapter, per-model mistake counts and error types.
- `difficulty_splits/difficulty_*.jsonl`: per-difficulty problem files using the small-model difficulty score.
- `difficulty_splits/{model}_failed_problems.jsonl`: problems each reviewed model genuinely failed, including GPT-5.
