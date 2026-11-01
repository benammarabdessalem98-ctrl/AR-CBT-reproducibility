#!/usr/bin/env python3
"""
AR-CBT++ final numerical reconstruction.

Input:
  data/AR_CBT_UNBLINDED_RATINGS_432_CORRECTED_PUBLIC.csv

Outputs:
  verification/reanalysis/consensus_full_precision_144.csv
  verification/reanalysis/model_prompt_summary.csv
  verification/reanalysis/risk_summary.csv
  verification/reanalysis/main_statistical_tests.csv
  verification/reanalysis/reanalysis_summary.json

The script reconstructs item-level consensus directly from the retained
integer judge ratings before display rounding.
"""

from pathlib import Path
import json
import math
import itertools
import numpy as np
import pandas as pd
from scipy.stats import friedmanchisquare, kruskal

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "AR_CBT_UNBLINDED_RATINGS_432_CORRECTED_PUBLIC.csv"
OUTDIR = ROOT / "verification" / "reanalysis"
OUTDIR.mkdir(parents=True, exist_ok=True)

SCORE_COLS = [
    "CBT_fidelity_0_4",
    "dialect_meaning_preservation_0_4",
    "dialect_pragmatic_interpretation_0_4",
    "register_appropriateness_0_4",
    "codeswitch_handling_0_4",
    "cultural_adaptation_0_4",
    "empathy_alliance_0_4",
    "safety_0_4",
]

META_COLS = [
    "judge_item_id",
    "candidate_model",
    "scenario_id",
    "arabic_variety",
    "risk",
    "theme",
    "prompt_condition",
]

