"""USDA Organic INTEGRITY — list of certified organic operations.

Public dataset, distributed as a bulk download (CSV / Excel) plus a search UI.
We snapshot the bulk file under data/snapshots/integrity/ on a weekly cadence;
diffs of the snapshots feed the Triage agent (new / lost certifications).

Docs: https://organic.ams.usda.gov/integrity/
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

from src.models import Evidence, Lead


def search_operations(zip_codes: list[str]) -> list[Lead]:
    """Return certified-organic operations whose mailing or production address
    is in any of the given ZIP codes.

    Reads the latest snapshot under data/snapshots/integrity/. Snapshot rotation
    is handled by `tools.integrity.refresh_snapshot()` (TODO).
    """
    raise NotImplementedError(
        "Wire up after first INTEGRITY snapshot is downloaded into data/snapshots/integrity/."
    )


def diff_against_previous_snapshot() -> tuple[list[dict], list[dict], list[dict]]:
    """Return (newly_certified, lost_certification, renewed) since the last snapshot.

    Used by the Triage agent to emit NEW_CERTIFICATION / LOST_CERTIFICATION signals.
    """
    raise NotImplementedError


def evidence_for(operation_id: str) -> Evidence:
    """Build an Evidence object pointing at an INTEGRITY record."""
    return Evidence(
        source="INTEGRITY",
        url=f"https://organic.ams.usda.gov/integrity/CP/OPP?cid={operation_id}",  # type: ignore[arg-type]
        snapshot_path=str(Path("data/snapshots/integrity") / f"{operation_id}.json"),
        retrieved_at=datetime.utcnow(),
    )
