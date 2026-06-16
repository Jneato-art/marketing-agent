"""
content_scorer — score a marketing draft against a target keyword + readability.

Combines on-page keyword signals (presence in title/headings/first paragraph,
density), structure (use of headings), readability (Flesch), and length into a
single 0-100 score with concrete, prioritised fixes.

Build-off note: keyword/structure heuristics follow common SEO-content scoring
conventions; the Flesch metric mirrors `textstat` (MIT). All code original.
See ATTRIBUTIONS.md.
"""

from __future__ import annotations

import re
from typing import Any, Dict, List

try:
    from ._text import flesch_reading_ease, reading_grade_label, words
except ImportError:
    from _text import flesch_reading_ease, reading_grade_label, words

IDEAL_DENSITY_LOW, IDEAL_DENSITY_HIGH = 0.5, 2.5  # percent


def _density(text: str, keyword: str) -> float:
    kw = keyword.lower().strip()
    if not kw:
        return 0.0
    total = len(words(text)) or 1
    hits = len(re.findall(re.escape(kw), text.lower()))
    return round(100.0 * hits / total, 2)


def score(draft: str, keyword: str, target_words: int = 800) -> Dict[str, Any]:
    """Score a draft (markdown or plain text) for a target keyword.

    Args:
        draft: the content body (markdown headings with '#' are recognised).
        keyword: the primary target keyword/phrase.
        target_words: desired length; shorter drafts are penalised.

    Returns:
        dict with score (0-100), sub-scores, metrics, and a fixes list.
    """
    draft = draft or ""
    kw = (keyword or "").lower().strip()
    lines = draft.splitlines()
    heading_lines = [ln for ln in lines if ln.lstrip().startswith("#")]
    body_words = len(words(draft))
    first_para = next((ln for ln in lines if ln.strip() and not ln.lstrip().startswith("#")), "")

    in_title = bool(heading_lines) and kw in heading_lines[0].lower() if kw else False
    in_any_heading = any(kw in h.lower() for h in heading_lines) if kw else False
    in_intro = kw in first_para.lower() if kw else False
    density = _density(draft, kw)
    flesch = flesch_reading_ease(draft)

    fixes: List[str] = []
    points = 0

    # Keyword placement (max 35)
    if in_title:
        points += 15
    else:
        fixes.append(f"Add the keyword '{keyword}' to the main heading/title.")
    if in_intro:
        points += 10
    else:
        fixes.append(f"Mention '{keyword}' in the first paragraph.")
    if in_any_heading:
        points += 10
    else:
        fixes.append(f"Use '{keyword}' (or a variant) in at least one subheading.")

    # Density (max 15)
    if IDEAL_DENSITY_LOW <= density <= IDEAL_DENSITY_HIGH:
        points += 15
    elif density < IDEAL_DENSITY_LOW:
        fixes.append(f"Keyword density {density}% is low; weave '{keyword}' in a bit more.")
        points += 6
    else:
        fixes.append(f"Keyword density {density}% looks stuffed; reduce repetition.")
        points += 5

    # Structure (max 20)
    if len(heading_lines) >= 3:
        points += 20
    elif heading_lines:
        points += 10
        fixes.append("Add more subheadings to break up the text (aim 3+).")
    else:
        fixes.append("Add headings/subheadings — the draft has none.")

    # Readability (max 20)
    if flesch >= 60:
        points += 20
    elif flesch >= 45:
        points += 12
        fixes.append(f"Readability is moderate ({flesch}, {reading_grade_label(flesch)}); shorten sentences.")
    else:
        points += 4
        fixes.append(f"Hard to read ({flesch}, {reading_grade_label(flesch)}); use shorter words and sentences.")

    # Length (max 10)
    if body_words >= target_words:
        points += 10
    elif body_words >= target_words * 0.6:
        points += 6
        fixes.append(f"A little short ({body_words}/{target_words} words); expand thin sections.")
    else:
        fixes.append(f"Too short ({body_words}/{target_words} words); add depth and examples.")

    return {
        "score": min(points, 100),
        "metrics": {
            "word_count": body_words,
            "keyword_density_pct": density,
            "flesch_reading_ease": flesch,
            "readability_label": reading_grade_label(flesch),
            "headings": len(heading_lines),
            "keyword_in_title": in_title,
            "keyword_in_intro": in_intro,
            "keyword_in_subheading": in_any_heading,
        },
        "fixes": fixes,
    }


if __name__ == "__main__":
    draft = """# The Best Cold Brew Coffee Subscription for Busy Mornings

Cold brew coffee subscription services save you time every single day.
You pick the roast, set the schedule, and fresh cold brew arrives weekly.

## Why a cold brew subscription beats the cafe
""" + ("Smooth, low-acid coffee at home costs less than a daily cafe run. " * 40) + """

## How to choose your cold brew plan
""" + ("Compare roast, caffeine, and delivery cadence to fit your routine. " * 30)
    r = score(draft, "cold brew coffee subscription", target_words=600)
    assert 0 <= r["score"] <= 100
    print("OK content_scorer score=", r["score"])
    print("metrics=", r["metrics"])
    print("fixes=", r["fixes"])
