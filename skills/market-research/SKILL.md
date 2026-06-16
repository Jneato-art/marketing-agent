---
name: market-research
description: Research a market, audience, and channel landscape using live web data before building any marketing plan. Use whenever you need current facts about who the buyer is, where they spend attention, what the category looks like, and what is working now.
---

# Skill: Market Research

Marketing advice is only as good as the facts behind it, and facts decay. This skill produces a grounded, sourced picture of the market **as it is today**.

## When to use
Before any plan, positioning, or channel decision for a brand you have not researched recently (or whose research is >90 days old).

## Inputs
- The brand brief (`knowledge/brands/<brand>/brief.md`). If missing, run intake first.

## Procedure

1. **Frame the questions.** Write the 5-7 specific questions this research must answer, e.g. "How big is the cold-brew DTC market?", "Who buys premium coffee subscriptions?", "Which channels do competitors use?"
2. **Search live.** Use web search for each question. Prefer recent sources (last 12-18 months). Look for: market size/growth, audience demographics & psychographics, buying triggers, price benchmarks, and channel norms.
3. **Map the audience.** Build a 1-paragraph ideal-customer profile + their top 3 pains and top 3 desires, and where they spend attention (specific platforms, communities, search terms).
4. **Scan the category.** Note the 3-5 dominant players and how they position (defer deep competitor work to `competitor-analysis`).
5. **Find what's working now.** Identify the 2-3 channels/tactics currently driving results in this category, with evidence.
6. **Cite everything.** Every non-obvious claim gets a source URL.
7. **Save.** Write to `knowledge/brands/<brand>/research.md` using the output format below.

## Output format

```
# Market Research — <brand> (<date>)

## Market
- Size & growth: ... [source]
- Key trends: ... [source]

## Ideal customer
<one paragraph>. Pains: ... Desires: ... Attention lives at: ...

## Category players
- <name>: positioned as ...

## What's working now
- <tactic/channel>: evidence ... [source]

## Implications for our plan
- 3-5 bullets connecting findings to what we should do
```

## Self-learning
After saving, add any durable benchmark (CAC ranges, conversion norms, winning angles) to `knowledge/index.md` so future plans reuse it.
