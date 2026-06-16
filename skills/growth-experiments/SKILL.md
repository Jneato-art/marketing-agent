---
name: growth-experiments
description: Run a prioritized growth-experiment backlog scored with ICE (Impact, Confidence, Ease), execute the top bets as small tests, and feed results into the self-learning loop. Use when you want compounding growth through disciplined testing rather than random tactics.
---

# Skill: Growth Experiments

Growth comes from running many cheap tests, keeping winners, and compounding. This skill maintains an ICE-scored backlog, runs the top experiments as small bets, and writes every result back into `knowledge/` so the agent gets smarter each cycle.

## When to use
- The user wants growth but has limited time/budget (you must prioritize).
- You have more ideas than you can run (a long backlog).
- You are setting up an ongoing testing cadence.

## ICE scoring
Score every idea 1-10 on three dimensions, then multiply:
- **Impact** - potential effect on the goal (revenue, conversion, signups) if it works.
- **Confidence** - how sure you are it will work (data/precedent = high; hunch = low).
- **Ease** - how cheap/fast to run (high = small effort).

`ICE = Impact x Confidence x Ease`. Rank by score. Run highest first. Re-score as you learn (confidence rises with evidence). Use ICE to *prioritize*, not to replace judgment - sanity-check the top of the list.

## Procedure

1. **Collect ideas** from every other skill: a landing-page test (`landing-page-cro`), a new offer (`offer-and-pricing`), a hook format (`short-form-video`), a subject line (`email-lifecycle`), an outreach template (`partnerships-outreach`).
2. **Write each as a testable hypothesis**: "Because [evidence], [change] will [effect] measured by [metric]."
3. **Score with ICE** and rank.
4. **Run the top 2-3** as small, time-boxed tests. Define the success metric and minimum sample/duration *before* starting (reach statistical significance; expect ~1 in 8 to win).
5. **Decide**: scale winners, kill losers, iterate the promising-but-inconclusive.
6. **Log everything** (next section) - this is the point.
7. **Maintain the backlog** in Airtable (Experiments table; see `marketing-crm-setup`) or `templates/experiment-backlog.md`. Run weekly/biweekly cycles for momentum.

## Backlog format

```
| # | Hypothesis | Metric | Impact | Confidence | Ease | ICE | Status | Result |
|---|---|---|---|---|---|---|---|---|
```

## Connection to the self-learning loop
This skill IS the engine of the agent's self-learning loop (see `docs/self-learning.md`):
- **Before** a cycle: read `knowledge/index.md` and `knowledge/experiments/experiments-log.md` so you don't re-run a known loser.
- **During**: each running test is an open loop tracked in the backlog.
- **After**: append a dated entry to `knowledge/experiments/experiments-log.md` (what you tried, what happened, what you'd change). Promote durable winners to `knowledge/playbooks-learned/` and update `knowledge/index.md`. Next cycle starts smarter.

## Output
- A ranked ICE backlog, 2-3 running experiments with defined success metrics, and a logged result for every completed test.

## Self-learning
This skill exists to feed self-learning. Never close an experiment without logging the outcome and updating the index. A test you didn't record is a test you'll waste budget repeating.
