"""Shared runtime utilities for ADK agents in this repository.

This package contains reusable configuration/auth helpers so each individual
agent file stays focused on agent-specific behavior (name, instructions, tools).
"""

from .config import AgentRuntimeConfig, configure_agent_runtime

__all__ = ["AgentRuntimeConfig", "configure_agent_runtime"]
