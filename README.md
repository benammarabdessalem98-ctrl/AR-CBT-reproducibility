# AR-CBT++ Public Reproducibility Repository

This repository provides public research code and reproducibility artifacts for AR-CBT++, a pre-clinical benchmark for evaluating large language models in Arabic CBT-style mental-health dialogue.

AR-CBT++ combines Arabic-variety-sensitive evaluation, safety-risk stratification, structured prompting, multi-judge automated evaluation, disagreement analysis, and reproducibility auditing.

## What is included

This public repository contains the research materials required to understand, inspect, and independently verify the AR-CBT++ benchmark analyses:

- the complete frozen 24-scenario benchmark, including scenario identifiers, Arabic variety, risk stratum, theme, cultural/context marker, and synthetic user utterances;
- candidate responses for the evaluated systems and prompt conditions;
- judge-level evaluation data, including scores, critical-safety-failure flags, primary-error labels, confidence values, and retained judge rationales;
- public analysis-ready data files, including the corrected 432-row judge-rating table and 144-item consensus data;
- exact open-weight model and judge revision identifiers;
- candidate-response prompts and locked evaluation prompts;
- the complete scoring rubric, dimension-specific anchors, safety rules, output schema, and judge item template;
- reproducibility notebooks and execution code, including the numerical reconstruction workflow;
- post-correction integrity and provenance audit files;
- documented generation and evaluation settings where available;
- software environment and dependency information;
- machine-readable verification outputs.
## What is intentionally excluded

The following materials are intentionally not included in this public repository:

- private unblinding keys;
- personally identifiable or confidential information;
- credentials, API keys, access tokens, or other secrets;
- third-party restricted artifacts that cannot legally or contractually be redistributed.

The repository is intended solely as a public scientific reproducibility resource for AR-CBT++.
## Repository structure

- `audit/` — validation, agreement, integrity, and provenance records
- `code/` — reproducibility notebook and execution code
- `data/` — public analysis-ready anonymized data
- `docs/` — generation settings, methodology, provenance, and reproducibility limitations
- `verification/` — machine-readable verification outputs

## Important reproducibility limitations

The complete historical judge-specific decoding configuration is not fully documented for every automated judge. The retained notebook is provided for transparency and inspection, but values visible in the notebook should not be interpreted as independently proven historical runtime settings unless they are also supported by preserved run metadata. See `docs/CODE_PROVENANCE_AND_LIMITATIONS.md`.

GPT-5.6 refers to the ChatGPT product-interface label observed during data collection. No immutable backend revision or complete decoding controls were exposed, and fresh-chat isolation could not be verified retrospectively. Those outputs are therefore treated as observed artifacts rather than bit-for-bit reproducible generations.

## Public-release boundary

This repository supports public inspection and independent verification of the AR-CBT++ benchmark.

The public release includes the complete frozen 24-scenario benchmark, synthetic user utterances, candidate responses, judge-level evaluation data and retained rationales, scoring rubrics, prompts, analysis-ready datasets, reproducibility code, verification outputs, documentation, and integrity/provenance audits.

Private unblinding keys, credentials, personally identifiable or confidential information, and third-party restricted artifacts are excluded.

