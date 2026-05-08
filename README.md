# Intercelex Lead Engine

> A multi-agent system that maps the Homestead/Redland organic-grower universe, identifies operations a Miami-based organic fertilizer founder hasn't yet reached, qualifies them against his actual customer profile, and generates bilingual outreach grounded in real signals.

**Status:** In active development. Pilot underway with Intercelex (Miami, FL) as design partner.

---

## The problem

Intercelex is a solo-founder organic fertilizer company headquartered in Miami. Their customer base is concentrated in the Redland — Miami-Dade's tropical fruit and winter vegetable belt around Homestead. The founder does all sales personally and has never had time to systematically canvas his own backyard.

The Redland contains dozens of organic-certified operations and hundreds of conventional ones. Many are within 15 miles of existing customers and have never been contacted.

This project finds them.

## The approach

A multi-agent system, built on the Anthropic API with tool use, that:

1. **Enumerates** the Redland grower universe from public data sources (USDA Organic INTEGRITY, NASS Quick Stats, FDACS nursery licenses)
2. **Cross-references** against the founder's existing customer list to surface "missed" operations
3. **Qualifies** each lead against a tier-specific rubric derived from the founder's actual best customers
4. **Monitors** real ag-industry signals (new certifications, hurricane damage, freeze events, BMP enrollments, extension field-days)
5. **Drafts** bilingual outreach grounded in evidence — never generic, always citing a real reason for contact
6. **Surfaces** ranked leads to the founder for one-click approve/edit/reject, with full evidence chain

The system is designed for a solo operator. Architecture extends without redesign to Broward, Palm Beach, GA, SC, and AL.

## Architecture

```
┌─────────────────┐     ┌─────────────────┐     ┌──────────────────┐
│ Discovery Agent │────▶│ Qualification   │────▶│ Outreach Agent   │
│                 │     │ Agent           │     │                  │
│ - INTEGRITY     │     │ - Tier classify │     │ - EN + ES drafts │
│ - NASS          │     │ - Score 0-100   │     │ - 3-touch seq    │
│ - FDACS         │     │ - Evidence      │     │ - Talk track     │
│ - Press (EN/ES) │     │ - Rationale     │     │ - Why-this-msg   │
└─────────────────┘     └─────────────────┘     └──────────────────┘
        ▲                       ▲                        │
        │                       │                        ▼
┌───────┴────────┐     ┌───────┴────────┐     ┌──────────────────┐
│ Triage Agent   │     │ Founder's      │     │ Streamlit UI     │
│ (signal feeds) │     │ customer list  │     │ Coverage Map     │
└────────────────┘     │ (private)      │     │ Approve/Edit     │
                       └────────────────┘     │ Pipeline         │
                                              │ Evals            │
                                              └──────────────────┘
```

See `docs/architecture.md` for the detailed agent contracts and data flow.

## Why this is interesting

Most "AI agent" portfolio projects skip evals. This one is built around them.

The Redland is small enough that the agent's universe of qualified leads can be **enumerated** from public data. That makes **recall measurable**, not just precision — a metric most LLM applications can't honestly produce.

The pilot includes 1–2 in-person grower visits with the founder to validate qualification rubrics in the field.

## Tech stack

- **Python 3.11+**
- **Anthropic API** — Claude with tool use, structured outputs (Pydantic). Orchestration via the [Claude Agent SDK](https://docs.claude.com/en/docs/agent-sdk).
- **Claude Code** for development acceleration
- **Streamlit** — single-operator dashboard with `st.map()` for the Coverage view
- **SQLite** — local storage (private customer data never leaves disk)
- **Data sources:** USDA Organic INTEGRITY, NASS Quick Stats API, FDACS, UF/IFAS TREC, NOAA/NWS Miami, ag trade press

## Eval methodology

The eval set is built from a recorded conversation with the Intercelex founder:

- ~30 hand-labeled leads (10 ideal / 10 marginal / 10 wrong-fit), stratified by buyer tier and crop type
- 20 outreach drafts rated 1–5 by the founder
- Full enumerated Redland universe as the recall denominator

**Reported metrics:**

- Qualification recall and precision (with stratified breakdowns by tier and crop type)
- Tier classification accuracy (confusion matrix)
- Score correlation (Spearman ρ) between agent and founder
- Outreach quality (mean rating)
- Cost per qualified lead, latency p50/p95
- "Missed customer" coverage gap closed

Prompt iteration is documented: v1 → v2 → v3 with measured deltas at each stage.

## Project status

| Milestone | Status |
|---|---|
| Project scoping & brief | Complete (v4) |
| Repo + architecture scaffolded | Complete |
| Founder call & ICP extraction | Scheduled |
| Universe enumeration | Pending |
| Discovery + Qualification agents | Pending |
| Signal monitoring + Outreach agent | Pending |
| First field visit | Pending |
| Eval harness + observability | Pending |
| Pilot results | Pending |
| Writeup published | Pending |

## Repository structure

```
intercelex-lead-engine/
├── README.md                 # You are here
├── docs/
│   ├── brief.md             # Full project brief (v4)
│   ├── architecture.md      # Detailed architecture
│   ├── eval-methodology.md  # How evals are constructed
│   └── prompt-iteration.md  # v1 → v2 → v3 prompt log with deltas
├── src/
│   ├── agents/
│   │   ├── discovery.py
│   │   ├── qualification.py
│   │   ├── triage.py
│   │   └── outreach.py
│   ├── tools/               # Tool definitions for each data source
│   ├── models/              # Pydantic schemas
│   ├── prompts/             # Versioned system prompts (markdown)
│   ├── eval/                # Eval harness
│   └── ui/                  # Streamlit dashboard
├── data/
│   ├── eval/                # Labeled eval set (anonymized)
│   └── snapshots/           # INTEGRITY / FDACS bulk snapshots
├── notebooks/               # Exploration and analysis
└── tests/
```

## Getting started

```bash
# Python 3.11+
python -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -e ".[dev]"

cp .env.example .env          # fill in ANTHROPIC_API_KEY etc.

streamlit run src/ui/app.py   # dashboard (stub)
python -m src.eval.run_evals  # eval harness (stub)
```

## Privacy and data handling

The founder's customer list and "contacted, no deal" list are sensitive business data:

- Stored locally only (SQLite, never committed)
- Anonymized in any public writeup or demo
- Deleted at the end of the pilot if requested
- NDA signed if requested

All outreach follows CAN-SPAM: real identifiable sender, low daily volume, easy unsubscribe, accurate subject lines.

## License

Code: MIT. Pilot data: not licensed for public use.

## Acknowledgments

Built in partnership with Intercelex (intercelex.com). Architecture and methodology informed by the Anthropic developer documentation.

---

*Writeup, demo video, and eval results will be linked here when the pilot completes.*
