"""Eval harness.

The eval set is the heart of this project. The README pitch — "recall is
measurable because the universe is enumerable" — is only true if this harness
runs cleanly, regularly, and stays honest as prompts iterate.

Structure:

- cases/         — JSONL files of input + expected output, one per agent.
- run_evals.py   — CLI entry point. Runs cases through agents, writes a report.
- metrics.py     — Recall, precision, Spearman ρ, confusion matrix.
- fixtures.py    — Loads frozen fixtures so eval runs don't hit live APIs.
                   (Live runs happen separately, less often, and are flagged.)
"""
