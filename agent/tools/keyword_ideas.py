"""
keyword_ideas — expand a seed term into grouped keyword / topic ideas.

Two sources, used together and deduped:
  1. Live: search-engine autocomplete (the public Google "suggestqueries"
     endpoint that returns a JSON array of completions) seeded with the term
     and with modifier prefixes/suffixes ("best <seed>", "<seed> vs", etc.).
  2. Offline fallback: a built-in modifier expansion so the tool always
     returns useful ideas even with no network.

Ideas are grouped by search intent (informational / commercial / comparison /
local / questions) so the agent can map them to funnel stages.

Build-off note: the "alphabet soup + modifiers" expansion is a widely used
keyword-research pattern; all code original. See ATTRIBUTIONS.md.
"""

from __future__ import annotations

import json
from typing import Any, Dict, List

try:
    from ._http import DEFAULT_HEADERS
except ImportError:
    from _http import DEFAULT_HEADERS

import requests

_AUTOCOMPLETE_URL = "https://suggestqueries.google.com/complete/search"

_QUESTION_MODS = ["how to", "what is", "why", "when to", "can you", "is", "does"]
_COMMERCIAL_MODS = ["best", "top", "cheap", "affordable", "buy", "review of"]
_COMPARISON_MODS = ["vs", "alternative", "or", "compared to"]
_LOCAL_MODS = ["near me", "in my area", "delivery", "online"]
_SUFFIXES = ["for beginners", "guide", "tips", "ideas", "examples", "pricing",
             "cost", "service", "tool", "software"]


def _autocomplete(term: str, timeout: int = 8) -> List[str]:
    """Hit the public autocomplete endpoint; return [] on any failure."""
    try:
        resp = requests.get(
            _AUTOCOMPLETE_URL,
            params={"client": "firefox", "q": term},
            headers=DEFAULT_HEADERS,
            timeout=timeout,
        )
        resp.raise_for_status()
        data = json.loads(resp.text)
        # Format: [query, [suggestion, suggestion, ...], ...]
        if isinstance(data, list) and len(data) > 1 and isinstance(data[1], list):
            return [s for s in data[1] if isinstance(s, str)]
    except Exception:
        pass
    return []


def _offline_expand(seed: str) -> List[str]:
    """Generate modifier-based ideas without any network call."""
    out = []
    for m in _QUESTION_MODS:
        out.append(f"{m} {seed}")
    for m in _COMMERCIAL_MODS:
        out.append(f"{m} {seed}")
    for m in _COMPARISON_MODS:
        out.append(f"{seed} {m}")
    for m in _LOCAL_MODS:
        out.append(f"{seed} {m}")
    for s in _SUFFIXES:
        out.append(f"{seed} {s}")
    return out


def _classify(kw: str) -> str:
    low = kw.lower()
    if any(low.startswith(q) or f" {q} " in f" {low} " for q in _QUESTION_MODS) or low.endswith("?"):
        return "questions"
    if any(m in low for m in _COMPARISON_MODS):
        return "comparison"
    if any(m in low for m in _COMMERCIAL_MODS):
        return "commercial"
    if any(m in low for m in _LOCAL_MODS):
        return "local"
    return "informational"


def ideas(seed: str, use_live: bool = True) -> Dict[str, Any]:
    """Return grouped keyword/topic ideas for a seed term.

    Args:
        seed: the seed keyword/topic.
        use_live: if True, also query live autocomplete (falls back silently).

    Returns:
        dict with 'seed', 'count', 'source', and 'groups' (intent -> [ideas]).
    """
    seed = (seed or "").strip()
    if not seed:
        return {"seed": seed, "count": 0, "groups": {}, "source": "none"}

    collected: List[str] = []
    source = "offline"
    if use_live:
        live = _autocomplete(seed)
        for mod in _COMMERCIAL_MODS[:3] + _QUESTION_MODS[:3]:
            live += _autocomplete(f"{mod} {seed}")
        if live:
            collected.extend(live)
            source = "autocomplete"

    collected.extend(_offline_expand(seed))

    # dedupe, preserve order, drop the bare seed
    seen, deduped = set(), []
    for kw in collected:
        k = " ".join(kw.lower().split())
        if k and k != seed.lower() and k not in seen:
            seen.add(k)
            deduped.append(kw.strip())

    groups: Dict[str, List[str]] = {
        "informational": [], "commercial": [], "comparison": [],
        "local": [], "questions": [],
    }
    for kw in deduped:
        groups[_classify(kw)].append(kw)

    return {
        "seed": seed,
        "count": len(deduped),
        "source": source,
        "groups": {g: v for g, v in groups.items() if v},
    }


if __name__ == "__main__":
    # use_live=False keeps the smoke test deterministic and network-free
    r = ideas("cold brew coffee subscription", use_live=False)
    assert r["count"] > 10, r["count"]
    assert "commercial" in r["groups"] and "questions" in r["groups"]
    print("OK keyword_ideas count=", r["count"], "source=", r["source"])
    for g, v in r["groups"].items():
        print(f"  {g}: {v[:3]}")
