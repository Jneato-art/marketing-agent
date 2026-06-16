---
name: marketing-plan-builder
description: Turn research into a concrete 90-day marketing plan with positioning, channel mix, budget, timeline, and KPIs. Use after research and competitor analysis are done.
---

# Skill: Marketing Plan Builder

## When to use
Once you have the brand brief and research. This is where strategy becomes a plan someone can execute.

## Inputs
- `knowledge/brands/<brand>/brief.md` and `research.md`

## Procedure

1. **Set the objective.** One primary 90-day goal, stated as a number (e.g. "300 paid subscribers" or "$15k MRR").
2. **Write positioning.** One sentence: For [audience] who [need], [brand] is the [category] that [unique benefit], unlike [alternative].
3. **Choose the channel mix** (use `channel-strategy`). Pick 2-3 channels max for 90 days. Doing two channels well beats five badly.
4. **Allocate budget** across channels using the 70/20/10 rule: 70% to proven, 20% to promising, 10% to experimental.
5. **Build the timeline.** Break 90 days into 3 phases: Foundation (wk 1-3), Launch (wk 4-8), Scale (wk 9-12). Each phase has 2-4 concrete initiatives.
6. **Define KPIs.** A north-star metric plus one leading indicator per channel. Set targets.
7. **Plan the tests.** List 3 experiments with hypotheses — this is how the plan improves itself.
8. **Fill** `templates/marketing-plan.md` and save a copy to `knowledge/brands/<brand>/`.

## Quality bar
Every line item must have: an owner, a channel, a budget or time cost, a date, and a metric. If it doesn't, it's a wish, not a plan.

## Output
A completed `marketing-plan.md` ending in **Next 3 Actions** the user can start today.

## Self-learning
Log the plan's hypotheses to `knowledge/experiments/experiments-log.md` so results can be checked against them later.
