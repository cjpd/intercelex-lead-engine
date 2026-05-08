"""CLI entry point for running the eval set.

Usage:
    python -m src.eval.run_evals --agent qualification
    python -m src.eval.run_evals --agent qualification --cases data/eval/qualification.jsonl
    python -m src.eval.run_evals --all --report eval-runs/$(date +%Y%m%d-%H%M).json

Stub for now — fill in once the founder call yields the first hand-labeled cases.
"""

from __future__ import annotations

import argparse
import sys


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run Intercelex agent evals.")
    parser.add_argument(
        "--agent",
        choices=["discovery", "qualification", "triage", "outreach", "all"],
        default="all",
        help="Which agent's eval set to run.",
    )
    parser.add_argument(
        "--cases",
        help="Path to a JSONL eval file. Defaults to data/eval/<agent>.jsonl.",
    )
    parser.add_argument(
        "--report",
        help="Where to write the run report (JSON).",
    )
    parser.add_argument(
        "--live",
        action="store_true",
        help="Hit live data sources instead of fixtures. Slower, costs API credits.",
    )
    args = parser.parse_args(argv)

    print(f"[stub] Would run {args.agent} evals (live={args.live}).")
    print(
        "[stub] Eval runner is not implemented yet. "
        "First step: drop founder-labeled cases into data/eval/qualification.jsonl, "
        "then implement load_cases() and per-agent runners."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
