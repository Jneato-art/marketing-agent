---
description: Produce a performance report - KPIs vs target, what's working, and next actions. Use when the user asks how marketing is doing or wants a recurring report.
argument-hint: [period, e.g. last week / last month]
disable-model-invocation: false
---

# /report - Performance report

You are the Marketing Agent. Produce a marketing performance report for: $ARGUMENTS

Steps:
1. Read `CLAUDE.md` and `knowledge/index.md`.
2. Load and follow `skills/analytics-reporting/SKILL.md`.
3. Pull data: Airtable trackers (`list_records_for_table`), email via Mailchimp `get_analytics`, and connected channel analytics. Note date range and sources.
4. Report one north-star metric + 3-5 supporting KPIs, each shown vs last period and vs target. For each: what happened, why, recommended action.
5. If asked for a live dashboard, build a Cowork artifact (`create_artifact`). If asked to make it recurring, set a scheduled task (`create_scheduled_task`).
6. Log a snapshot to Airtable and save the narrative to `knowledge/brands/<brand>/reports/<date>.md`.
7. End with "Next 3 actions."
