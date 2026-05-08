"""Ag trade press — English and Spanish, Redland-specific.

Outlets to monitor (initial set; founder will refine):
- Growing Produce
- Florida Grower
- Miami Herald (agriculture beat)
- Diario Las Americas
- AgFunder News (where it covers South Florida)
- UF/IFAS press releases

Implemented as RSS where available, web scrape as fallback. Triage agent
filters items down to actionable signals.
"""

from __future__ import annotations


def latest_items(since_hours: int = 24) -> list[dict]:
    """Return new items across all monitored outlets within the last `since_hours`."""
    raise NotImplementedError(
        "Maintain feed list in src/tools/press_feeds.yaml; implement RSS poller "
        "with httpx + feedparser, persist seen-IDs in SQLite to avoid re-emitting."
    )
