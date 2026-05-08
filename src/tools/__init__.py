"""Data-source adapters that agents call as tools.

Each module exposes typed functions that agents can use via Claude tool use
(decorate with `@tool` from claude-agent-sdk when wiring up). Agents do not
talk to data sources directly — they go through these adapters so that:

- The same adapter can be swapped from "live API" to "fixture" in eval runs.
- Rate limiting, retries, and snapshot-on-disk caching live in one place.
- Privacy-sensitive calls (customer_db) are auditable.
"""
