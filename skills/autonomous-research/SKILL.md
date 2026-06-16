---
name: autonomous-research
description: Use the agent's built-in tools layer (web_research, competitor_scan, seo_audit, keyword_ideas, content_scorer, trends_monitor) to actually research, analyze, and QA marketing work instead of guessing. Use whenever you need live data, a competitor read, on-page SEO checks, keyword/topic ideas, a content-quality score, or a trend pulse — and save findings to knowledge/.
---

# Skill: Autonomous Research (built-in tools)

The autonomous runtime ships with a real tools layer (`agent/tools/`) exposed to
the agent as the in-process MCP server `marketing_tools`. These tools fetch,
parse, and score real data, so prefer them over recalling facts from memory.
When running outside the SDK runtime (e.g. in Cowork), call the same modules
with `Bash` (`python agent/tools/<name>.py` runs each tool's smoke test) or use
`WebSearch`/`WebFetch` as a fallback.

## The six tools

| Tool | Call when you need to... | Returns |
|---|---|---|
| `web_research` | Research a market, audience, channel, or claim | sub-queries, scraped `sources` (title/url/excerpt), `all_urls` to cite |
| `competitor_scan` | Read how competitors position and price | per-URL title/meta/H1s/pricing/CTAs + a flat comparison |
| `seo_audit` | Check a page's on-page SEO | title/meta lengths, headings, word count, links, alt coverage, issues, score |
| `keyword_ideas` | Find topics/keywords to target | ideas grouped by intent (informational/commercial/comparison/local/questions) |
| `content_scorer` | QA a draft before publishing | 0-100 score, metrics (density, Flesch, headings), concrete fixes |
| `trends_monitor` | Spot what's trending in a category | recent feed items (title/link/published/summary) |

## When to use
- **Before any plan, positioning, or channel call** → `web_research` (then synthesise + cite).
- **During competitor work** → `competitor_scan` (feeds `competitor-analysis`).
- **When briefing or fixing a page** → `seo_audit`.
- **When planning content/SEO** → `keyword_ideas` (map groups to funnel stages).
- **Before shipping any written asset** → `content_scorer`, then apply the fixes.
- **For a weekly pulse or launch timing** → `trends_monitor`.

## Procedure

1. **Pick the tool** that matches the question (table above). Use more than one
   when needed (e.g. `web_research` + `competitor_scan` for a category read).
2. **Call it** with the smallest useful input (an objective, a few URLs, a seed,
   a draft, or a topic).
3. **Read the structured result**, not just the prose. Pull the concrete numbers
   (scores, counts, prices) and the source URLs.
4. **Synthesise** in your own words and **cite** every non-obvious claim with a
   URL from `all_urls`/`sources`.
5. **Act on the output**: apply `content_scorer` fixes, turn `keyword_ideas`
   groups into a content plan, turn `competitor_scan` gaps into positioning.
6. **Save findings** to `knowledge/`:
   - market/competitor research → `knowledge/brands/<brand>/research.md`
   - durable benchmarks/angles → `knowledge/index.md`
   - what you ran + what you learned → `knowledge/experiments/experiments-log.md`

## Output format

```
# Research — <topic/brand> (<date>)

## Method
- Tools used: web_research, competitor_scan, ... (inputs)

## Findings
- <claim> [source url]
- Competitor read: <name> positions as ..., priced at ... [url]
- SEO: page scores X/100; top fixes: ...
- Keyword groups worth targeting: ...
- Trend pulse: ...

## Implications
- 3-5 bullets connecting findings to what we should do next
```

## Self-learning
After saving, add any durable benchmark (CAC ranges, winning angles, content
score baselines, competitor prices) to `knowledge/index.md` so the next run
starts smarter. Log the tool run in `knowledge/experiments/experiments-log.md`.
