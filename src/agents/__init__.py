"""Agent implementations.

Four agents, each with a single responsibility:

- DiscoveryAgent  : enumerates the Redland grower universe from public data.
- QualificationAgent : scores a Lead against the founder's ICP rubric.
- TriageAgent     : monitors signal feeds and surfaces reasons-to-reach-out-now.
- OutreachAgent   : drafts bilingual 3-touch sequences grounded in evidence.

The orchestrator (`src.orchestrator`, to be added) wires them together. Each
agent is independently testable against the eval harness in `src.eval`.
"""

from src.agents.base import Agent
from src.agents.discovery import DiscoveryAgent
from src.agents.outreach import OutreachAgent
from src.agents.qualification import QualificationAgent
from src.agents.triage import TriageAgent

__all__ = [
    "Agent",
    "DiscoveryAgent",
    "OutreachAgent",
    "QualificationAgent",
    "TriageAgent",
]
