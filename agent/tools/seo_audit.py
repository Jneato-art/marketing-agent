"""
seo_audit — on-page SEO basics for a single web page.

Fetches a URL (or accepts raw HTML) and reports the on-page fundamentals an
SEO would check first: title, meta description, heading hierarchy, word
count, internal/external link counts, and image alt-text coverage. Returns a
structured dict plus a list of concrete issues.

Build-off note: the set of on-page checks mirrors the conventions used by
permissively-licensed SEO crawlers/auditors; all code here is original.
See ATTRIBUTIONS.md.
"""

from __future__ import annotations

from urllib.parse import urlparse
from typing import Any, Dict, List, Optional

try:
    from ._http import fetch_html, make_soup, word_count, extract_main_text
except ImportError:  # allow running as a standalone script
    from _http import fetch_html, make_soup, word_count, extract_main_text

# Common on-page SEO guidance (pixel-equivalent character ranges).
TITLE_MIN, TITLE_MAX = 30, 60
META_MIN, META_MAX = 70, 160


def _same_domain(base: str, href: str) -> Optional[bool]:
    """True if href is internal, False if external, None if not a real link."""
    if not href or href.startswith(("#", "mailto:", "tel:", "javascript:")):
        return None
    base_host = urlparse(base).netloc.lower()
    host = urlparse(href).netloc.lower()
    if not host:  # relative link -> internal
        return True
    return host == base_host


def audit(url: str, html: Optional[str] = None) -> Dict[str, Any]:
    """Run an on-page SEO audit.

    Args:
        url: page URL (used for internal/external link classification).
        html: optional raw HTML; if omitted the page is fetched from `url`.

    Returns:
        dict with keys: url, fetched, title, meta_description, headings,
        word_count, links, images, issues, score (0-100).
    """
    if html is None:
        html = fetch_html(url)
    if not html:
        return {"url": url, "fetched": False, "issues": ["Could not fetch page."],
                "score": 0}

    soup = make_soup(html)
    issues: List[str] = []

    title = (soup.title.get_text(strip=True) if soup.title else "") or ""
    meta_tag = soup.find("meta", attrs={"name": "description"})
    meta_desc = (meta_tag.get("content", "").strip() if meta_tag else "")

    headings = {f"h{i}": [h.get_text(strip=True)
                          for h in soup.find_all(f"h{i}")] for i in range(1, 4)}
    h1s = headings["h1"]

    main_text = extract_main_text(html)
    wc = word_count(main_text)

    internal = external = 0
    for a in soup.find_all("a", href=True):
        kind = _same_domain(url, a["href"])
        if kind is True:
            internal += 1
        elif kind is False:
            external += 1

    imgs = soup.find_all("img")
    with_alt = sum(1 for i in imgs if i.get("alt", "").strip())
    alt_coverage = round(with_alt / len(imgs), 2) if imgs else 1.0

    # --- issue detection ---
    if not title:
        issues.append("Missing <title>.")
    elif not (TITLE_MIN <= len(title) <= TITLE_MAX):
        issues.append(f"Title length {len(title)} chars (aim {TITLE_MIN}-{TITLE_MAX}).")
    if not meta_desc:
        issues.append("Missing meta description.")
    elif not (META_MIN <= len(meta_desc) <= META_MAX):
        issues.append(f"Meta description {len(meta_desc)} chars (aim {META_MIN}-{META_MAX}).")
    if len(h1s) == 0:
        issues.append("No H1 heading.")
    elif len(h1s) > 1:
        issues.append(f"Multiple H1s ({len(h1s)}); use exactly one.")
    if wc < 300:
        issues.append(f"Thin content ({wc} words); aim for 300+ for indexable pages.")
    if imgs and alt_coverage < 1.0:
        issues.append(f"Only {int(alt_coverage*100)}% of images have alt text.")
    if internal == 0:
        issues.append("No internal links found.")

    score = max(0, 100 - 12 * len(issues))

    return {
        "url": url,
        "fetched": True,
        "title": title,
        "title_length": len(title),
        "meta_description": meta_desc,
        "meta_length": len(meta_desc),
        "headings": headings,
        "word_count": wc,
        "links": {"internal": internal, "external": external},
        "images": {"total": len(imgs), "with_alt": with_alt,
                   "alt_coverage": alt_coverage},
        "issues": issues,
        "score": score,
    }


if __name__ == "__main__":
    sample = """
    <html><head><title>Cold Brew Coffee Subscription | Daily Delivery</title>
    <meta name="description" content="Fresh cold brew delivered weekly. Pick your roast, set your schedule, cancel anytime. Free shipping on the first order today."></head>
    <body><h1>Cold Brew, Delivered</h1>
    <p>%s</p>
    <a href="/pricing">Pricing</a><a href="https://other.com">Partner</a>
    <img src="a.jpg" alt="cold brew bottle"><img src="b.jpg"></body></html>
    """ % ("Great coffee every morning. " * 80)
    r = audit("https://example.com/cold-brew", html=sample)
    assert r["fetched"] and r["title_length"] > 0
    print("OK seo_audit score=", r["score"], "issues=", r["issues"])
    print("words=", r["word_count"], "links=", r["links"], "imgs=", r["images"])