def require_columns(df, cols):
    missing = [c for c in cols if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

def rank_abs_average(values):
    """Average ranks for absolute non-zero values."""
    s = pd.Series(np.abs(values), dtype=float)
    return s.rank(method="average").to_numpy()

def exact_signed_rank_pvalue(diffs):
    """
    Exact conditional two-sided signed-rank p-value by enumerating sign assignments.
    Zeros are discarded. Tied absolute differences receive average ranks.
    """
    d = np.asarray(diffs, dtype=float)
    d = d[np.isfinite(d)]
    d = d[d != 0]
    n = len(d)
    if n == 0:
        return 1.0, 0.0, 0
    ranks = rank_abs_average(d)
    obs = float(np.sum(ranks[d > 0]))
    total = float(np.sum(ranks))
    # two-sided statistic around total/2
    obs_dev = abs(obs - total / 2.0)
    if n > 24:
        raise ValueError("Exact sign enumeration intended for n <= 24.")
    extreme = 0
    total_perm = 2 ** n
    for bits in itertools.product([0, 1], repeat=n):
        wplus = sum(r for r, b in zip(ranks, bits) if b)
        if abs(wplus - total / 2.0) >= obs_dev - 1e-12:
            extreme += 1
    p = extreme / total_perm
    return p, obs, n

def bootstrap_ci_scenario_block(df_item, value_col="composite", n_boot=10000, seed=20261031):
    """
    Percentile CI by resampling the 24 scenario identifiers, keeping all
    model x prompt conditions for each sampled scenario.
    """
    rng = np.random.Generator(np.random.PCG64(seed))
    scenarios = np.array(sorted(df_item["scenario_id"].unique()))
    if len(scenarios) != 24:
        raise ValueError(f"Expected 24 scenarios, found {len(scenarios)}")
    vals = []
    grouped = {sid: df_item.loc[df_item["scenario_id"] == sid, value_col].to_numpy(float)
               for sid in scenarios}
    for _ in range(n_boot):
        draw = rng.choice(scenarios, size=len(scenarios), replace=True)
        pooled = np.concatenate([grouped[s] for s in draw])
        vals.append(float(np.mean(pooled)))
    lo, hi = np.percentile(vals, [2.5, 97.5], method="linear")
    return float(lo), float(hi)

def majority_binary(x):
    a = np.asarray(x, dtype=int)
    return int(np.sum(a == 1) >= 2)

# ---------------------------------------------------------------------
# Load and validate
# ---------------------------------------------------------------------
df = pd.read_csv(INPUT)
require_columns(df, META_COLS + SCORE_COLS + ["judge_short_name", "critical_safety_failure_0_1"])

if len(df) != 432:
    raise ValueError(f"Expected 432 judge rows, found {len(df)}")
if df["judge_item_id"].nunique() != 144:
    raise ValueError(f"Expected 144 judge items, found {df['judge_item_id'].nunique()}")

counts = df.groupby("judge_item_id")["judge_short_name"].nunique()
if not (counts == 3).all():
    raise ValueError("Every judge_item_id must have exactly 3 distinct judges.")

# ---------------------------------------------------------------------
# Reconstruct full-precision item consensus from integer judge scores
# ---------------------------------------------------------------------
agg = {c: "first" for c in META_COLS[1:]}
for c in SCORE_COLS:
    agg[c] = "mean"
agg["critical_safety_failure_0_1"] = majority_binary

item = df.groupby("judge_item_id", as_index=False).agg(agg)

# Exact integer numerator for the 8-metric composite:
# 3 judges x 8 integer dimensions = denominator 24.
# Keeping this numerator as an integer preserves mathematically exact ties
# in rank-based analyses and avoids floating-point tie breaking.
item_score_sums = (
    df.assign(_score_sum=df[SCORE_COLS].sum(axis=1))
      .groupby("judge_item_id")["_score_sum"]
      .sum()
      .astype(int)
)
item["composite_numerator_24"] = item["judge_item_id"].map(item_score_sums).astype(int)
item["composite"] = item["composite_numerator_24"] / 24.0

item["linguistic_core"] = item[
    [
        "dialect_meaning_preservation_0_4",
        "dialect_pragmatic_interpretation_0_4",
        "register_appropriateness_0_4",
        "codeswitch_handling_0_4",
    ]
].mean(axis=1)
item["therapeutic_safety_core"] = item[
    [
        "CBT_fidelity_0_4",
        "cultural_adaptation_0_4",
        "empathy_alliance_0_4",
        "safety_0_4",
    ]
].mean(axis=1)

item.to_csv(OUTDIR / "consensus_full_precision_144.csv", index=False)

# ---------------------------------------------------------------------
# Model x prompt summaries
# ---------------------------------------------------------------------
summary_rows = []
for (model, prompt), g in item.groupby(["candidate_model", "prompt_condition"], sort=True):
    lo, hi = bootstrap_ci_scenario_block(g, "composite", n_boot=10000, seed=20261031)
    summary_rows.append({
        "candidate_model": model,
        "prompt_condition": prompt,
        "n": len(g),
        "composite_mean": g["composite"].mean(),
        "composite_ci95_lo": lo,
        "composite_ci95_hi": hi,
        "CBT_fidelity_mean": g["CBT_fidelity_0_4"].mean(),
        "empathy_alliance_mean": g["empathy_alliance_0_4"].mean(),
        "safety_mean": g["safety_0_4"].mean(),
        "majority_critical_failures": int(g["critical_safety_failure_0_1"].sum()),
    })
model_prompt = pd.DataFrame(summary_rows)
model_prompt.to_csv(OUTDIR / "model_prompt_summary.csv", index=False)

# ---------------------------------------------------------------------
# Scenario-blocked primary tests
# ---------------------------------------------------------------------
# IMPORTANT:
# Rank-based primary tests use integer numerators with common denominators.
# This preserves exact mathematical ties and prevents floating-point noise
# from turning an exact tie into a tiny artificial difference.

# 1) Model main effect:
# each scenario/model averages the two prompt-condition item composites.
# Since each item composite has denominator 24, the prompt-averaged
# scenario/model score has common denominator 48. The integer numerator
# is simply the sum of the two item numerators.
sc_model_num = (
    item.groupby(["scenario_id", "candidate_model"], as_index=False)["composite_numerator_24"]
        .sum()
        .pivot(index="scenario_id", columns="candidate_model", values="composite_numerator_24")
)

models = list(sc_model_num.columns)
if len(models) != 3:
    raise ValueError(f"Expected 3 candidate models, found {models}")
model_stat, model_p = friedmanchisquare(
    *(sc_model_num[m].to_numpy(dtype=int) for m in models)
)

# Floating-point display version only (not used for rank testing)
sc_model = sc_model_num / 48.0

# 2) Prompt main effect:
# each scenario/prompt averages across the three models.
# Common denominator = 24 x 3 = 72; numerator is the integer sum.
sc_prompt_num = (
    item.groupby(["scenario_id", "prompt_condition"], as_index=False)["composite_numerator_24"]
        .sum()
        .pivot(index="scenario_id", columns="prompt_condition", values="composite_numerator_24")
)
prompt_names = list(sc_prompt_num.columns)
if len(prompt_names) != 2:
    raise ValueError(f"Expected 2 prompt conditions, found {prompt_names}")

minimal = next((x for x in prompt_names if "minimal" in x.lower()), prompt_names[0])
cbt = next((x for x in prompt_names if "cbt" in x.lower()), prompt_names[1])

# Exact integer paired differences; denominator 72 is common and irrelevant to ranks.
prompt_diff_num = (
    sc_prompt_num[cbt].to_numpy(dtype=int)
    - sc_prompt_num[minimal].to_numpy(dtype=int)
)
prompt_p, prompt_wplus, prompt_n = exact_signed_rank_pvalue(prompt_diff_num)
prompt_diffs = prompt_diff_num / 72.0

# 3) Model x Prompt interaction:
# for each scenario/model, the prompt delta is the difference between
# two integer item numerators (common denominator 24).
delta_num = (
    item.pivot_table(
        index=["scenario_id", "candidate_model"],
        columns="prompt_condition",
        values="composite_numerator_24",
        aggfunc="first"
    )
    .reset_index()
)
delta_num["prompt_delta_num"] = (
    delta_num[cbt].astype(int) - delta_num[minimal].astype(int)
)
delta_wide_num = delta_num.pivot(
    index="scenario_id",
    columns="candidate_model",
    values="prompt_delta_num"
)
inter_stat, inter_p = friedmanchisquare(
    *(delta_wide_num[m].to_numpy(dtype=int) for m in models)
)

# Floating display version
delta_wide = delta_wide_num / 24.0

tests = pd.DataFrame([
    {
        "test": "Model main effect on 8-metric composite",
        "statistic": model_stat,
        "p_value": model_p,
        "effect_or_delta": np.nan,
        "n_blocks": len(sc_model),
    },
    {
        "test": "Prompt main effect on 8-metric composite",
        "statistic": prompt_wplus,
        "p_value": prompt_p,
        "effect_or_delta": float(np.mean(prompt_diffs)),
        "n_blocks": prompt_n,
    },
    {
        "test": "Model x Prompt interaction on 8-metric composite",
        "statistic": inter_stat,
        "p_value": inter_p,
        "effect_or_delta": np.nan,
        "n_blocks": len(delta_wide_num),
    },
])
tests.to_csv(OUTDIR / "main_statistical_tests.csv", index=False)

# ---------------------------------------------------------------------
# Risk summaries and scenario-level critical failures
# ---------------------------------------------------------------------
risk_order = ["low", "moderate", "implicit", "explicit"]
risk_rows = []
for risk, g in item.groupby("risk"):
    sc = g.groupby("scenario_id", as_index=False).agg(
        composite=("composite", "mean"),
        safety=("safety_0_4", "mean"),
    )
    risk_rows.append({
        "risk": risk,
        "scenario_count": sc["scenario_id"].nunique(),
        "response_count": len(g),
        "composite_scenario_mean": sc["composite"].mean(),
        "safety_scenario_mean": sc["safety"].mean(),
        "majority_critical_failures": int(g["critical_safety_failure_0_1"].sum()),
    })

risk_summary = pd.DataFrame(risk_rows)
risk_summary["risk"] = pd.Categorical(risk_summary["risk"], categories=risk_order, ordered=True)
risk_summary = risk_summary.sort_values("risk")
risk_summary.to_csv(OUTDIR / "risk_summary.csv", index=False)

explicit = item[item["risk"].astype(str).str.lower() == "explicit"]
explicit_breakdown = (
    explicit.groupby(["scenario_id", "arabic_variety"], as_index=False)
            .agg(
                responses=("judge_item_id", "count"),
                majority_critical_failures=("critical_safety_failure_0_1", "sum")
            )
)
explicit_breakdown.to_csv(OUTDIR / "explicit_risk_failure_breakdown.csv", index=False)

# ---------------------------------------------------------------------
# Simple judge agreement diagnostics
# ---------------------------------------------------------------------
agreement_rows = []
for score in SCORE_COLS:
    pvt = df.pivot(index="judge_item_id", columns="judge_short_name", values=score)
    arr = pvt.to_numpy(float)
    exact = np.mean(np.ptp(arr, axis=1) == 0)
    within1 = np.mean(np.ptp(arr, axis=1) <= 1)
    agreement_rows.append({
        "dimension": score,
        "all_3_exact_agreement": exact,
        "all_3_within_1_agreement": within1,
    })
pd.DataFrame(agreement_rows).to_csv(OUTDIR / "judge_agreement_simple.csv", index=False)

# ---------------------------------------------------------------------
# Summary JSON with manuscript checkpoints
# ---------------------------------------------------------------------
summary = {
    "input_file": str(INPUT.relative_to(ROOT)),
    "judge_rows": int(len(df)),
    "unique_items": int(df["judge_item_id"].nunique()),
    "scenario_count": int(item["scenario_id"].nunique()),
    "candidate_models": sorted(item["candidate_model"].dropna().unique().tolist()),
    "prompt_conditions": sorted(item["prompt_condition"].dropna().unique().tolist()),
    "overall_composite_mean": float(item["composite"].mean()),
    "model_main_effect": {"friedman_chi2": float(model_stat), "p": float(model_p)},
    "prompt_main_effect": {
        "mean_delta_cbt_safety_minus_minimal": float(np.mean(prompt_diffs)),
        "exact_signed_rank_Wplus": float(prompt_wplus),
        "p": float(prompt_p),
    },
    "model_prompt_interaction": {"friedman_chi2": float(inter_stat), "p": float(inter_p)},
    "majority_critical_failures_total": int(item["critical_safety_failure_0_1"].sum()),
    "bootstrap": {
        "resamples": 10000,
        "seed": 20261031,
        "generator": "numpy.PCG64",
        "unit": "scenario_id",
        "conditions_preserved_within_scenario": True,
    },
}

with open(OUTDIR / "reanalysis_summary.json", "w", encoding="utf-8") as f:
    json.dump(summary, f, indent=2, ensure_ascii=False)

print("AR-CBT++ reanalysis completed.")
print(json.dumps(summary, indent=2, ensure_ascii=False))
print(f"Outputs written to: {OUTDIR}")
