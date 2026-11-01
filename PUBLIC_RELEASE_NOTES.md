# AR-CBT++ Public Reproducibility Release

This repository provides the public reproducibility materials associated with the AR-CBT++ benchmark.

The public release includes:

- the complete frozen 24-scenario benchmark, including scenario identifiers, Arabic variety, risk stratum, theme, cultural/context marker, and synthetic user utterances;
- candidate responses for the evaluated systems and prompt conditions;
- judge-level evaluation data, including scores, critical-safety-failure flags, primary-error labels, confidence values, and retained judge rationales;
- the corrected 432-row judge-rating table and 144-item consensus data;
- model and judge revision metadata;
- reproducibility notebooks and execution code;
- candidate-response prompts and locked evaluation prompts;
- scoring rubrics, dimension-specific anchors, safety rules, output schema, and judge item template;
- integrity and provenance audit records;
- machine-readable verification outputs;
- documented generation and evaluation settings where available;
- software environment and dependency information.

The release is intended to support transparent inspection, methodological verification, independent numerical verification, and reproducibility research related to AR-CBT++.

The following materials are intentionally excluded:

- private unblinding keys;
- personally identifiable or confidential information;
- credentials, API keys, access tokens, or other secrets;
- third-party restricted artifacts that cannot legally or contractually be redistributed.

## Scope of the public release

The repository includes the complete public benchmark and the materials required to inspect and independently verify the reported AR-CBT++ analyses.

This includes the 24 frozen synthetic scenarios, synthetic user utterances, candidate responses, judge-level ratings and retained rationales, consensus data, prompts, scoring documentation, model and judge metadata, reproducibility code, verification outputs, and audit/provenance records.

Private unblinding information, credentials, personally identifiable or confidential information, and third-party restricted artifacts remain outside the public release.

## Reproducibility note

The repository documents only what is supported by preserved research artifacts and does not infer undocumented historical settings.

For the automated judges, the retained source notebooks specify greedy decoding (`do_sample=False`), a 3,000-token input limit, a 260-token output limit, generation seed 42, and evaluation-order seeds 5505 for Qwen3, 7707 for Mistral-Nemo, and 8808 for Gemma-3. The prompt hashes and evaluation-order seeds are corroborated by preserved run artifacts.

However, the retained notebooks do not contain saved execution outputs, and the run metadata do not independently log every decoding parameter. These settings are therefore reported as source configuration rather than as fully verified historical execution parameters.

GPT-5.6 was collected through the ChatGPT product interface. No immutable backend revision or complete decoding controls were exposed, and fresh-chat isolation could not be verified retrospectively. GPT-5.6 outputs are therefore treated as observed system artifacts rather than bit-for-bit reproducible generations.
