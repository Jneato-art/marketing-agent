# Autonomous Runtime

This turns the file-based agent into a program you can run from the command line or on a schedule. It uses the [Claude Agent SDK](https://docs.claude.com/en/api/agent-sdk/overview), loads `CLAUDE.md` as the system prompt, gives the agent its skills/playbooks/knowledge as readable files, and lets it search the web and write deliverables.

## Setup
```bash
cd agent
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env        # add your ANTHROPIC_API_KEY
```

## Run
```bash
python marketing_agent.py "Build a 90-day plan for my cold-brew subscription"
```

Outputs go to `agent/out/`; learnings are written back into `../knowledge/`.

## How it stays self-improving
On each run the agent reads `knowledge/index.md` and the brand folder first, and is instructed (by `CLAUDE.md`) to append results to `knowledge/experiments/experiments-log.md` at the end. Because the runtime grants it file write access to `knowledge/`, the memory persists across runs and across both modes (CLI and Cowork).

## Connectors
Add MCP servers (Bloom, Higgsfield, Mailchimp, n8n, Airtable, etc.) via the `mcp_servers` argument in `marketing_agent.py`. See `../docs/connectors.md`.
