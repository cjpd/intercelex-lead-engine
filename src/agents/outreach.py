"""Outreach agent.

Role
----
Draft a 3-touch bilingual outreach sequence (English + Spanish) for a qualified
Lead, grounded in a specific Signal or customer-list cross-reference. Output
includes a "why this message" justification and a talk track for follow-up.

Nothing is sent automatically. The Streamlit UI shows the draft for founder
approval / edit / reject.

Inputs
------
- One Lead.
- One Qualification (must be Tier 1, 2, or 3 — never UNFIT).
- One Signal (optional but strongly preferred — leads without a fresh signal
  produce weaker drafts).

Outputs
-------
- One OutreachDraft with 3 touches (or fewer if the Lead profile suggests
  phone-only).

Notes
-----
- Refuses to draft if there's no Evidence to anchor the message. We never want
  the founder sending generic outreach with our name on it.
- Spanish drafts are not translations — they're separately drafted, since the
  Redland Spanish-speaking growers have meaningfully different conventions.
"""

from __future__ import annotations

from src.agents.base import Agent
from src.models import Lead, OutreachDraft, Qualification, Signal, Tier


class OutreachAgent(Agent):
    prompt_file = "outreach.md"
    prompt_version = "outreach@v0"

    async def run(
        self,
        lead: Lead,
        qualification: Qualification,
        signal: Signal | None = None,
    ) -> OutreachDraft:
        """Draft a 3-touch outreach package.

        Implementation plan:

        1. Refuse if `qualification.tier == Tier.UNFIT`.
        2. Refuse if no Signal AND no neighboring-customer evidence — we have
           nothing concrete to lead with.
        3. Call Claude twice (EN, then ES) with the Outreach prompt and force
           the OutreachTouch schema.
        4. Compose the OutreachDraft with a `why_this_message` line that names
           the Signal or the neighbor-customer cross-reference explicitly.
        """
        if qualification.tier == Tier.UNFIT:
            raise ValueError(
                f"Refusing to draft outreach for unfit lead {lead.lead_id}."
            )
        raise NotImplementedError(
            "OutreachAgent.run is stubbed. EN and ES prompts in "
            "src/prompts/outreach.md need to be filled in after the founder call "
            "(tone, sample phrases, sign-off conventions)."
        )
