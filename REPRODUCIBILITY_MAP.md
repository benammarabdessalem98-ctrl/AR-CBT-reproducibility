# AR-CBT++ Reproducibility Map

This file provides a concise map of the public reproducibility materials available in this repository.

| Purpose | Repository location |
|---|---|
| Complete frozen 24-scenario benchmark, including scenario metadata and synthetic user utterances | `data/` |
| Candidate responses for all evaluated systems and prompt conditions | `data/` |
| Corrected 432-row judge-level evaluation table | `data/` |
| 144-item consensus data | `data/` |
| Retained judge rationales and evaluation outputs | `data/` and/or `verification/` |
| Automated-judge execution notebook | `code/AR-CBTpp_KAGGLE_UNIFIED_3_JUDGES.ipynb` |
| Representative execution code | `code/Code_Execution_Excerpt.py` |
| Numerical reconstruction and final analysis workflow | `code/reproduce_results.py` |
| Candidate-response prompts and locked evaluation prompts | `code/` and `docs/` |
| Scoring rubric, dimension-specific anchors, safety rules, output schema, and judge item template | `code/` and `docs/` |
| Integrity and provenance audits | `audit/` |
| Machine-readable verification outputs | `verification/` |
| Full-precision reanalysis outputs and statistical verification materials | `verification/reanalysis/` |
| Model and judge revision identifiers | `MODEL_REVISIONS.md` |
| Generation settings, evaluation settings, methodology, and reproducibility limitations | `docs/` |
| Software environment and Python dependencies | `requirements.txt` |
| Public-release scope and availability notes | `PUBLIC_RELEASE_NOTES.md` |
| Licensing and reuse information | `LICENSE_NOTE.md` |

## Scope

The repository provides the public materials required to inspect and independently verify the AR-CBT++ experimental workflow, benchmark scenarios, candidate-response generation, automated evaluation process, judge disagreement analyses, critical-safety-failure counts, statistical analyses, and provenance records.

The public release includes the complete frozen 24-scenario benchmark, synthetic user utterances, candidate responses, judge-level ratings and retained rationales, consensus data, prompts, rubric documentation, analysis and reconstruction code, verification outputs, and audit/provenance records.

Private unblinding keys, credentials, personally identifiable or confidential information, and third-party restricted artifacts that cannot legally or contractually be redistributed are not included.
