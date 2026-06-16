"""
competitor_scan — extract positioning signals from competitor pages.

Given one or more competitor URLs, fetch each page and pull the signals that
reveal how they position and sell: title, meta description, H1s, candidate
taglines, pricing hints (anything that looks like a price), and calls-to-action
(button/link text that reads like a CTA). Returns a per-URL breakdown plus a
flat comparison table for easy side-by-side reading.

Build-off note: a clean-room scraper using the readability-style extraction in
_http.py. All code original. See ATTRIBUTIONS.md.
"""

from __future__ import annotations

import re
from typing import Any, Dict, List, Optional

try:
    from ._http import fetch_html, make_soup
except ImportError:
    from _http import fetch_html, make_soup

# $1,299 / £49.99 / €19 / 29.00 USD -- broad price-like matcher.
_PRICE_RE = re.compile(
    r"(?:[$£€]\s?\d[\d,]*(?:\.\d{2})?|\b\d[\d,]*(?:\.\d{2})?\s?(?:USD|EUR|GBP)\b)"
)
_CTA_WORDS = (
    "buy", "shop", "subscribe", "sign up", "signup", "start", "get started",
    "try", "free trial", "book", "demo", "download", "join", "order",
    "add to cart", "learn more", "contact",
)


def _ctas(soup) -> List[str]:
    """Collect short CTA-like button/link texts (deduped, capped)."""
    found: List[str] = []
    for el in soup.find_all(["a", "button"]):
        txt = el.get_text(" ", strip=True)
        if not txt or len(txt) > 40:
            continue
        low = txt.lower()
        if any(w in low for w in _CTA_WORDS):
            if txt not in found:
                found.append(txt)
    return found[:10]


def _prices(html: str) -> List[str]:
    seen, out = set(), []
    for m in _PRICE_RE.findall(html):
        m = m.strip()
        if m not in seen:
            seen.add(m)
            out.append(m)
    return out[:10]


def scan_one(url: str, html: Optional[str] = None) -> Dict[str, Any]:
    """Scan a single competitor URL for positioning signals."""
    if html is None:
        html = fetch_html(url)
    if not html:
        return {"url": url, "fetched": False}

    soup = make_soup(html)
    title = (soup.title.get_text(strip=True) if soup.title else "") or ""
    meta_tag = soup.find("meta", attrs={"name": "description"})
    meta_desc = meta_tag.get("content", "").strip() if meta_tag else ""
    h1s = [h.get_text(strip=True) for h in soup.find_all("h1")][:5]
    h2s = [h.get_text(strip=True) for h in soup.find_all("h2")][:8]

    return {
        "url": url,
        "fetched": True,
        "title": title,
        "meta_description": meta_desc,
        "h1": h1s,
        "subheads": h2s,
        "pricing_hints": _prices(html),
        "ctas": _ctas(soup),
    }


def scan(urls: List[str]) -> Dict[str, Any]:
    """Scan several competitor URLs and build a comparison structure.

    Returns:
        dict with 'competitors' (list of per-URL signal dicts) and
        'comparison' (flat rows for side-by-side reading).
    """
    results = [scan_one(u) for u in urls]
    comparison = []
    for r in results:
        if not r.get("fetched"):
            comparison.append({"url": r["url"], "status": "fetch-failed"})
            continue
        comparison.append({
            "url": r["url"],
            "headline": (r["h1"][0] if r["h1"] else r["title"])[:120],
            "promise": r["meta_description"][:160],
            "top_price": r["pricing_hints"][0] if r["pricing_hints"] else "—",
            "primary_cta": r["ctas"][0] if r["ctas"] else "—",
        })
    return {"competitors": results, "comparison": comparison}


if __name__ == "__main__":
    a = """<html><head><title>RivalBrew — Cold Brew Delivered</title>
    <meta name="description" content="Premium cold brew on subscription. Cancel anytime."></head>
    <body><h1>Cold brew, on your schedule</h1><h2>Plans</h2>
    <p>From $19.99/mo.</p><a class="btn">Start your subscription</a>
    <button>Learn more</button></body></html>"""
    b = """<html><head><title>BeanBox</title></head>
    <body><h1>Roasts you'll love</h1><p>Bags from £12.50</p>
    <a>Shop now</a></body></html>"""
    out = scan(["https://rivalbrew.test", "https://beanbox.test"])
    # inject fixtures (no network in this env) to exercise scan_one fully
    out2 = {"competitors": [scan_one("https://rivalbrew.test", a),
                            scan_one("https://beanbox.test", b)]}
    assert out2["competitors"][0]["pricing_hints"] == ["$19.99"], out2["competitors"][0]["pricing_hints"]
    assert "Start your subscription" in out2["competitors"][0]["ctas"]
    print("OK competitor_scan")
    for c in out2["competitors"]:
        print(" ", c["url"], "| price:", c["pricing_hints"], "| cta:", c["ctas"][:2])
