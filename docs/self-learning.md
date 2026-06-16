# The Self-Learning Loop

The agent improves over time because it writes down what it learns and reads it back before every run. There is no model fine-tuning involved — the "learning" is durable, structured memory that the agent maintains itself.

## How it works

```
  read knowledge/  ->  do the work  ->  observe results  ->  write knowledge/
        ^                                                          |
        +----------------------------------------------------------+
```

## The memory store: `knowledge/`

```
knowledge/
  index.md                     A table of contents the agent reads first
  brands/
    <brand>/
      brief.md                 Positioning, audience, voice, constraints
      research.md              Market + competitor findings, with sources
      assets.md                Links to created creative, copy, campaigns
  experiments/
    experiments-log.md         Dated log: what we tried, what happened
  playbooks-learned/
    <name>.md                  Tactics that worked, promoted to reusable
```

## Rules the agent follows

1. **Read before acting.** Always open `index.md` and the brand folder first. Never re-research what is already known unless it is stale (>90 days for fast-moving channels).
2. **Record durable facts only.** Not every detail — just things that will matter next time (a converting hook, a CAC benchmark, a channel that flopped).
3. **Date everything.** Marketing decays. A learning from 8 months ago is a hypothesis, not a fact.
4. **Promote winners.** When an experiment beats its benchmark twice, write it up in `playbooks-learned/` so it becomes default practice.
5. **Prune.** When a learning is contradicted by new results, update or delete it. Stale memory is worse than none.

## Example experiment-log entry

```
## 2026-06-16 | Cold-brew subscription | UGC TikTok hook test
- Tried: 3 TikTok hooks (taste, convenience, price) on $50 each.
- Result: "convenience" hook 2.1% CTR vs 0.6% baseline; others flat.
- Learning: lead with convenience for this audience. Promote to playbook.
- Next: scale convenience angle to $200, test 2 new variations.
```

That single entry means the next campaign starts from "convenience converts" instead of guessing.
