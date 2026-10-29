# AR-CBT++ — Public Reproducibility Repository

This repository provides public, versioned code and research artifacts for **AR-CBT++**, a pre-clinical benchmark for evaluating large language models in Arabic CBT-style mental-health dialogue.

AR-CBT++ combines Arabic-variety-sensitive evaluation, safety-risk stratification, structured prompting, multi-judge automated evaluation, disagreement analysis, and reproducibility auditing.

## What is included

This public repository contains only research materials required to understand, inspect, and reproduce the AR-CBT++ benchmark analyses:

public analysis-ready aggregated and anonymized data tables;

- exact open-weight model and judge revision identifiers;

- reproducibility notebooks and execution code;

- scripts for reproducing the main statistical analyses;

- scripts for regenerating the published figures;

- derived statistical tables and sensitivity analyses;

- post-correction integrity and provenance audit files;

- candidate-response prompts and evaluation prompts;

- scoring rubric and evaluation schema;

- documented generation and execution settings where available;

- software environment and dependency information.

## What is intentionally excluded

- The following materials are intentionally not included in this public repository:

- private unblinding keys;

-personally identifiable information;

- author contact details and private correspondence;

- journal submission documents;

- cover letters and editorial correspondence;

- responses to reviewers;

- title pages containing author information;

- private human-evaluation files;

- credentials, API keys, access tokens, or other secrets;

- restricted or sensitive research artifacts not required for public reproducibility.

- The repository is intended solely as a public scientific reproducibility resource for AR-CBT++.

## Reproduce the main numerical analyses

```bash
pip install -r requirements.txt
python scripts/reproduce_results.py
```

The resulting verification table is written to:

`verification/main_results_check.csv`

## Regenerate figures

```bash
python scripts/generate_figures.py
```

The script generates `figures/Fig1_workflow.png` through `figures/Fig6_variety_core_profiles.png` and writes the corresponding source tables to `figure_sources/`.

## Repository structure

- `code/` — retained execution notebook and code excerpt
- `data/` — public analysis-ready tables
- `scripts/` — numerical reproduction and figure-generation scripts
- `tables/` — derived analytical tables
- `figures/` — generated figures
- `figure_sources/` — source data used for figures
- `audit/` — validation, agreement, integrity, and provenance records
- `docs/` — generation settings, code provenance, limitations, and citation guidance
- `verification/` — machine-readable result checks and repository validation summaries

See `REPRODUCIBILITY_MAP.md` for a direct map between major reported analyses and repository artifacts.

## Important reproducibility limitations

The complete historical judge-specific decoding configuration is not fully documented for every automated judge. The retained notebook is provided for transparency and inspection, but values visible in the notebook should not be interpreted as independently proven historical runtime settings unless they are also supported by preserved run metadata. See `docs/CODE_PROVENANCE_AND_LIMITATIONS.md`.

GPT-5.6 refers to the ChatGPT product-interface label observed during data collection. No immutable backend revision or complete decoding controls were exposed, and fresh-chat isolation could not be verified retrospectively. Those outputs are therefore treated as observed artifacts rather than bit-for-bit reproducible generations.

## Public-release boundary

This repository supports public inspection and independent numerical verification while minimizing unnecessary publication of safety-sensitive raw text. Public numerical/categorical tables, code, derived analyses, and audits are included; sensitive raw text and the private unblinding key remain outside the repository.

## Citation

Please use the citation metadata in `CITATION.cff` when citing this repository or the AR-CBT++ benchmark.
