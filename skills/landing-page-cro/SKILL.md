---
name: landing-page-cro
description: Structure a high-converting landing page and run a disciplined conversion-rate-optimization (CRO) program - what each section must do, and what to test in priority order. Use when building or fixing a landing/sales page, or when traffic converts poorly.
---

# Skill: Landing Page & CRO

A landing page has one job: convert a specific visitor to a single action. This skill gives the section-by-section structure that converts in 2026, then a testing program so the page keeps getting better.

## When to use
- Building a new landing, sales, or signup page.
- A page gets traffic but converts poorly.
- You want a prioritized A/B test backlog instead of random tweaks.

## Inputs
- Positioning, value prop, message hierarchy (`messaging.md`) and the offer (`offer.md`). Do not write a page without these.

## Page structure (top to bottom)

1. **Hero (above the fold)** - decided in 3-5 seconds. Show product value fast (story-driven hero beats a static tagline). Include: outcome headline, supporting subhead, primary CTA, and a visual that demonstrates the product. One goal, one primary CTA.
2. **Social proof early** - logos, a star rating, or one strong testimonial right under the hero. Proof placement can lift conversion meaningfully; trust is highest from real people and named customers.
3. **Problem / before-after** - name the pain, then paint the after-state (pull from `messaging.md`).
4. **How it works** - 3 simple steps so the path feels easy.
5. **Benefits as pillars** - the 3 messaging pillars, each with proof. Benefits first, features in support.
6. **Deeper social proof** - testimonials, case numbers, UGC, before/after results.
7. **Offer + pricing** - the offer from `offer-and-pricing`, with the guarantee beside the price and honest urgency if real.
8. **Objection handling / FAQ** - answer the top 5 reasons people hesitate.
9. **Final CTA** - repeat the single CTA; restate the core promise. Use the same CTA throughout (hero, mid-page, end).

Rules: one goal per page, remove navigation/distractions, mobile-first (most traffic and most friction is mobile), and fast load (speed is a top conversion variable).

## CRO testing program

High-impact variables, in roughly the order that moves the needle most:

| Priority | Test | Why |
|---|---|---|
| 1 | Form length / fields | Reducing fields is the single largest lift in most tests |
| 2 | Headline clarity | Headline changes routinely lift conversion 25-100% |
| 3 | Mobile friction | Most visitors, most drop-off |
| 4 | Page speed | Slow pages bleed conversions |
| 5 | Proof placement | Moving/adding proof lifts 15-30% |
| 6 | CTA copy/color/position | Cheap to test, can compound |
| 7 | Offer / pricing presentation | Often the real lever |

Testing discipline:
- Test **one variable at a time**; change the thing you have a hypothesis about.
- Write a hypothesis: "Because [evidence], changing [X] will [effect] measured by [metric]."
- Run to **statistical significance** - typically 2+ full business cycles and an adequate sample. Expect only ~1 in 8 tests to win; that is normal.
- Run **2-3 tests/month** for compounding gains, not one big swing.
- Connect to `growth-experiments` to log each test in the ICE-scored backlog.

## Output
- A complete page wireframe (section-by-section copy + layout notes), and
- A prioritized A/B test backlog (hypothesis, variable, metric, expected sample) handed to `growth-experiments`.

## Self-learning
After each test concludes, record winner, lift, and confidence in `knowledge/experiments/experiments-log.md`. Promote repeatable winners (e.g. "short form beats long form for this audience") to `knowledge/index.md`.
