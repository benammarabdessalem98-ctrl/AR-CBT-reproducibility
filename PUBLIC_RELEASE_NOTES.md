# Public release notes

This repository is a public reproducibility resource for the AR-CBT++ benchmark.

It is intended for researchers, developers, clinicians, auditors, and other members of the public who want to inspect the methodology, reproduce numerical analyses, regenerate figures, or examine the documented provenance and limitations of the benchmark.

## Quick start

```bash
pip install -r requirements.txt
python scripts/reproduce_results.py
python scripts/generate_figures.py
```

## Scope of the public release

The repository includes public analysis-ready numerical/categorical tables, code, model revision metadata, derived tables, figures, and audit records.

The private unblinding key, credentials, and unnecessary safety-sensitive raw text are intentionally excluded.

## Reproducibility note

The repository documents what is supported by preserved artifacts. It does not infer undocumented historical settings. In particular, the complete judge-specific decoding configuration is not fully documented for every automated judge, and GPT-5.6 was collected through a product interface without an immutable backend revision.
