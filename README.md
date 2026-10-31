# AR-CBT++ Public Reproducibility Repository

This repository provides public research code and reproducibility artifacts for AR-CBT++, a pre-clinical benchmark for evaluating large language models in Arabic CBT-style mental-health dialogue.

AR-CBT++ combines Arabic-variety-sensitive evaluation, safety-risk stratification, structured prompting, multi-judge automated evaluation, disagreement analysis, and reproducibility auditing.

## What is included

This public repository contains research materials required to understand, inspect, and verify the AR-CBT++ benchmark analyses:

- public analysis-ready anonymized data files;

- exact open-weight model and judge revision identifiers;

- reproducibility notebooks and execution code;

- post-correction integrity and provenance audit files;

- candidate-response prompts and evaluation prompts;

- scoring rubric and evaluation schema;

- documented generation and execution settings where available;

- software environment and dependency information;

- machine-readable verification outputs.

## What is intentionally excluded

The following materials are intentionally not included in this public repository:

- private unblinding keys;

- personally identifiable or confidential information;

- credentials, API keys, access tokens, or other secrets;

- restricted or sensitive research artifacts that are not required for public reproducibility.

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

This repository supports public inspection and independent verification while minimizing unnecessary publication of safety-sensitive raw text. Public anonymized data, code, verification outputs, documentation, and audits are included; sensitive raw text and the private unblinding key remain outside the repository.


