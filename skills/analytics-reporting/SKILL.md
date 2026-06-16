---
name: analytics-reporting
description: Produce clear weekly and monthly KPI reports and live dashboards that tie activity to outcomes - and automate them on a schedule. Use when the user needs to know what's working, wants a recurring report, or needs a dashboard.
---

# Skill: Analytics & Reporting

A marketing report exists to drive a decision, not to dump numbers. This skill builds weekly/monthly KPI reports and live dashboards, and automates the recurring ones so the user gets them without asking.

## When to use
- The user asks "how are we doing?" or "what's working?"
- You need a recurring (weekly/monthly) performance report.
- You want a live dashboard the user can open any time.

## Connected tools
- **Scheduled tasks** (`create_scheduled_task`, `list_scheduled_tasks`, `update_scheduled_task`) - run recurring reports automatically (e.g. every Monday 8am).
- **Airtable** (`list_records_for_table`, `search_records`, `create_records_for_table`) - read trackers (campaigns, content, experiments) and log report snapshots.
- **Cowork artifacts** (`create_artifact`, `update_artifact`, `list_artifacts`) - build a live dashboard the user can open and that you update each cycle.
- **Mailchimp** `get_analytics` for email; channel analytics via their connectors where available.

## What to report (pick KPIs that map to the goal)

| Funnel stage | Metric examples |
|---|---|
| Reach | impressions, reach, follower growth |
| Acquisition | sessions, clicks, CTR, CAC |
| Conversion | conversion rate, signups, sales, AOV |
| Retention/Revenue | repeat rate, LTV, MRR, revenue, ROAS |

Report one north-star metric + 3-5 supporting KPIs. More than that hides the signal.

## Procedure

1. **Confirm the goal & KPIs.** Tie every number to the 90-day goal from the brief. Drop vanity metrics.
2. **Pull the data.** From Airtable trackers, `get_analytics` (email), and connected channel analytics. Note the date range and source.
3. **Compare.** Show this period vs. last period vs. target. Trend > snapshot.
4. **Explain & decide.** For each KPI: what happened, why, and the recommended action. End with "Next 3 actions."
5. **Build the dashboard.** Use a Cowork artifact (`create_artifact`) for a live, visual dashboard; `update_artifact` each cycle so it stays current.
6. **Automate recurring reports.** Use `create_scheduled_task` for the weekly/monthly cadence (pull -> summarize -> deliver). For multi-app pipelines, hand off to `automation-builder` (n8n).
7. **Log a snapshot** to an Airtable Campaigns/Reports table for history.
8. **Save** the narrative to `knowledge/brands/<brand>/reports/<date>.md`.

## Report format

```
# <brand> Marketing Report - <period>

North star: <metric> = <value> (<vs last>, <vs target>)

## KPIs
| Metric | This period | Last | Target | Note |
|---|---|---|---|---|

## What's working / not
- ...

## Next 3 actions
1. ... 2. ... 3. ...
```

## Self-learning
Each report is a learning event. Append what moved and why to `knowledge/experiments/experiments-log.md`, and update durable benchmarks (your real CAC, conversion, ROAS) in `knowledge/index.md`.
