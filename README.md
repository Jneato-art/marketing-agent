# Marketing Agent

A **self-improving AI marketing agent** that researches how to market any product, builds complete marketing plans, and then either tells you exactly how to execute each step or builds the automation to do it for you.

It is built to run two ways:

1. **Inside Claude (Cowork / Claude Code)** — open this repo and the `skills/`, `agents/`, and `playbooks/` turn Claude into a marketing operator you talk to.
2. **Autonomously** — the `agent/` folder is a Python program built on the [Claude Agent SDK](https://docs.claude.com/en/api/agent-sdk/overview) that can research, plan, and produce deliverables on its own or on a schedule.

---

## What it does

```
  YOU: "Market my cold-brew coffee subscription."
   |
   v
  +--------------+   researches the market, the buyer, the
  |  RESEARCHER  |   competitors, and current best practices
  +------+-------+   (live web research, saved to knowledge/)
         v
  +--------------+   turns research into positioning, channel mix,
  |  STRATEGIST  |   budget, and a 90-day marketing plan
  +------+-------+
         v
  +--------------+   writes the copy, briefs the creative,
  |  COPYWRITER  |   drafts emails / posts / ad scripts
  +------+-------+
         v
  +--------------+   measures results, logs what worked, and feeds
  |   ANALYST    |   learnings back into knowledge/ for next time
  +--------------+
```

Every run makes the agent better because it writes what it learns to `knowledge/`, which it reads at the start of the next run. That is the "self-learning" loop — see [docs/self-learning.md](docs/self-learning.md).

---

## The three things it gives you

| You ask for... | You get... |
|---|---|
| **A plan** | A researched, channel-by-channel marketing plan with budget, timeline, and KPIs |
| **How to do a step** | A step-by-step execution guide — what to do, in what tool, in what order |
| **Automation** | A ready-to-run workflow (n8n, scheduled tasks, email/CRM sequences) that does it for you |

---

## Quick start

**In Claude Cowork / Claude Code:** open this folder and say:

> "Read CLAUDE.md, then build me a marketing plan for [my product]."

The agent loads its brain, asks a few brand questions, researches live, and produces a plan.

**As an autonomous program:** see [docs/quickstart.md](docs/quickstart.md).

---

## Repo map

```
CLAUDE.md     The agent's brain - role, principles, operating loop
skills/       Repeatable capabilities (research, planning, content, automation)
agents/       Specialist sub-agents (researcher, strategist, copywriter, analyst)
playbooks/    Proven marketing playbooks (launch, growth, SEO, paid, social)
templates/    Fill-in deliverables (plan, competitor matrix, briefs, calendar)
knowledge/    The agent's memory - what it has learned, per brand and experiment
agent/        Autonomous Python agent (Claude Agent SDK)
docs/         Architecture, self-learning, connectors, quickstart
```

---

## Connected tools it can use

This agent plugs into marketing tools via MCP connectors. See [docs/connectors.md](docs/connectors.md) for the full list and what each unlocks (image/ad generation, video, email campaigns, CRM, workflow automation).

---

## License

MIT — see [LICENSE](LICENSE).
