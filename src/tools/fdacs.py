"""Florida Department of Agriculture & Consumer Services — nursery licenses, BMP enrollments.

Public bulk downloads. Nursery licenses give us a much bigger universe than
INTEGRITY (most Redland operations are conventional, not certified organic),
and BMP enrollments are a useful proxy for "operation cares about inputs".

Docs (license search): https://aessearch.fdacs.gov/
"""

from __future__ import annotations


def licensed_nurseries(zip_codes: list[str]) -> list[dict]:
    """Return active nursery / plant-broker licenses in the given ZIPs."""
    raise NotImplementedError(
        "Implement by parsing the FDACS bulk license file from data/snapshots/fdacs/."
    )


def bmp_enrollments(county_fips: str = "12086") -> list[dict]:
    """Return Best Management Practices enrollments for a county.

    Used by Triage to emit BMP_ENROLLMENT signals.
    """
    raise NotImplementedError
