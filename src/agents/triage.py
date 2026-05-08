"""Triage agent.

Role
----
Watch signal feeds and emit Signal objects — *reasons to reach out now*.
Examples: a new USDA Organic certification, a freeze warning over Homestead, a
TREC field-day announcement, a press mention of a Redland grower.

This agent runs on Haiku because it's high-volume and the per-item stakes are
low (a noisy signal is filtered out by the orchestrator before it influences
outreach).

Inputs
------
- A feed item (RSS entry, USDA INTEGRITY diff row, NOAA bulletin, etc.).

Outputs
-------
- 0..N Signal objects. Most feed items produce zero signals (most weather
  bulletins aren't actionable; most press is irrelevant).
"""

from __future__ import annotations

from typing import Any

from src.agents.base import Agent
from src.models import Signal


class TriageAgent(Agent):
    prompt_file = "triage.md"
    prompt_version = "triage@v0"
    model_env_var = "INTERCELEX_FAST_MODEL"  # Haiku

    async def run(self, feed_item: dict[str, Any]) -> list[Signal]:
        """Decide whether a feed item is a reason-to-reach-out, and if so, for whom.

        Implementation plan:

        1. Cheap pre-filter (regex / keyword) before invoking the LLM, so we
           don't spend tokens on every NOAA bulletin in the country.
        2. Call Claude with the Triage prompt; ask for a JSON array of 0..N
           Signals or an empty array.
        3. Resolve `lead_id` against the Lead store when the signal references
           a known operation; leave null otherwise.
        """
        raise NotImplementedError(
            "TriageAgent.run is stubbed. Pre-filters and feed adapters live under "
            "src/tools/ and need source-specific implementations."
        )
