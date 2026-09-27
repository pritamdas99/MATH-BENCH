# Research GPT-4.1 Cropped Problem Difficulty

Difficulty is assigned from the Gemma, Qwen, and Mistral cropped labels, then corrected with the attached manual explanations where a wrong label is actually a final-format or non-reasoning issue.

Rules:

- Easy: 0 or 1 genuine reasoning failure among the three target models.
- Medium: 2 genuine reasoning failures.
- Hard: 3 genuine reasoning failures.
- Explicit false positives and final-format-only misses are excluded from the genuine failure count.

## Summary

| Difficulty | Problems |
|---|---:|
| Easy | 205 |
| Medium | 106 |
| Hard | 217 |

## Genuine Failure Counts

| Genuine failures | Problems |
|---:|---:|
| 0 | 103 |
| 1 | 102 |
| 2 | 106 |
| 3 | 217 |

## Source Coverage

| Source | Problems |
|---|---:|
| manual_blank_note_plus_labels | 16 |
| manual_note_plus_labels | 71 |
| model_labels_only | 441 |

## Output Files

- `results\research_gpt41\difficulty\problem_difficulty_cropped.csv`
- `results\research_gpt41\difficulty\problem_difficulty_cropped.jsonl`
