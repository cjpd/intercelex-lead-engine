"""Base class shared by every agent.

Keeps three things consistent across agents:

1. **Prompt loading** — system prompts live in versioned markdown files
   under `src/prompts/`, never inline in Python. Hot-swappable without code
   changes; trivially diff-able for the prompt-iteration log.
2. **Model selection** — each agent declares whether it needs Sonnet or can
   ride on Haiku. Triage runs on Haiku (high volume, low stakes per item);
   Qualification runs on Sonnet (low volume, high stakes per item).
3. **Eval logging** — each `run()` invocation can be wrapped to emit a
   structured trace (input, output, prompt version, model, tokens, latency)
   that the eval harness consumes.
"""

from __future__ import annotations

import os
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, ClassVar

PROMPTS_DIR = Path(__file__).resolve().parent.parent / "prompts"


class Agent(ABC):
    """Base class for all four agents.

    Subclasses set:
        prompt_file : str  — filename under src/prompts/, e.g. "qualification.md"
        prompt_version : str — semver-ish tag matching the front-matter in the
                               prompt file. Logged on every output.
        model_env_var : str — env var that holds the model id for this agent.
                              Defaults to INTERCELEX_MODEL (Sonnet) but Triage
                              overrides to INTERCELEX_FAST_MODEL (Haiku).
    """

    prompt_file: ClassVar[str]
    prompt_version: ClassVar[str]
    model_env_var: ClassVar[str] = "INTERCELEX_MODEL"

    def __init__(self) -> None:
        self.system_prompt = self._load_prompt()
        self.model = os.environ.get(self.model_env_var, "claude-sonnet-4-6")

    # ------------------------------------------------------------------
    # Prompt loading
    # ------------------------------------------------------------------

    @classmethod
    def _load_prompt(cls) -> str:
        path = PROMPTS_DIR / cls.prompt_file
        if not path.exists():
            raise FileNotFoundError(
                f"Missing system prompt for {cls.__name__}: {path}. "
                "Create the markdown file under src/prompts/."
            )
        return path.read_text(encoding="utf-8")

    # ------------------------------------------------------------------
    # Subclass contract
    # ------------------------------------------------------------------

    @abstractmethod
    async def run(self, *args: Any, **kwargs: Any) -> Any:
        """Execute the agent. Inputs and outputs are typed per subclass."""
