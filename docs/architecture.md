# Architecture

The Marketing Agent is built in layers. Each layer is just files, so it works in any agent harness that can read a folder.

```
+-----------------------------------------------------------+
|  BRAIN          CLAUDE.md / AGENTS.md                      |
|  Role, principles, the Plan->Execute->Measure->Learn loop |
+-----------------------------------------------------------+
|  SKILLS         skills/*/SKILL.md                          |
|  Repeatable capabilities the brain loads on demand        |
+-----------------------------------------------------------+
|  SUB-AGENTS     agents/*.md                                |
|  Specialists the brain delegates to (researcher, etc.)    |
+-----------------------------------------------------------+
|  PLAYBOOKS      playbooks/*.md                             |
|  Proven, situation-specific sequences                     |
+-----------------------------------------------------------+
|  TEMPLATES      templates/*                                |
|  The shape of every deliverable                           |
+-----------------------------------------------------------+
|  MEMORY         knowledge/                                 |
|  What the agent has learned - read first, written last     |
+-----------------------------------------------------------+
|  RUNTIME        agent/  (Claude Agent SDK)                 |
|  Optional: run the whole thing autonomously                |
+-----------------------------------------------------------+
```

## Why files, not code

The agent's capabilities are written as Markdown (skills, playbooks, templates) instead of hard-coded logic. This means:

- **It works anywhere** an agent can read files — Cowork, Claude Code, or the SDK runtime.
- **You can edit it** without being a programmer. Want a new playbook? Add a Markdown file.
- **The agent can edit itself.** When it learns something, it writes a new file into `knowledge/` — that is the self-learning loop.

## Data flow for one request

1. Brain reads `CLAUDE.md` + `knowledge/index.md`.
2. Brain runs Intake, then loads `skills/market-research`.
3. Researcher sub-agent does live web research, writes `knowledge/brands/<brand>/research.md`.
4. Strategist loads `marketing-plan-builder`, fills `templates/marketing-plan.md`.
5. Copywriter drafts assets; automation-builder wires recurring steps.
6. Analyst logs results to `knowledge/experiments/experiments-log.md`.
7. Index updated. Next run starts smarter.
