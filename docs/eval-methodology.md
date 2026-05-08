# Eval methodology

The README pitch — *"recall is measurable because the universe is
enumerable"* — only works if this methodology is followed.

## Ground truth

Three sources of labels, in descending authority:

1. **Founder labels** (highest authority). Hand-labeled during the founder
   call and field visits. Only these count toward published metrics.
2. **Analyst labels.** Used during prompt iteration to triage what to ask the
   founder about. Never published as ground truth.
3. **Heuristic labels.** Generated from public data (e.g., a USDA-certified
   organic operation in 33031 with avocado as primary commodity is presumed
   T1-eligible). Used only for sanity checks.

## Recall denominator

Discovery's recall is measured against the **enumerated Redland universe**.
We construct this once during pilot setup by:

1. Pulling INTEGRITY for all FL operations, filtering to in-scope ZIPs.
2. Pulling FDACS nursery licenses for the same ZIPs.
3. Manual deduplication and normalization, with the founder reviewing the
   final list for completeness ("did we miss anyone you know exists?").

The universe is frozen at start of pilot and stored at
`data/eval/discovery_universe.json`. Discovery is re-run against the same
universe whenever the agent's prompt changes; recall = found / |universe|.

## Per-agent eval design

### Discovery

- Inputs: in-scope ZIP list.
- Expected: list of operation IDs that should appear in the output.
- Metrics: recall (vs. enumerated universe), dedupe accuracy
  (no double-counting of the same op under DBA aliases).

### Qualification

- Inputs: one Lead per case, with full Evidence.
- Expected: tier, score range (±10 around founder's number).
- Metrics: per-tier precision/recall, confusion matrix, Spearman ρ on score.
- Stratified by crop and tier. A T1-recall headline number that hides poor
  recall on avocado is misleading.

### Triage

- Inputs: feed items.
- Expected: 0 or N signals, with kind labels.
- Metrics: precision (false positives waste founder time) and per-kind
  accuracy. Recall less critical — missing one of three press mentions of the
  same event is fine.

### Outreach

- Inputs: Lead + Qualification + Signal.
- Expected: founder rating 1-5 on the resulting draft.
- Metrics: mean rating, % rated >= 4, fraction of drafts that cite the
  Signal verbatim (groundedness check).

## Cost and latency

Measured per run, not per case:

- Cost per qualified lead = total $ spent / count(predicted T1+T2+T3).
- Latency p50 / p95 of the full pipeline per lead.

Both are reported alongside quality metrics. A 3% recall improvement that
triples cost is not a win.

## Reporting

Each run emits a JSON report under `eval-runs/`:

```json
{
  "run_id": "20260512-103015",
  "agent": "qualification",
  "prompt_version": "qualification@v2",
  "model": "claude-sonnet-4-6",
  "n_cases": 30,
  "metrics": {
    "precision": ...,
    "recall": ...,
    "confusion_matrix": ...,
    "spearman_rho": ...
  },
  "cost_usd": ...,
  "latency_p50_ms": ...,
  "latency_p95_ms": ...
}
```

Reports are committed (under `eval-runs/`) so the prompt-iteration log can
reference run IDs.

## Honesty rules

- Never tune a prompt against the founder-labeled set. Use a separate analyst
  set for iteration; only run founder set as a holdout.
- Never report metrics from a partial run. If 5 of 30 cases errored,
  the run is a failure, not a 25-case result.
- Always report cost and latency next to quality. Reviewers should be able
  to see the full picture in one screen.
