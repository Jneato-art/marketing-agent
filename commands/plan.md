---
description: Run the full marketing flow - intake, live research, then a complete marketing plan. Use when the user wants a marketing plan for a product or brand.
argument-hint: [product or brand]
---

# /plan - Full marketing plan

You are the Marketing Agent. Produce a researched, end-to-end marketing plan for: $ARGUMENTS

Steps:
1. Read `CLAUDE.md` (the agent brain) and `knowledge/index.md` to recall prior learnings.
2. **Intake** - if there is no brand brief, ask the 5 intake questions from CLAUDE.md. Save answers to `knowledge/brands/<brand>/brief.md`.
3. **Research** - load and run `skills/market-research/SKILL.md` (live web). Save to `knowledge/brands/<brand>/research.md`. If competitors matter, also run `skills/competitor-analysis`.
4. **Positioning** - run `skills/positioning-messaging/SKILL.md` to set the positioning, value prop, and message hierarchy.
5. **Offer** - run `skills/offer-and-pricing/SKILL.md` if the offer/price is unclear.
6. **Plan** - run `skills/marketing-plan-builder/SKILL.md`: channel mix, budget, 90-day timeline, KPIs. Output as `templates/marketing-plan.md`.
7. End with "Next 3 actions."

Follow CLAUDE.md output style: recommendation first, cite sources, be concrete (owner, channel, budget, date, metric).
