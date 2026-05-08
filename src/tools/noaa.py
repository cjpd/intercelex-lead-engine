"""NOAA / NWS Miami — freeze warnings, hurricane advisories, drought.

Used by the Triage agent to emit FREEZE_EVENT and HURRICANE_DAMAGE signals.

NOAA APIs are public and unmetered. We poll the Miami forecast office's
products feed.
"""

from __future__ import annotations


def recent_alerts(area: str = "FLZ073") -> list[dict]:
    """Return recent NWS alerts for the South Florida zone covering the Redland.

    FLZ073 = Inland Miami-Dade. Adjacent zones may also matter for hurricanes.
    """
    raise NotImplementedError(
        "Implement against https://api.weather.gov/alerts/active?zone=FLZ073"
    )
