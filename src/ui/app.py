"""Streamlit dashboard entry point.

Run locally:
    streamlit run src/ui/app.py

Four tabs map onto the four jobs the founder will do in this app:

1. Coverage Map — st.map() of all known Redland operations, colored by status
   (existing customer / contacted / qualified-not-yet-contacted / unfit /
   unknown). The founder asked to see his coverage gap visually.
2. Pipeline — table of qualified leads ordered by score, with one-click
   approve / edit / reject on outreach drafts.
3. Lead Detail — drill-down on a single lead: sources, signals, evidence chain,
   draft outreach with diff against any edits the founder made.
4. Evals — last eval run summary, per-tier and per-crop breakdowns, prompt
   version log.

Stub for now — wire up to Lead / Qualification / OutreachDraft once the
agents are running and there's something to display.
"""

from __future__ import annotations

import streamlit as st


def main() -> None:
    st.set_page_config(
        page_title="Intercelex Lead Engine",
        page_icon=None,
        layout="wide",
    )

    st.title("Intercelex Lead Engine")
    st.caption("Pilot dashboard — Homestead / Redland organic-grower outreach")

    tab_coverage, tab_pipeline, tab_lead, tab_evals = st.tabs(
        ["Coverage Map", "Pipeline", "Lead Detail", "Evals"]
    )

    with tab_coverage:
        st.subheader("Coverage Map")
        st.info(
            "Stub: will render st.map() with all Redland operations colored by status. "
            "Filter by ZIP, tier, crop, contacted-or-not."
        )

    with tab_pipeline:
        st.subheader("Pipeline")
        st.info(
            "Stub: ranked table of qualified leads with one-click approve / edit / reject "
            "on outreach drafts."
        )

    with tab_lead:
        st.subheader("Lead Detail")
        st.info(
            "Stub: drill-down view. Lead profile + evidence chain + signals + draft sequence."
        )

    with tab_evals:
        st.subheader("Evals")
        st.info(
            "Stub: most recent eval run with per-tier and per-crop breakdowns, prompt-version log."
        )


if __name__ == "__main__":
    main()
