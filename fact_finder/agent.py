"""Fact Finder agent definition.

This module intentionally contains only Fact Finder-specific behavior.
Shared provider/auth/model config is implemented in `agent_runtime`.
"""

from agent_runtime import configure_agent_runtime
from google.adk.agents import Agent

# Shared runtime configuration:
# - loads `.env`
# - validates provider-specific auth/env requirements
# - resolves model with provider-aware defaults
runtime = configure_agent_runtime()

root_agent = Agent(
    name="fact_finder",
    model=runtime.model,
    description="Research assistant that gathers and summarizes factual information.",
    instruction=(
        "You are a careful fact-finding assistant. "
        "When answering, provide concise summaries and include source links when available."
    ),
)
