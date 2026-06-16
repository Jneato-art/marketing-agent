"""
Shared HTTP + HTML helpers for the marketing-agent tools layer.

Small, dependency-light utilities used across the tools:
- a polite requests session with a browser-ish User-Agent and timeouts
- main-text extraction from raw HTML

The extraction approach (strip script/style/nav/footer, score block tags,
keep the densest text) is a clean-room reimplementation of the classic
"readability" heuristic. It is original code; see ATTRIBUTIONS.md for the
permissively-licensed projects (readability-lxml / Trafilatura, both
Apache-2.0) whose well-known pattern inspired it.
"""

from __future__ import annotations

import re
from typing import Optional

import requests
from bs4 import BeautifulSoup

DEFAULT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (compatible; MarketingAgentBot/1.0; "
        "+https://github.com/Jneato-art/marketing-agent)"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}

DEFAULT_TIMEOUT = 15
_BOILERPLATE_TAGS = (
    "script", "style", "noscript", "nav", "header", "footer",
    "aside", "form", "svg", "iframe", "button",
)


def fetch_html(url: str, timeout: int = DEFAULT_TIMEOUT) -> Optional[str]:
    """Fetch a URL and return decoded HTML, or None on any failure.

    Never raises for network/HTTP problems — callers can treat None as
    "could not fetch" and continue with the next URL.
    """
    try:
        resp = requests.get(
            url, headers=DEFAULT_HEADERS, timeout=timeout, allow_redirects=True
        )
        resp.raise_for_status()
        ctype = resp.headers.get("Content-Type", "")
        if "html" not in ctype and "xml" not in ctype and ctype:
            return None
        return resp.text
    except Exception:
        return None


def make_soup(html: str) -> BeautifulSoup:
    """Build a BeautifulSoup parser, preferring lxml, falling back to stdlib."""
    try:
        return BeautifulSoup(html, "lxml")
    except Exception:
        return BeautifulSoup(html, "html.parser")


def clean_text(text: str) -> str:
    """Collapse whitespace runs into single spaces / single blank lines."""
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n\s*\n\s*\n+", "\n\n", text)
    return text.strip()


def extract_main_text(html: str, max_chars: int = 6000) -> str:
    """Extract the main readable text from an HTML document.

    Heuristic (clean-room readability pattern):
      1. Drop boilerplate tags (script/style/nav/header/footer/aside/...).
      2. Score candidate block elements by text length, penalising
         link-heavy (navigation) blocks.
      3. Return the highest-scoring block, trimmed to max_chars.
    """
    soup = make_soup(html)

    for tag in soup(list(_BOILERPLATE_TAGS)):
        tag.decompose()

    for preferred in ("article", "main"):
        node = soup.find(preferred)
        if node:
            txt = clean_text(node.get_text("\n", strip=True))
            if len(txt) > 200:
                return txt[:max_chars]

    best_text = ""
    best_score = 0.0
    for node in soup.find_all(["section", "div", "p"]):
        text = node.get_text(" ", strip=True)
        if len(text) < 120:
            continue
        link_text = "".join(a.get_text(" ", strip=True) for a in node.find_all("a"))
        link_ratio = (len(link_text) / len(text)) if text else 1.0
        score = len(text) * (1.0 - min(link_ratio, 0.95))
        if score > best_score:
            best_score = score
            best_text = node.get_text("\n", strip=True)

    if not best_text:
        best_text = soup.get_text("\n", strip=True)

    return clean_text(best_text)[:max_chars]


def word_count(text: str) -> int:
    """Count word-like tokens in a string."""
    return len(re.findall(r"\b\w[\w'-]*\b", text))


if __name__ == "__main__":
    sample = """
    <html><head><title>T</title><style>.x{}</style></head>
    <body>
      <nav><a href='/'>Home</a><a href='/about'>About</a></nav>
      <article><h1>Real Headline</h1>
      <p>This is the genuine body of the article with enough words to be
      counted as the main content block by the extractor heuristic, repeated
      so the density score wins over navigation chrome and sidebars.</p>
      <p>A second paragraph adds even more readable prose to the article body
      so the extraction clearly prefers it over the link-heavy navigation.</p>
      </article>
      <footer>copyright</footer>
    </body></html>
    """
    out = extract_main_text(sample)
    assert "genuine body" in out, out
    assert "Home" not in out, out
    print("OK extract_main_text ->", word_count(out), "words")
    print(out[:160])
