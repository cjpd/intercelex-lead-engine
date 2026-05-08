# Project brief

The canonical project brief (v4) lives in this Claude Project's knowledge
files. It has not been copied here to avoid drift — when the brief changes,
update the project knowledge, not this file.

This document instead pins the *operational decisions* that have to be
referenced from code. When the brief changes, update this file too.

## Decisions pinned for the codebase

| Decision | Value | Source |
|---|---|---|
| Scope | Redland: Miami-Dade ZIPs around Homestead | brief v4 |
| In-scope ZIPs | TBD — confirm during founder call | — |
| Tiers | T1 / T2 / T3 / UNFIT | brief v4 |
| Tier definitions | TBD — confirm during founder call | — |
| Languages | English + Spanish, drafted natively | brief v4 |
| Channels | Email primary, SMS optional, phone script always | brief v4 |
| Touches | 3 max per lead | brief v4 |
| Privacy | Founder customer list never leaves laptop | brief v4 |
| Eval cadence | Every prompt change; weekly during pilot | README |

## Open questions for the founder call

These questions need answers before the qualification rubric and outreach tone
can be encoded into prompts.

### Scope
- What ZIPs are in scope? Is 33031, 33032, 33033, 33034, 33170, 33187 the right list?
- Are conventional (non-organic) growers in scope, or organic-only?

### Tiers
- What's the difference between a T1 and a T2 customer?
- What disqualifies a lead outright (UNFIT)?
- How heavily does proximity to existing customers count?

### Outreach
- Sample phrases the founder uses on a real call
- Words / framings to avoid
- Sign-off conventions, formal vs informal
- How agronomically deep should first-touch go?

### Operations
- How many leads per week is a reasonable approval queue?
- Is there a dollar-value threshold below which we shouldn't bother?

## Eval set seed

A target ~30 leads to hand-label during the founder call:

- 10 obvious T1s (the founder's existing best customers, blinded)
- 10 marginal cases (the founder has to think about it)
- 10 wrong-fit (the founder rejects on sight)

Plus 20 outreach drafts to rate 1-5 after a v0 pass.

The eval set is the deliverable from the call, not a side effect.
