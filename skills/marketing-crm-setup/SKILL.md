---
name: marketing-crm-setup
description: Stand up a complete "Marketing OS" in Airtable - Leads, Content Calendar, Experiments, Campaigns, and Partners tables - and wire n8n automations that write into it. Use when a brand needs a single source of truth for marketing operations.
---

# Skill: Marketing CRM Setup (Marketing OS)

A marketing operation without a single source of truth runs on memory and spreadsheets. This skill builds a "Marketing OS" in Airtable - the core tables every brand needs - and connects automations so data flows in by itself.

## When to use
- A brand has no central place to track leads, content, experiments, campaigns, or partners.
- Other skills (`growth-experiments`, `partnerships-outreach`, `analytics-reporting`, `content-calendar`) need a database to read/write.
- Set this up early; the other skills plug into it.

## Connected tools
- **Airtable** (`create_base`, `create_table`, `create_field`, `update_field`, `create_records_for_table`, `list_tables_for_base`, `get_table_schema`) - build the base and tables.
- **n8n** (via `automation-builder`) - workflows that write into the base (new lead -> Leads, published post -> Content Calendar, weekly metrics -> Campaigns).

## The Marketing OS schema

Create one base ("<brand> Marketing OS") with these tables:

**Leads**
| Field | Type |
|---|---|
| Name | single line |
| Email | email |
| Source | single select (ad, organic, referral, partner) |
| Stage | single select (new, contacted, qualified, customer) |
| Date added | date |
| Owner | single line |
| Notes | long text |

**Content Calendar**
| Field | Type |
|---|---|
| Title | single line |
| Channel | single select (blog, IG, TikTok, email, YouTube) |
| Status | single select (idea, drafting, scheduled, published) |
| Publish date | date |
| Owner | single line |
| Link/Asset | url |
| Pillar | single select (the messaging pillars) |

**Experiments** (used by `growth-experiments`)
| Field | Type |
|---|---|
| Hypothesis | long text |
| Metric | single line |
| Impact | number | 
| Confidence | number |
| Ease | number |
| ICE score | formula (Impact * Confidence * Ease) |
| Status | single select (backlog, running, won, lost, inconclusive) |
| Result | long text |

**Campaigns**
| Field | Type |
|---|---|
| Name | single line |
| Channel | single select |
| Goal/KPI | single line |
| Budget | currency |
| Start / End | date |
| Status | single select (planned, live, done) |
| Result | long text |

**Partners** (used by `partnerships-outreach`)
| Field | Type |
|---|---|
| Name | single line |
| Handle | single line |
| Platform | single select |
| Size/Tier | single select (nano, micro, macro, mega) |
| Audience fit | single select (high, med, low) |
| Contact | single line |
| Status | single select (target, contacted, replied, negotiating, live, declined) |
| Notes | long text |

## Procedure

1. **Create the base** with `create_base` ("<brand> Marketing OS").
2. **Create each table** with `create_table`, then add fields with `create_field` per the schema above. Use `get_table_schema` to confirm single-select choice IDs before writing records.
3. **Seed** with any existing leads/content/partners via `create_records_for_table`.
4. **Wire automations** (hand to `automation-builder`/n8n): form submission -> Leads; published content -> Content Calendar; weekly analytics -> Campaigns. Lead capture and review-request flows are good first builds.
5. **Connect the other skills**: point `growth-experiments` at Experiments, `partnerships-outreach` at Partners, `analytics-reporting` at Campaigns, `content-calendar` at Content Calendar.
6. **Document** the base ID and table IDs in `knowledge/brands/<brand>/marketing-os.md`.

## Output
- A live Airtable base with five tables, seeded data, and at least one automation writing into it - the operating system the rest of the agent reads and writes.

## Self-learning
The Experiments and Campaigns tables are the structured backing store for the self-learning loop. After each cycle, ensure results are recorded there and mirror durable wins into `knowledge/index.md`.
