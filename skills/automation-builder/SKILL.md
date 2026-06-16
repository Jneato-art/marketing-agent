---
name: automation-builder
description: Turn a recurring marketing step into an automation - an n8n workflow, a scheduled task, or an email/CRM sequence. Use when a step repeats and should not be done by hand each time.
---

# Skill: Automation Builder

## When to use
When a marketing step repeats (weekly report, new-lead follow-up, content posting, review requests). If you'd do it more than ~3 times, automate it.

## Decide the tool

| Pattern | Build it with |
|---|---|
| Multi-app workflow (trigger -> action across tools) | n8n workflow |
| "Do X every day/week at a time" inside Claude | scheduled task |
| Email nurture / drip | Mailchimp campaign tool |
| Lead/record tracking | Airtable base + automations |

## Procedure (n8n example)

1. **Map the flow** in one sentence: "When [trigger], do [steps], ending in [outcome]."
2. Follow the n8n build order: read the SDK reference, get suggested nodes, search nodes, get node types, write workflow code, validate, then create.
3. **Test** with sample data before publishing.
4. **Hand off**: tell the user what it does, when it runs, and how to turn it off.

## Common marketing automations to offer
- Weekly performance report: pull analytics -> summarize -> email/Slack the user.
- New lead -> add to CRM -> send welcome email -> notify owner.
- Publish content -> cross-post to channels -> log to calendar.
- Post-purchase -> request review after N days -> tag happy customers for referral.
- Abandoned interest -> re-engagement email sequence.

## Output
A working, tested automation plus a one-paragraph plain-English description of what it does and its kill switch.

## Self-learning
Log each automation built (what, where, impact) so the agent can reuse and improve the pattern for the next brand.
