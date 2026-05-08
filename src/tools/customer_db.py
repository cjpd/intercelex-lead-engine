"""Founder's customer list — sensitive data, local SQLite only.

This is the only tool with read access to the founder's private list. It never
exposes contact details to agents — only operation name, ZIP, and tier. The
Discovery agent uses this to flag `is_existing_customer` and the Qualification
agent uses it to compute geographic proximity.

DB path is configured via INTERCELEX_DB_PATH (.env). The file is gitignored.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CustomerStub:
    """The minimal shape we expose to agents — no PII."""

    operation_name: str
    zip_code: str
    tier: str  # tier_1 / tier_2 / tier_3
    latitude: float | None
    longitude: float | None


def list_customers() -> list[CustomerStub]:
    """Read the customer list from local SQLite. PII (emails, phones, contracts) is never returned."""
    raise NotImplementedError(
        "Implement after the founder hands over his customer list. Schema: "
        "operations(operation_name TEXT PRIMARY KEY, zip TEXT, tier TEXT, lat REAL, lon REAL, "
        "first_sale_date DATE, ...). PII columns must NOT be exposed via this function."
    )


def list_previously_contacted() -> set[str]:
    """Operation names the founder has reached out to, regardless of outcome."""
    raise NotImplementedError
