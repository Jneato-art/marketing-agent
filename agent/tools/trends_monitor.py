"""
trends_monitor — pull recent items for a topic from RSS / news feeds.

Given a topic (or explicit feed URLs), fetch and parse RSS/Atom feeds and
return the most recent items (title, link, published date, summary) so the
agent can spot what is trending in a category. By default it builds a Google
News RSS query URL for the topic; you can also pass your own feeds.

Uses `feedparser` (BSD) when available. If feedparser is not installed, it
falls back to a minimal built-in RSS/Atom parser (BeautifulSoup) so the tool
still works. See ATTRIBUTIONS.md.
"""

from __future__ import annotations

from urllib.parse import quote_plus
from typing import Any, Dict, List, Optional

try:
    from ._http import fetch_html, make_soup
except ImportError:
    from _http import fetch_html, make_soup

from bs4 import BeautifulSoup


def _xml_soup(xml: str) -> BeautifulSoup:
    """Parse a feed as XML (preferred), falling back to the HTML parser."""
    try:
        return BeautifulSoup(xml, "xml")
    except Exception:
        return make_soup(xml)

try:
    import feedparser  # type: ignore
    _HAVE_FEEDPARSER = True
except Exception:
    _HAVE_FEEDPARSER = False


def google_news_feed(topic: str) -> str:
    """Build a Google News RSS URL for a topic query."""
    return ("https://news.google.com/rss/search?q="
            f"{quote_plus(topic)}&hl=en-US&gl=US&ceid=US:en")


def _parse_with_feedparser(xml: str, limit: int) -> List[Dict[str, str]]:
    parsed = feedparser.parse(xml)
    items = []
    for e in parsed.entries[:limit]:
        items.append({
            "title": getattr(e, "title", "").strip(),
            "link": getattr(e, "link", "").strip(),
            "published": getattr(e, "published", getattr(e, "updated", "")),
            "summary": (getattr(e, "summary", "") or "")[:300],
        })
    return items


def _parse_fallback(xml: str, limit: int) -> List[Dict[str, str]]:
    """Minimal RSS/Atom parser used when feedparser isn't installed."""
    soup = _xml_soup(xml)
    items = []
    entries = soup.find_all("item") or soup.find_all("entry")

    def _first(node, *names):
        for n in names:
            found = node.find(lambda t: t.name and t.name.lower() == n)
            if found:
                return found
        return None

    for e in entries[:limit]:
        title = _first(e, "title")
        link = _first(e, "link")
        link_val = ""
        if link:
            link_val = link.get("href") or link.get_text(strip=True)
        date = _first(e, "pubdate", "published", "updated", "date")
        summary = _first(e, "description", "summary", "content")
        items.append({
            "title": title.get_text(strip=True) if title else "",
            "link": link_val.strip(),
            "published": date.get_text(strip=True) if date else "",
            "summary": (summary.get_text(strip=True) if summary else "")[:300],
        })
    return items


def monitor(topic: str, feeds: Optional[List[str]] = None,
            limit: int = 10) -> Dict[str, Any]:
    """Fetch recent items for a topic.

    Args:
        topic: subject to monitor (used to build a Google News feed if no
            feeds are supplied; also echoed in the result).
        feeds: optional explicit list of RSS/Atom feed URLs.
        limit: max items per feed.

    Returns:
        dict with 'topic', 'parser' used, 'feeds', and 'items' (merged,
        most-recent-first as provided by the feeds).
    """
    feed_urls = feeds or [google_news_feed(topic)]
    parser = "feedparser" if _HAVE_FEEDPARSER else "builtin-fallback"
    items: List[Dict[str, str]] = []
    for url in feed_urls:
        xml = fetch_html(url)
        if not xml:
            continue
        try:
            chunk = (_parse_with_feedparser(xml, limit) if _HAVE_FEEDPARSER
                     else _parse_fallback(xml, limit))
            items.extend(chunk)
        except Exception:
            continue
    return {"topic": topic, "parser": parser, "feeds": feed_urls,
            "count": len(items), "items": items[: limit * len(feed_urls)]}


if __name__ == "__main__":
    # Build URL works offline:
    u = google_news_feed("cold brew coffee")
    assert "news.google.com" in u and "cold" in u
    print("OK trends_monitor feed URL:", u[:70], "...")

    # Parse a local RSS fixture (no network) to exercise the parser path:
    fixture = """<?xml version="1.0"?><rss version="2.0"><channel>
      <item><title>Cold brew sales surge 30% in Q2</title>
        <link>https://example.test/a</link>
        <pubDate>Mon, 15 Jun 2026 09:00:00 GMT</pubDate>
        <description>Demand for ready-to-drink cold brew keeps climbing.</description></item>
      <item><title>New low-acid cold brew launches</title>
        <link>https://example.test/b</link>
        <pubDate>Sun, 14 Jun 2026 12:00:00 GMT</pubDate>
        <description>A startup debuts a smoother cold brew line.</description></item>
    </channel></rss>"""
    parsed = (_parse_with_feedparser(fixture, 10) if _HAVE_FEEDPARSER
              else _parse_fallback(fixture, 10))
    assert len(parsed) == 2 and parsed[0]["title"].startswith("Cold brew sales"), parsed
    print("OK trends_monitor parser=", "feedparser" if _HAVE_FEEDPARSER else "builtin-fallback",
          "parsed", len(parsed), "items")
    print("   ", parsed[0])
