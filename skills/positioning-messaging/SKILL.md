---
name: positioning-messaging
description: Build a brand's positioning statement, value proposition, and a full message hierarchy (promise -> pillars -> proof) plus before/after framing. Use when copy feels generic, when launching something new, or when nobody can say in one sentence why this product beats the alternative.
---

# Skill: Positioning & Messaging

Great marketing starts with one decision: what do we stand for in the customer's mind, and why us over the alternative? Positioning is that decision; messaging is how you say it everywhere. This skill produces both, in a hierarchy you can reuse across the site, ads, email, and sales.

## When to use
- Copy across channels feels generic or inconsistent.
- You are launching a new product, feature, or entering a new segment.
- The team cannot agree on the one-sentence reason to buy.
- Run this before `landing-page-cro`, `email-lifecycle`, `ad-creative-brief`, or any copy work.

## Inputs
- Brand brief (`knowledge/brands/<brand>/brief.md`) and research (`knowledge/brands/<brand>/research.md`). If missing, run intake + `market-research` first.
- The competitor set (from `competitor-analysis`) so you can differentiate, not echo.

## Key distinction (do not blur these)
- **Positioning** = how the brand is *different* from alternatives, for a *specific* buyer. It guides choices.
- **Value proposition** = the *outcome and benefits* the customer gets. It is the promise.
- **Messaging** = the words that carry the value prop across every surface, organized by hierarchy.

## Procedure

1. **Write the positioning statement.** Use this template and fill every slot from research, not guesswork:
   > For [target customer] who [need/struggle], [brand] is the [category] that [key differentiated benefit]. Unlike [primary alternative], we [the one thing only we do].
2. **Write the value proposition.** One outcome-focused headline a 12-year-old understands, plus a 1-2 sentence subhead naming the benefit and who it is for. Avoid jargon and feature-speak.
3. **Build the message hierarchy** (big promise -> 3 pillars -> proof):
   - **Promise**: the value prop, restated as the top-line claim.
   - **3 messaging pillars**: the 3 themes that prove the promise (e.g. faster, cheaper, safer). Each pillar is a benefit, not a feature.
   - **Proof points** under each pillar: specific evidence (numbers, demos, testimonials, certifications, guarantees). No proof = cut the claim.
4. **Map before/after framing.** State the customer's world *before* (the pain, the bad status quo) and *after* (the new reality with the product). The gap between them is the value you sell.
5. **Differentiate explicitly.** Name the primary alternative and write the one sentence that makes you the obvious choice over it. If you cannot, the positioning is not sharp enough — go back to step 1.
6. **Voice & tone, briefly.** 3 adjectives + 3 words/phrases to use + 3 to avoid, so every writer sounds like the brand.
7. **Save.** Write to `knowledge/brands/<brand>/messaging.md` using the output format.

## Output format

```
# Positioning & Messaging - <brand> (<date>)

## Positioning statement
For <customer> who <need>, <brand> is the <category> that <benefit>. Unlike <alternative>, we <only-we>.

## Value proposition
Headline: <one outcome line>
Subhead: <benefit + who it's for>

## Message hierarchy
Promise: <top-line claim>
- Pillar 1: <benefit> | Proof: <evidence>
- Pillar 2: <benefit> | Proof: <evidence>
- Pillar 3: <benefit> | Proof: <evidence>

## Before / After
Before: <painful status quo>
After: <new reality with product>

## Differentiation
Primary alternative: <name>. Why us: <one sentence>.

## Voice
Tone: <3 adjectives>. Use: <words>. Avoid: <words>.
```

## Self-learning
When a message angle clearly outperforms in market (high CTR, replies, sales), record the winning angle and the losing one in `knowledge/index.md` so future positioning starts from what already converts for this audience.
