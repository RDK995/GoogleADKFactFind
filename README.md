# Google ADK + Gemini Example Agent

This repository contains a minimal example of a **Google ADK** agent configured to use a **Gemini** model.

## Prerequisites

- Python 3.10+
- A Google AI Studio API key (`GEMINI_API_KEY`)

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Set your API key:

```bash
export GEMINI_API_KEY="your-api-key"
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

Example prompt:

- `Find 3 reputable sources about quantum computing breakthroughs in 2024 and summarize them.`
