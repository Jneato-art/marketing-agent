---
name: email-lifecycle
description: Design and ship lifecycle email automation - welcome, nurture, abandoned-cart/browse, post-purchase, and win-back sequences - and push them live through the connected Mailchimp campaign tool. Use when setting up or improving automated email flows.
---

# Skill: Email Lifecycle

Lifecycle (triggered) emails are the highest-ROI marketing most brands neglect. Automated flows like welcome and abandoned-cart routinely beat one-off promos several times over. This skill designs the core flows and ships them using the connected Mailchimp campaign tool.

## When to use
- A brand has list signups or a store but no automated flows.
- Existing flows underperform (low open/click/revenue-per-recipient).
- After a launch, to convert and retain the people you just acquired.

## Connected tool (Mailchimp campaign tool)
Use these tools - call them by name:
- `campaign_planner` - plan a campaign/flow (audience, goal, structure).
- `edit_campaign` - draft and revise subject lines and body copy.
- `save_to_mailchimp` - push the finished campaign live to Mailchimp.
- `get_analytics` - pull open/click/revenue performance to measure and iterate.
- `set_active_campaign` / `get_campaign_content` / `get_enrichment` - manage the working campaign and enrich audience data.

Workflow: plan with `campaign_planner` -> draft with `edit_campaign` -> ship with `save_to_mailchimp` -> measure with `get_analytics` -> iterate.

## The core flows every brand should have

| Flow | Trigger | Goal | Typical structure |
|---|---|---|---|
| Welcome | New subscriber | Deliver promise, first purchase | 3-5 emails over ~7 days: welcome + brand story + best content/offer |
| Nurture | No purchase yet | Educate, build trust | Weekly value emails tied to messaging pillars |
| Abandoned cart | Cart, no checkout | Recover the sale | 3 emails: reminder (1h) -> objection/benefit (24h) -> incentive (48-72h) |
| Browse abandon | Viewed, no cart | Bring them back | 1-2 emails featuring viewed items |
| Post-purchase | Order placed | Onboard, reduce returns, cross-sell | thank-you -> how-to-use -> review request -> cross-sell |
| Win-back | Lapsed buyer | Re-activate | segment by recency; "we miss you" + reason to return + offer |

Benchmarks to aim at (2026): welcome opens ~42-50%+, abandoned-cart opens ~45-50% with strong revenue-per-recipient. Win-back works far better when segmented by last-purchase recency than as a blast.

## Procedure

1. **Pick the flows** that match the brand's stage and goal (start with welcome + abandoned-cart for ecommerce; welcome + nurture for SaaS/services).
2. **Map each flow**: trigger, number of emails, timing, one goal per email, and the CTA.
3. **Write the copy** grounded in `messaging.md` and `offer.md`. Subject line = the open; first line = the click. One idea per email.
4. **Build in Mailchimp**: `campaign_planner` to structure, `edit_campaign` to draft each email, `save_to_mailchimp` to ship.
5. **Segment** by behavior/recency (especially win-back) using audience enrichment.
6. **Measure & iterate** with `get_analytics`; A/B test subject lines and the incentive email.
7. **Save** the flow specs and results to `knowledge/brands/<brand>/email-flows.md`.

## Output
Live, named flows in Mailchimp plus a one-page spec per flow (trigger, emails, timing, goals) and the first analytics readout.

## Self-learning
Log which subject lines, send times, and incentives win in `knowledge/experiments/experiments-log.md`. Promote durable winners (best welcome subject, best cart-recovery offer) to `knowledge/index.md`.
