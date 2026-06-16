# Specialist Sub-Agents

The brain (`CLAUDE.md`) delegates big tasks to these specialists. Each is a focused role with its own principles, tools, and output format. They hand off to each other in a chain:

```
researcher -> strategist -> copywriter -> analyst -> (back to strategist)
```

- **researcher** — finds the truth about the market
- **strategist** — turns it into a 90-day plan
- **copywriter** — writes the assets
- **analyst** — measures results and feeds learnings back

In the autonomous runtime (`agent/`), these map to Claude Agent SDK subagents. In Cowork/Claude Code, the brain reads the relevant file and adopts that role.
