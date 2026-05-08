"""USDA NASS Quick Stats API — county-level crop and acreage statistics.

Used to estimate the population denominator for recall and to enrich Leads
with crop / acreage hints. Requires a free API key (NASS_API_KEY in .env).

Docs: https://quickstats.nass.usda.gov/api
"""

from __future__ import annotations


def county_crop_summary(county_fips: str = "12086") -> dict:
    """Crop / acreage breakdown for a Florida county (default: Miami-Dade = 12086).

    Returns the raw NASS response; caller normalizes.
    """
    raise NotImplementedError(
        "Implement against quickstats.nass.usda.gov/api/api_GET. Cache responses for 24h "
        "(NASS data updates infrequently and rate limits are tight)."
    )
