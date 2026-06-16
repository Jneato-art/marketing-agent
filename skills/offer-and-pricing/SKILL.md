---
name: offer-and-pricing
description: Design the offer and price it to sell - tiers, bundles, anchoring, charm pricing, decoy, guarantees, and honest urgency. Use when conversion is weak despite good traffic, when launching, or when you need to package and price something.
---

# Skill: Offer & Pricing

People do not buy products; they buy offers. A strong offer makes the price feel like a no-brainer. This skill designs the offer (what they get) and prices it using proven behavioral levers - without resorting to dishonest pressure.

## When to use
- Traffic is fine but conversion is weak (often an offer problem, not a traffic problem).
- You are launching and need to decide what to sell, in what package, at what price.
- You want to raise average order value or reduce checkout friction.

## Inputs
- Positioning & value prop (`knowledge/brands/<brand>/messaging.md`).
- Research price benchmarks for the category (`knowledge/brands/<brand>/research.md`). If absent, run `market-research` to pull current competitor price points first.

## Procedure

1. **Define the core offer.** State the dream outcome, then stack value: the main thing + bonuses that remove specific objections (onboarding, templates, a guarantee). The goal is perceived value far above price.
2. **Choose a pricing model.** One-time, subscription, usage-based, or tiered. Match how the customer experiences value and how competitors price (don't be the lone outlier without a reason).
3. **Build 3 tiers with an anchor and a decoy.** People compare; give them something to compare against.
   - A high **anchor** tier sets the reference point and makes the middle look reasonable (anchoring lifts perceived value materially).
   - A **decoy** (slightly worse value than the target tier) nudges buyers to the tier you want to sell.
   - Make the **target tier** the visually highlighted "most popular."
4. **Apply charm pricing where it fits.** $49 / $99 reads as meaningfully cheaper than $50 / $100 for self-serve and lower tiers. Use round numbers for premium/luxury positioning where they signal quality.
5. **Bundle to raise value and AOV.** All-inclusive bundles raise perceived value and satisfaction versus a la carte. Bundle complements; never bundle in a way that hides the price of the hero item.
6. **Add a guarantee that reverses risk.** A specific, generous guarantee (e.g. "30-day, no-questions refund") near the price removes the fear of being wrong and lifts conversion. Make it concrete, not vague.
7. **Use honest urgency/scarcity only.** Real deadlines, real limited quantities, real cohort starts. Fake countdowns destroy trust and can be illegal. Genuine scarcity ("early-bird ends Friday", "12 seats") can lift conversion 20-30%.
8. **Pressure-test.** Would you buy it? Is the no-brainer obvious? What is the single biggest objection, and does the offer answer it?
9. **Save** to `knowledge/brands/<brand>/offer.md`.

## Pricing levers cheat sheet

| Lever | What it does | Use when |
|---|---|---|
| Anchor (high tier) | Raises perceived value of mid tier | You sell tiers |
| Decoy | Steers buyers to target tier | 3+ options |
| Charm pricing ($X9) | Feels cheaper | Self-serve, low/mid tier |
| Round pricing | Signals premium | Luxury positioning |
| Bundle | Raises AOV + perceived value | Complementary items |
| Guarantee | Reverses risk | Any paid offer |
| Honest urgency | Triggers action now | Real deadline/limit |

## Output format

```
# Offer & Pricing - <brand> (<date>)

## Core offer
Dream outcome: ...
Value stack: main + <bonus 1> + <bonus 2> + guarantee

## Tiers
| Tier | Price | For | Role |
|---|---|---|---|
| Basic | $X9 | ... | entry / decoy |
| Pro (highlight) | $X9 | ... | target |
| Premium | $XXX | ... | anchor |

## Guarantee
<specific risk reversal>

## Urgency (honest)
<real deadline or limit>

## Biggest objection + how the offer answers it
...
```

## Self-learning
Log price tests and their results (which price/tier/guarantee won, by how much) in `knowledge/experiments/experiments-log.md`. Promote winning offer structures to `knowledge/index.md` as durable benchmarks for the category.
