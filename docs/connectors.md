# Connectors

The agent is most powerful when connected to real marketing tools through MCP connectors. Below is what each connected tool unlocks. You do not need all of them — the agent degrades gracefully and will tell you when a connector would help.

| Tool | Category | What it unlocks for the agent |
|---|---|---|
| **Web search** | Research | Live market, audience, and competitor research — the foundation of every plan |
| **Bloom** | Creative | Brand-aware image and ad generation; pulls from a library of high-performing real ads to recreate proven formats |
| **Higgsfield** | Creative | Video, audio, and a marketing studio for short-form ad creative; can predict virality of a video |
| **Mailchimp (campaign tool)** | Lifecycle | Plan, write, and push email campaigns; pull campaign analytics and audience enrichment |
| **n8n** | Automation | Build workflows that run marketing steps automatically (lead capture, posting, reporting) |
| **Airtable** | Data / CRM | Store leads, content calendars, campaign trackers as live databases |
| **Gmail** | Outreach | Draft and send outreach, partnership, and follow-up emails |
| **Google Drive** | Storage | Read briefs and brand assets; save deliverables |
| **GitHub** | Versioning | Version the agent itself and its knowledge base (this repo) |

## How the agent chooses

- **Research** -> always start with web search.
- **Need a visual ad** -> Bloom (static) or Higgsfield (video).
- **Need to send email at scale** -> Mailchimp tool; for 1:1 outreach -> Gmail.
- **Step repeats on a schedule** -> n8n workflow or a scheduled task.
- **Need to track many records** -> Airtable.

## Adding a connector

In Claude, connect the tool from the connectors menu. Then tell the agent it is available — it will start using it where the table above applies.
