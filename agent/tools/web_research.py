"""
web_research — multi-query web research that returns a structured digest.

Implements the GPT-Researcher-style loop in clean, original code:

    plan  -> derive several focused sub-queries from the objective
    search-> run each query against a keyless SERP (DuckDuckGo HTML endpoint)
    scrape-> fetch the top results and extract their main text (_http.py)
    digest-> assemble per-source summaries + a deduped source list

It returns structured data (not prose) so the calling agent can synthesise the
final report itself and cite sources. No API key required.

Build-off note: the plan/search/scrape/synthesize architecture follows GPT
Researcher (assafelovic/gpt-researcher, Apache-2.0). Code here is original.
See ATTRIBUTIONS.md.
"""

from __future__ import annotations

import re
from html import unescape
from urllib.parse import quote_plus, urlparse, parse_qs, unquote
from typing import Any, Dict, List, Optional

import requests

try:
    from ._http import fetch_html, extract_main_text, make_soup, DEFAULT_HEADERS, clean_text
except ImportError:
    from _http import fetch_html, extract_main_text, make_soup, DEFAULT_HEADERS, clean_text

_DDG_HTML = "https://html.duckduckgo.com/html/"

# Angle modifiers used to fan a single objective into several sub-queries.
_ANGLES = [
    "{q}",
    "{q} statistics 2026",
    "{q} best practices",
    "{q} trends",
    "{q} examples",
]


def plan_queries(objective: str, max_queries: int = 4) -> List[str]:
    """Turn an objective into a small set of focused sub-queries."""
    objective = objective.strip()
    queries = [a.format(q=objective) for a in _ANGLES]
    # dedupe preserving order, cap to max_queries
    seen, out = set(), []
    for q in queries:
        if q.lower() not in seen:
            seen.add(q.lower())
            out.append(q)
        if len(out) >= max_queries:
            break
    return out


def _clean_ddg_link(href: str) -> str:
    """DuckDuckGo HTML wraps targets in /l/?uddg=<url>; unwrap to the real URL."""
    if href.startswith("//"):
        href = "https:" + href
    parsed = urlparse(href)
    if "duckduckgo.com" in parsed.netloc and parsed.path.startswith("/l/"):
        qs = parse_qs(parsed.query)
        if "uddg" in qs:
            return unquote(qs["uddg"][0])
    return href


def search(query: str, max_results: int = 5, timeout: int = 12) -> List[Dict[str, str]]:
    """Run a keyless web search; return [{title, url, snippet}]. [] on failure."""
    try:
        resp = requests.post(
            _DDG_HTML,
            data={"q": query},
            headers=DEFAULT_HEADERS,
            timeout=timeout,
        )
        resp.raise_for_status()
        return parse_serp(resp.text, max_results)
    except Exception:
        return []


def parse_serp(html: str, max_results: int = 5) -> List[Dict[str, str]]:
    """Parse a DuckDuckGo HTML results page into result dicts."""
    soup = make_soup(html)
    results: List[Dict[str, str]] = []
    for res in soup.select(".result, .web-result"):
        a = res.select_one("a.result__a")
        if not a:
            continue
        url = _clean_ddg_link(a.get("href", ""))
        title = a.get_text(" ", strip=True)
        snip_el = res.select_one(".result__snippet")
        snippet = snip_el.get_text(" ", strip=True) if snip_el else ""
        if url and title:
            results.append({"title": title, "url": url,
                            "snippet": unescape(snippet)})
        if len(results) >= max_results:
            break
    return results


def research(objective: str, max_queries: int = 4,
             results_per_query: int = 4, max_sources: int = 6,
             scrape_chars: int = 2500) -> Dict[str, Any]:
    """Run the full plan -> search -> scrape -> digest loop.

    Args:
        objective: the research goal in plain language.
        max_queries: how many sub-queries to plan.
        results_per_query: SERP results to collect per query.
        max_sources: max distinct pages to actually scrape.
        scrape_chars: chars of main text to keep per source.

    Returns:
        dict with 'objective', 'queries', 'sources' (each with title/url/
        excerpt), and 'all_urls' for citation.
    """
    queries = plan_queries(objective, max_queries)

    # Collect + dedupe results across queries by URL.
    seen_urls: set = set()
    candidates: List[Dict[str, str]] = []
    for q in queries:
        for r in search(q, results_per_query):
            if r["url"] not in seen_urls:
                seen_urls.add(r["url"])
                candidates.append(r)

    sources: List[Dict[str, Any]] = []
    for c in candidates[:max_sources]:
        html = fetch_html(c["url"])
        excerpt = (extract_main_text(html, scrape_chars) if html
                   else c.get("snippet", ""))
        sources.append({
            "title": c["title"],
            "url": c["url"],
            "excerpt": excerpt or c.get("snippet", ""),
        })

    return {
        "objective": objective,
        "queries": queries,
        "source_count": len(sources),
        "sources": sources,
        "all_urls": [s["url"] for s in sources],
    }


if __name__ == "__main__":
    # 1) Query planning (offline, deterministic):
    qs = plan_queries("cold brew coffee subscription growth", max_queries=4)
    assert len(qs) == 4 and qs[0] == "cold brew coffee subscription growth"
    print("OK plan_queries ->", qs)

    # 2) SERP parsing against a local fixture (no network):
    fixture = """<html><body>
      <div class="result"><a class="result__a" href="//duckduckgo.com/l/?uddg=https%3A%2F%2Fexample.test%2Fa">Cold brew market report</a>
        <div class="result__snippet">The cold brew category grew sharply this year.</div></div>
      <div class="result"><a class="result__a" href="https://example.test/b">DTC coffee subscription tips</a>
        <div class="result__snippet">How subscription brands retain customers.</div></div>
    </body></html>"""
    parsed = parse_serp(fixture, 5)
    assert len(parsed) == 2, parsed
    assert parsed[0]["url"] == "https://example.test/a", parsed[0]["url"]
    print("OK parse_serp + link-unwrap ->", [r["url"] for r in parsed])
    print("   first:", parsed[0])
