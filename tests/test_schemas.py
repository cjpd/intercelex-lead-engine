"""Smoke tests for the data contracts.

These run against the real Pydantic models — failing here means an agent's
inputs and outputs no longer agree. Cheap to keep green.
"""

from __future__ import annotations

from datetime import datetime, timezone

import pytest
from pydantic import ValidationError

from src.models import (
    Crop,
    Evidence,
    Lead,
    OutreachDraft,
    OutreachTouch,
    Qualification,
    Tier,
)


def _evidence() -> Evidence:
    return Evidence(
        source="INTEGRITY",
        url="https://organic.ams.usda.gov/integrity/CP/OPP?cid=test",
        retrieved_at=datetime.now(timezone.utc),
    )


def test_lead_round_trip() -> None:
    lead = Lead(
        lead_id="redland-test-33031",
        operation_name="Test Grove LLC",
        zip_code="33031",
        primary_crops=[Crop.AVOCADO, Crop.MANGO],
        is_organic_certified=True,
        discovered_at=datetime.now(timezone.utc),
        sources=[_evidence()],
    )
    assert lead.model_dump()["primary_crops"] == ["avocado", "mango"]


def test_qualification_requires_evidence() -> None:
    with pytest.raises(ValidationError):
        Qualification(
            lead_id="x",
            tier=Tier.T1,
            score=85,
            rationale="...",
            evidence=[],  # min_length=1
            crop_fit=80,
            scale_fit=80,
            organic_alignment=90,
            geographic_proximity=85,
            qualified_at=datetime.now(timezone.utc),
            prompt_version="qualification@v0",
        )


def test_outreach_draft_min_one_touch() -> None:
    with pytest.raises(ValidationError):
        OutreachDraft(
            lead_id="x",
            qualification_score=85,
            why_this_message="neighbor of T1 customer",
            touches=[],  # min_length=1
            drafted_at=datetime.now(timezone.utc),
            prompt_version="outreach@v0",
        )


def test_outreach_touch_subject_optional_for_phone() -> None:
    touch = OutreachTouch(
        sequence_index=1,
        channel="phone_script",
        language="es",
        body="Buenos días, soy ...",
        send_after_days=0,
    )
    assert touch.subject is None
