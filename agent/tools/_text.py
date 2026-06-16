"""
Readability + tokenisation helpers (pure-Python, no dependencies).

The Flesch Reading Ease implementation here is original code following the
published Flesch formula. A heuristic syllable counter is included so the
module has zero third-party dependencies. The well-known `textstat` project
(MIT) computes the same family of metrics; see ATTRIBUTIONS.md.
"""

from __future__ import annotations

import re
from typing import List

_VOWELS = "aeiouy"


def sentences(text: str) -> List[str]:
    """Split text into sentences on ., !, ? (good-enough heuristic)."""
    parts = re.split(r"[.!?]+(?:\s|$)", text)
    return [p.strip() for p in parts if p.strip()]


def words(text: str) -> List[str]:
    """Return word-like tokens."""
    return re.findall(r"[A-Za-z][A-Za-z'-]*", text)


def count_syllables(word: str) -> int:
    """Estimate syllables in a word with a vowel-group heuristic.

    Counts contiguous vowel groups, subtracts a silent trailing 'e',
    and clamps to a minimum of 1.
    """
    word = word.lower()
    if not word:
        return 0
    groups = re.findall(rf"[{_VOWELS}]+", word)
    count = len(groups)
    if word.endswith("e") and not word.endswith(("le", "ee", "ye")):
        count -= 1
    return max(count, 1)


def flesch_reading_ease(text: str) -> float:
    """Flesch Reading Ease score (0-100; higher = easier to read).

    Formula: 206.835 - 1.015*(words/sentences) - 84.6*(syllables/words).
    Returns 0.0 for empty / unparseable text.
    """
    ws = words(text)
    ss = sentences(text)
    if not ws or not ss:
        return 0.0
    total_syll = sum(count_syllables(w) for w in ws)
    score = (
        206.835
        - 1.015 * (len(ws) / len(ss))
        - 84.6 * (total_syll / len(ws))
    )
    return round(max(0.0, min(100.0, score)), 1)


def reading_grade_label(score: float) -> str:
    """Map a Flesch score to a plain-language difficulty label."""
    if score >= 80:
        return "very easy (grade 5-6)"
    if score >= 60:
        return "plain English (grade 7-9)"
    if score >= 50:
        return "fairly difficult (grade 10-12)"
    if score >= 30:
        return "difficult (college)"
    return "very difficult (college graduate)"


if __name__ == "__main__":
    easy = "The cat sat on the mat. The dog ran fast. We had fun all day."
    hard = ("Notwithstanding the aforementioned considerations, the "
            "implementation necessitates comprehensive evaluation of "
            "multifactorial interdependencies.")
    e = flesch_reading_ease(easy)
    h = flesch_reading_ease(hard)
    assert e > h, (e, h)
    print(f"OK flesch easy={e} ({reading_grade_label(e)}) hard={h} ({reading_grade_label(h)})")
