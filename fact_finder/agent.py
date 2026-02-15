"""Example Google ADK agent that uses Gemini as the LLM."""

from google.adk.agents import Agent


root_agent = Agent(
    name="fact_finder",
    model="gemini-2.0-flash",
    description="Research assistant that gathers and summarizes factual information.",
    instruction=(
        "You are a careful fact-finding assistant. "
        "When answering, provide concise summaries and include source links when available."
    ),
)
