# Built-in tools (`agent/tools/`)

A real, working tools layer the autonomous runtime calls to **actually**
research, analyze, and produce marketing work — not just describe it. Every
module is plain Python, runnable on its own (`python agent/tools/<name>.py`
runs a smoke test), and exposed to the Claude Agent SDK as in-process MCP
tools (see `agent/marketing_agent.py`).

Dependencies: `requests`, `beautifulsoup4`, `lxml`, and optionally
`feedparser` (see `agent/requirements.txt`). All are permissive-licensed.
See [`ATTRIBUTIONS.md`](../../ATTRIBUTIONS.md) for the open-source projects
whose patterns these tools build on.

| Module | Function | Input | Output | Example |
|---|---|---|---|---|
| `web_research.py` | `research(objective, max_queries=4, max_sources=6)` | a research goal (str) | dict: `queries`, `sources` (title/url/excerpt), `all_urls` | `research("cold brew DTC market size")` |
| `competitor_scan.py` | `scan(urls)` | list of competitor URLs | dict: per-URL `title`/`meta`/`h1`/`pricing_hints`/`ctas` + flat `comparison` | `scan(["https://rival.com"])` |
| `seo_audit.py` | `audit(url)` | a page URL (str) | dict: title/meta lengths, headings, word count, links, image alt coverage, `issues`, `score` | `audit("https://example.com/page")` |
| `keyword_ideas.py` | `ideas(seed, use_live=True)` | a seed keyword (str) | dict: `groups` of ideas by intent (informational/commercial/comparison/local/questions) | `ideas("cold brew subscription")` |
| `content_scorer.py` | `score(draft, keyword, target_words=800)` | draft text + target keyword | dict: `score` (0-100), `metrics` (density, Flesch, headings), `fixes` | `score(my_draft, "cold brew")` |
| `trends_monitor.py` | `monitor(topic, feeds=None, limit=10)` | a topic (str) or RSS URLs | dict: recent `items` (title/link/published/summary) | `monitor("cold brew coffee")` |

## How the agent should use them

1. **Research a market/topic** → `web_research.research(...)`, then synthesise +
   cite from `sources`/`all_urls`.
2. **Size up competitors** → `competitor_scan.scan([...])` for positioning,
   pricing, and CTAs.
3. **Check a page** → `seo_audit.audit(url)` for on-page fixes.
4. **Find topics/keywords** → `keyword_ideas.ideas(seed)` and map groups to
   funnel stages.
5. **QA a draft before publishing** → `content_scorer.score(draft, keyword)`
   and apply the returned `fixes`.
6. **Spot what's trending** → `trends_monitor.monitor(topic)`.

Always save useful findings to `knowledge/` (research → `knowledge/brands/<brand>/research.md`,
durable facts → `knowledge/index.md`). See the `autonomous-research` skill.

## Design notes

- **No API keys required.** Search uses a keyless SERP endpoint; keyword ideas
  use public autocomplete with an offline modifier fallback.
- **Graceful failure.** Network/parse errors return empty/partial results
  instead of raising, so one bad URL never aborts a run.
- **Original code.** These modules build on well-known *patterns* from
  permissively-licensed projects; no GPL/AGPL code is included.
