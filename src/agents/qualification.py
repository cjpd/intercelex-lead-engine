"""Qualification agent.

Role
----
Score one Lead against the founder's ICP rubric. Produce a Tier, a 0-100
composite score, four sub-scores (crop fit, scale fit, organic alignment,
geographic proximity), and a 2-4 sentence rationale citing evidence.

This is the agent that owns the eval set. The founder's hand-labeled 30 leads
are the ground truth. Recall and precision are reported per Tier and per crop.

Inputs
------
- One Lead.
- The founder's customer list (used to compute proximity to existing accounts).

Outputs
-------
- One Qualification.

Notes
-----
- The system prompt for this agent is the *qualification rubric*. It MUST be
  derived from the founder call and committed to `src/prompts/qualification.md`
  before the first eval run.
- Refuse to qualify a Lead that lacks any Evidence. Garbage in, garbage out.
"""

from __future__ import annotations

from src.agents.base import Agent
from src.models import Lead, Qualification


class QualificationAgent(Agent):
    prompt_file = "qualification.md"
    prompt_version = "qualification@v0"

    async def run(self, lead: Lead) -> Qualification:
        """Score a Lead.

        Implementation plan:

        1. Build the user message: serialize Lead + neighboring-customer context.
        2. Call Claude with structured output forced to the Qualification schema.
        3. Validate that `evidence` references real sources from the input.
           Re-prompt once if hallucinated.
        4. Stamp `prompt_version` so eval runs are reproducible.
        """
        if not lead.sources:
            raise ValueError(
                f"Lead {lead.lead_id} has no sources. Refusing to qualify without evidence."
            )
        raise NotImplementedError(
            "QualificationAgent.run is stubbed. The system prompt in "
            "src/prompts/qualification.md is a placeholder and must be replaced "
            "with the rubric extracted from the founder call before first eval run."
        )
