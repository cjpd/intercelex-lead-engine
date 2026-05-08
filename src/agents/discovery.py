"""Discovery agent.

Role
----
Enumerate the universe of grower operations in the Redland (and adjacent ZIPs
the founder considers in-scope). Cross-reference against the founder's existing
customer list to flag operations that have *not* been contacted.

Inputs
------
- A geographic scope (list of ZIP codes, or a county-level filter).
- The current customer list (read from `tools.customer_db`).
- Bulk snapshots / API access for INTEGRITY, NASS, FDACS, ag press.

Outputs
-------
- list[Lead] — each Lead carries Evidence pointing back to the source records
  that produced it.

Notes
-----
- Discovery is the only agent that may produce *new* Leads. Every other agent
  takes a Lead as input.
- Deduplication is the hard part. Multiple sources will reference the same
  operation under slightly different names. We dedupe on (normalized name,
  zip) plus FDACS license number / INTEGRITY operation_id when available.
"""

from __future__ import annotations

from typing import Iterable

from src.agents.base import Agent
from src.models import Lead


class DiscoveryAgent(Agent):
    prompt_file = "discovery.md"
    prompt_version = "discovery@v0"

    async def run(
        self,
        zip_codes: Iterable[str],
        existing_customer_ids: set[str] | None = None,
    ) -> list[Lead]:
        """Enumerate Leads in the given geographic scope.

        Implementation plan (to wire up after the founder call):

        1. Pull bulk snapshots via `tools.integrity`, `tools.fdacs`, `tools.nass`.
        2. Normalize and merge records into candidate Leads.
        3. Use Claude with tool use to:
           - resolve ambiguous operation names against ag press / web search
           - extract crop and acreage hints from unstructured fields
        4. Mark `is_existing_customer` and `is_previously_contacted` from the
           customer DB.
        5. Return a deduped list.

        Until then, this raises so we don't ship a silent no-op into evals.
        """
        raise NotImplementedError(
            "DiscoveryAgent.run is stubbed. Wire up tools/ and the SDK call after "
            "the founder call confirms the in-scope ZIPs and the customer-DB schema."
        )
