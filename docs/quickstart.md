# Quickstart

## Option A — Use it inside Claude (no code)

1. Open this folder in Claude Cowork or Claude Code.
2. Say: **"Read CLAUDE.md, then build me a marketing plan for [your product]."**
3. Answer the 5 intake questions.
4. The agent researches live, fills `templates/marketing-plan.md`, and gives you Next 3 Actions.
5. For any step, ask: *"how do I do this"*, *"do it for me"*, or *"automate this."*

That's it. Everything it learns is saved to `knowledge/` for next time.

## Option B — Run it autonomously (Python)

Requires Python 3.10+ and an Anthropic API key.

```bash
cd agent
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env        # then add your ANTHROPIC_API_KEY
python marketing_agent.py "Build a 90-day plan for my cold-brew subscription"
```

The agent will run the full loop and write deliverables to `agent/out/` and learnings to `knowledge/`.

## Option C — Schedule it

In Cowork, ask: *"Run my weekly marketing report every Monday at 8am."* The agent sets up a scheduled task that pulls analytics, summarizes what moved, and proposes the next test.

## First things to try

- "Research my market and competitors."
- "Build me a 90-day marketing plan."
- "Give me a 30-day content calendar."
- "Write me 3 ad concepts and generate the creative."
- "Automate my weekly performance report."
