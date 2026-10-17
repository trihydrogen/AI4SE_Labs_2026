# Prompt comparison

## Results

All three prompt strategies were tested on the same 155 natural-language-to-SQL
questions with `gpt-5.6-luna`.

| Prompt | Correct | Accuracy | Inference time | Average SQL execution time* |
|---|---:|---:|---:|---:|
| CRISP | 37/155 | 23.87% | 56 s | 0.036132 s |
| RISEN | 43/155 | 27.74% | 69 s | 0.053965 s |
| RTF | 37/155 | 23.87% | 63 s | 0.025045 s |

`*` Execution times are average total times over 10 measurements of all 155
queries.

![Comparison of accuracy and inference time](../Task_2/results_visualization.svg)

The accuracy difference is small in absolute terms: RISEN is six answers
better than either of the other prompts, or 3.87 percentage points. CRISP and
RTF produced the same number of correct answers. RISEN also had the longest
inference time and SQL execution time. RTF had the shortest SQL execution time,
although all three execution times are very small.

## Interpretation

RISEN gives the model the most explicit structure: a role, a task, concrete
instructions, and an expected form of response. That extra organization may
help it separate irrelevant wording from the actual database request, which
is consistent with its six additional correct queries.

CRISP and RTF were equally accurate in this experiment. Their shorter or more
compact instructions may have been sufficient for the simpler questions, but
less helpful on ambiguous questions containing distracting text. The generated
SQL was still functionally equivalent often enough to produce the same overall
score.

The model and the coding agent were not varied between these measurements, so
they are controlled factors rather than explanations for differences between
the prompts. The observed accuracy difference is consequently attributable
only to the prompt strategy within this experiment, subject to the limited
sample size. Inference time reflects model response generation, while
execution time reflects running the generated SQL and may depend on the SQL
shape and measurement noise.
