---
description: Run market and competitor research only - live web research grounding the brand, audience, category, and what's working now. Use when the user wants research without a full plan.
argument-hint: [market or brand]
---

# /research - Market & competitor research

You are the Marketing Agent. Research the market for: $ARGUMENTS

Steps:
1. Read `CLAUDE.md` and `knowledge/index.md`.
2. If there is no brand brief, ask only the questions needed to scope the research.
3. Load and follow `skills/market-research/SKILL.md` - search the live web; do not rely on memory. Cover market size/trends, ideal customer (pains/desires/where attention lives), category players, and what's working now. Cite every non-obvious claim.
4. If the user wants competitor depth, also load `skills/competitor-analysis/SKILL.md`.
5. Save findings to `knowledge/brands/<brand>/research.md` and append durable benchmarks to `knowledge/index.md`.
6. End with "Implications for our plan" (3-5 bullets) and "Next 3 actions."
