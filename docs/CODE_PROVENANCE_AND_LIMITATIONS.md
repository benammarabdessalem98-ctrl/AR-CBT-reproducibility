# Code provenance and reproducibility limitations

This repository contains a retained unified Kaggle notebook for the three open-weight automated judges, together with public analysis and reconstruction scripts that reproduce the principal numerical results from the preserved judge-level integer ratings and analysis-ready tables.

The retained judge source notebooks specify greedy decoding (`do_sample=False`), a 3,000-token input limit, a 260-token output limit, and generation seed 42. They also specify evaluation-order seeds 5505 for Qwen3, 7707 for Mistral-Nemo, and 8808 for Gemma-3. These evaluation-order seeds reproduce the saved evaluation orders from the exact blinded input file, and the notebook system-prompt and item-template hashes match the preserved run records.

Recorded run metadata confirm Python 3.12.13, PyTorch 2.10.0+cu128, Transformers 5.15.1, and 4-bit NF4 execution on a Tesla T4.

However, the retained judge notebooks do not contain saved execution outputs, and the run metadata do not independently log the token limits or the generation seed. These decoding values are therefore reported as retained source configuration rather than as fully verified historical execution parameters.

What is strongly supported by retained provenance:

- exact judge repositories and pinned revisions;
- common frozen input identity and hashes;
- common judge instructions, rubric, and item schema;
- judge-specific randomized evaluation orders;
- preserved prompt and item-template hashes;
- raw and parsed output provenance;
- Qwen3 raw-output parser recovery;
- corrected metadata audit without score editing;
- corrected 432-row judge-level evaluation data;
- historical and full-precision 144-item consensus data;
- the complete frozen 24-scenario benchmark and associated public evaluation materials;
- public reconstruction and verification outputs.

The public repository excludes only private unblinding keys, credentials or secrets, personally identifiable or confidential information, and third-party restricted artifacts that cannot legally or contractually be redistributed.

## Numerical reconstruction

The final revision recomputes numerical results from the retained integer judge ratings before display rounding.

Consensus scores are reconstructed at full precision, and revised 95% confidence intervals use 10,000 nonparametric bootstrap resamples of the 24 scenario identifiers, preserving all six model × prompt conditions within each scenario. The bootstrap uses PCG64 seed `20261031`.

Rank-based analyses use the reconstructed full-precision values and explicitly account for ties. These revision settings are documented reproducibility choices and are not presented as reconstructed historical analysis settings.

The corresponding public reconstruction workflow is provided in:

`code/reproduce_results.py`

with machine-readable outputs and supporting records under:

`verification/reanalysis/`

## Tie-sensitive Model × Prompt interaction

Using the final full-precision reconstruction from the retained integer ratings, the 8-metric composite Model × Prompt interaction is:

**Friedman χ² = 2.41, p = 0.300.**

This is the value reported in the final revised manuscript.

The earlier value of approximately **χ² = 3.08, p = 0.214** arose from the historical rounded consensus export and is retained only as part of the study's provenance history. It is not the final reported interaction statistic.

The difference illustrates why the final revision reconstructs consensus values directly from the original integer judge ratings before rank-based statistical testing.

## GPT-5.6 reproducibility limitation

GPT-5.6 was collected through the ChatGPT product interface. The interface did not expose an immutable backend revision or complete decoding controls, and the archived collection records do not establish whether every response was generated in a fresh chat.

GPT-5.6 outputs are therefore treated as observed system artifacts rather than bit-for-bit reproducible generations. Fresh-chat isolation remains unverified.
