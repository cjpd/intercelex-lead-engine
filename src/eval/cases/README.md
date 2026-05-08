# Eval cases

Hand-labeled cases the agents are tested against. One JSONL file per agent.

## Layout

```
data/eval/
├── qualification.jsonl     # ~30 leads, 10/10/10 ideal/marginal/wrong-fit
├── outreach.jsonl          # ~20 drafted touches with founder ratings 1-5
├── triage.jsonl            # ~50 feed items with binary signal-or-not labels
└── discovery_universe.json # the enumerated Redland universe (recall denominator)
```

The actual labeled data lives under `data/eval/` (gitignored if it contains
identifiable info from the founder's customer list). This directory is for
*public-safe* eval scaffolding — fixtures, examples, schemas.

## Case format

Each line is a JSON object with `input`, `expected`, and `metadata`. Example
for `qualification.jsonl`:

```json
{"input": {"lead": {...}}, "expected": {"tier": "tier_1", "score_range": [80, 100]}, "metadata": {"crop": "avocado", "labeled_by": "founder", "labeled_on": "2026-05-08"}}
```

Notes:

- `expected.score_range` is a 2-tuple, not a single number — the founder's
  scoring is calibrated within ±10 at best, so exact-match is the wrong target.
- `metadata.labeled_by` distinguishes founder labels from analyst labels.
  Only founder labels count toward published recall/precision.
