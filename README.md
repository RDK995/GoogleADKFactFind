# Google ADK Agent (Vertex or OpenAI)

This repository contains a minimal **Google ADK** agent with an env-driven provider switch.

## Project Structure

- `agent_runtime/config.py`: Shared runtime logic for all agents.
  - Loads `.env`
  - Validates provider requirements (Vertex/OpenAI)
  - Validates auth setup (ADC/OpenAI key)
  - Resolves model defaults per provider
- `fact_finder/agent.py`: Fact Finder behavior only (name, description, instruction).

This keeps each agent module focused on domain logic while reusing one runtime policy.

## Prerequisites

- Python 3.10+
- One provider setup:
  - Vertex AI: `AGENT_PROVIDER=vertex`, `GOOGLE_CLOUD_PROJECT`, `GOOGLE_CLOUD_LOCATION`, ADC credentials
  - OpenAI: `AGENT_PROVIDER=openai`, `OPENAI_API_KEY`

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Configure environment variables:

```bash
cp .env.example .env
# Edit .env and choose your provider.
```

Load environment variables into your shell:

```bash
set -a
source .env
set +a
```

`.env` is ignored by git, so secrets stay local.
You can override the model with `ADK_MODEL` in `.env`.

Provider defaults:
- `vertex` -> `gemini-2.0-flash`
- `openai` -> `gpt-4o-mini`

For Vertex AI auth, ensure ADC credentials are available:

```bash
gcloud auth application-default login
```

## Run in ADK Web UI

```bash
adk web
```

Then select the `fact_finder` agent.

## Run from command line

```bash
adk run fact_finder
```

## Adding More Agents

Create a new `your_agent/agent.py` and reuse the shared runtime:

```python
from agent_runtime import configure_agent_runtime
from google.adk.agents import Agent

runtime = configure_agent_runtime()

root_agent = Agent(
    name="your_agent",
    model=runtime.model,
    description="...",
    instruction="...",
)
```

Example prompt:

- `Find 3 reputable sources about quantum computing breakthroughs in 2024 and summarize them.`

## Switching To ChatGPT

Set the following in `.env`:

```bash
AGENT_PROVIDER=openai
OPENAI_API_KEY=your-openai-api-key
# Optional:
# ADK_MODEL=gpt-4o-mini
```

## Troubleshooting 429 RESOURCE_EXHAUSTED (Vertex)

If you see quota errors like `limit: 0` for `gemini-2.0-flash`, your Vertex project has no available quota for that model.

1. Verify usage/limits in Google Cloud for the configured project.
2. Enable billing or request higher quotas for the project.
3. Try a different model by setting `ADK_MODEL` in `.env`.
4. Confirm Vertex env vars are set:
   - `GOOGLE_GENAI_USE_VERTEXAI=true`
   - `GOOGLE_CLOUD_PROJECT=your-project-id`
   - `GOOGLE_CLOUD_LOCATION=us-central1`
