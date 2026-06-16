"""
marketing-agent built-in tools layer.

Six runnable modules the autonomous agent can call to actually research,
analyze, and produce marketing work (not just describe it):

  web_research     - multi-query web research -> structured digest
  competitor_scan  - extract positioning signals from competitor URLs
  seo_audit        - on-page SEO basics for a single page
  keyword_ideas    - expand a seed term into grouped keyword/topic ideas
  content_scorer   - score a draft vs a target keyword + readability
  trends_monitor   - pull recent items for a topic from RSS/news feeds

See ATTRIBUTIONS.md (repo root) for the open-source projects whose patterns
these modules build on. All code here is original and permissively usable.
"""

__all__ = [
    "web_research",
    "competitor_scan",
    "seo_audit",
    "keyword_ideas",
    "content_scorer",
    "trends_monitor",
]
