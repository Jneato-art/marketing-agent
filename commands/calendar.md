---
description: Build a 30-day content calendar mapped to channels, messaging pillars, and publish dates. Use when the user wants a publishing schedule.
argument-hint: [brand or channel focus]
---

# /calendar - 30-day content calendar

You are the Marketing Agent. Build a 30-day content calendar for: $ARGUMENTS

Steps:
1. Read `CLAUDE.md` and `knowledge/index.md`.
2. Pull positioning/pillars from `knowledge/brands/<brand>/messaging.md` (run `skills/positioning-messaging` first if missing).
3. Load and follow `skills/content-calendar/SKILL.md`. Map each piece to a channel, a messaging pillar, a format, and a publish date. Balance the channel mix; reuse winning formats from `knowledge/index.md`.
4. For short-form video slots, note hook angles (see `skills/short-form-video`); for email slots, tie to flows (`skills/email-lifecycle`).
5. If Airtable is connected, offer to write the calendar into the Content Calendar table (`skills/marketing-crm-setup`).
6. Output the 30-day calendar as a table (date, channel, title, pillar, format, owner, status) and end with "Next 3 actions."
