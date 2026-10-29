# AR-CBT++ reproducibility map

This file maps major AR-CBT++ analyses to the corresponding public repository artifacts.

| Analysis or artifact | Repository location |
|---|---|
| 144 candidate-response consensus records | `data/AR_CBT_UNBLINDED_ITEM_CONSENSUS_144_CORRECTED_PUBLIC.csv` |
| 432 judge-item ratings | `data/AR_CBT_UNBLINDED_RATINGS_432_CORRECTED_PUBLIC.csv` |
| Three-judge item consensus | `data/AR_CBT_3_JUDGES_ITEM_CONSENSUS_144.csv` |
| Candidate and judge revisions | `MODEL_REVISIONS.md` |
| Candidate generation settings | `docs/CANDIDATE_GENERATION_SETTINGS.md` |
| Explicit-risk scenario failure breakdown | `tables/Explicit_Risk_Scenario_Failures.csv` |
| Critical-failure error categories | `tables/Critical_Failure_Error_Categories.csv` |
| Composite-definition sensitivity | `tables/Composite_Definition_Sensitivity.csv` |
| High-disagreement examples | `tables/High_Disagreement_Examples.csv` |
| Same-family sensitivity | `tables/Table_U10_Qwen_Family_Sensitivity.csv` |
| Main numerical checks | `scripts/reproduce_results.py` |
| Figure generation | `scripts/generate_figures.py` |
| Figure source data | `figure_sources/` |
| Generated figures | `figures/` |
| Integrity and provenance audits | `audit/` |
| Machine-readable result checks | `verification/main_results_check.csv` |

## Public-release boundary

The private unblinding key and unnecessary safety-sensitive raw dialogue text are not part of the public repository.
