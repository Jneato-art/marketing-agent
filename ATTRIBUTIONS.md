# Attributions

The Marketing Agent's built-in tools layer (`agent/tools/`) is **original code**
that builds on patterns and ideas from the open-source projects below. We did
not copy substantial verbatim code from any of them. Every project listed here
is under a permissive license (MIT / Apache-2.0 / BSD); no GPL/AGPL/LGPL or
unlicensed code is used.

If you redistribute this repo, keep this file accurate.

## Projects we built off (patterns & ideas)

| Project | URL | License | What we used / adapted |
|---|---|---|---|
| GPT Researcher | https://github.com/assafelovic/gpt-researcher | Apache-2.0 | The **plan → search → scrape → synthesize** research architecture behind `web_research.py`. We reimplemented the loop in clean original code (sub-query planning, keyless SERP, main-text scraping, structured digest). No source files copied. |
| readability-lxml | https://github.com/buriy/python-readability | Apache-2.0 | The **"readability" main-content heuristic** (strip boilerplate, score blocks by text density, keep the densest) behind `extract_main_text` in `agent/tools/_http.py`. Reimplemented from the well-known approach; no code copied. |
| Trafilatura | https://github.com/adbar/trafilatura | Apache-2.0 | Same family of main-text-extraction ideas as a reference for `_http.py`. Pattern only; no code copied. |
| textstat | https://github.com/textstat/textstat | MIT | The **Flesch Reading Ease** metric family computed in `agent/tools/_text.py`. We implemented the published Flesch formula and a heuristic syllable counter ourselves (zero dependencies); no code copied. |
| feedparser | https://github.com/kurtmckee/feedparser | BSD-2-Clause | Used as a **runtime dependency** in `trends_monitor.py` for robust RSS/Atom parsing (with a built-in BeautifulSoup fallback when it is not installed). |
| Requests | https://github.com/psf/requests | Apache-2.0 | HTTP client used across the tools layer (runtime dependency). |
| Beautiful Soup | https://www.crummy.com/software/BeautifulSoup/ | MIT | HTML/XML parsing used across the tools layer (runtime dependency). |
| lxml | https://github.com/lxml/lxml | BSD-3-Clause | Fast parser backend for Beautiful Soup (runtime dependency). |
| httpx | https://github.com/encode/httpx | BSD-3-Clause | Async HTTP client (declared dependency; used by the Agent SDK custom-tools examples). |

## License compatibility

This repository is MIT-licensed (see `LICENSE`). MIT, Apache-2.0, and BSD are
all permissive and compatible with redistribution under MIT. The Apache-2.0
projects above carry a patent grant and a NOTICE requirement **only if** their
source is redistributed — since we redistribute none of their source, only the
attribution above is required, which this file provides.

Keyword expansion and SEO on-page checks follow widely used, non-proprietary
industry conventions and are implemented as original code.
