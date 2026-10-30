# AR-CBT++ Public Reproducibility Release

This repository provides a public version of the reproducibility materials associated with the AR-CBT++ benchmark.

The public release includes:

- anonymized analysis-ready data;
- model and judge revision metadata;
- reproducibility notebooks and execution code;
- evaluation prompts and scoring documentation;
- integrity and provenance audit records;
- machine-readable verification outputs;
- software environment and dependency information.

The release is intended to support transparent inspection, methodological verification, and reproducibility research related to AR-CBT++.

The following materials are intentionally excluded:

- private unblinding keys;
- personally identifiable or confidential information;
- credentials, API keys, access tokens, or other secrets;
- restricted or sensitive artifacts that are not necessary for public reproducibility.

## Scope of the public release

The repository includes public anonymized data, code, model revision metadata, reproducibility documentation, verification outputs, and audit records.

Sensitive raw text, private unblinding information, credentials, and unnecessary restricted artifacts are intentionally excluded.

## Reproducibility note

The repository documents only what is supported by preserved research artifacts. It does not infer undocumented historical settings.

In particular, the complete judge-specific decoding configuration is not fully documented for every automated judge. GPT-5.6 was collected through a product interface without an immutable backend revision and is therefore treated as an observed system output rather than a bit-for-bit reproducible generation.
