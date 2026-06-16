---
name: partnerships-outreach
description: Run influencer and partnership outreach that gets replies - build a target list, personalize at scale, and draft/send via Gmail while tracking everything in Airtable. Use when you want creators, affiliates, or partners to promote the brand.
---

# Skill: Partnerships & Outreach

Most outreach is ignored - ~73% of influencer partnership emails go unanswered, almost always because they are generic. This skill builds a researched target list, writes personalized outreach that earns replies, and runs it through Gmail with tracking in Airtable.

## When to use
- You want influencers, creators, affiliates, or co-marketing partners to promote the brand.
- You need a repeatable outreach pipeline, not one-off emails.

## Connected tools
- **Gmail** (`create_draft`, `search_threads`, `get_thread`, `label_thread`, `label_message`) - draft and send outreach, track replies, label by stage.
- **Airtable** (`create_records_for_table`, `list_records_for_table`, `update_records_for_table`, `search_records`) - the **Partners** target list and pipeline tracker (see `marketing-crm-setup`).

## What works (2026 benchmarks)
- **Personalized DMs** get ~32% response; generic cold email ~18%; **personalized** email 25-35%.
- **Micro-influencers (10-50k)** respond most (15-25%); response drops as size grows.
- **Short, focused** messages get 35-50% replies vs 10-15% for long ones.
- Reference a **specific recent post**, state a **clear deliverable**, and be **transparent about compensation**.
- Channel by tier: DMs for nano/micro and TikTok creators; email for macro/agency-managed. Midweek afternoons convert best.

## Procedure

1. **Define the fit.** Who is the ideal partner (audience overlap, values, size tier, platform)? Write the criteria.
2. **Build the target list** in Airtable (Partners table): name, handle, platform, size, audience fit, contact, a note about *their* recent content, status. Aim for quality over volume.
3. **Pick the channel per target** (DM vs email) by tier and platform.
4. **Write a personalized template with variable slots** - 4-6 sentences max:
   - Specific compliment referencing a recent post (proof you actually watched).
   - One-line who-we-are + why this is a fit for *their* audience.
   - The clear ask + concrete deliverable.
   - Transparent compensation (paid, gifted, affiliate %, revenue share).
   - Low-friction next step ("open to a quick chat?").
5. **Draft in Gmail** with `create_draft` (one personalized draft per target). For 1:many at scale, hand the sequence to `automation-builder`/n8n, but keep personalization real.
6. **Track & follow up.** Label threads by stage; log status in Airtable. One polite follow-up after 3-4 business days lifts replies.
7. **Save** the template + results to `knowledge/brands/<brand>/partnerships.md`.

## Output
- A scored target list in Airtable, personalized Gmail drafts ready to send, and a pipeline view (contacted -> replied -> negotiating -> live).

## Self-learning
Log response rate by channel, tier, and template variant in `knowledge/experiments/experiments-log.md`. Promote the highest-reply template and the best-fit partner profile to `knowledge/index.md`.
