"""
Marketing Agent — autonomous runtime.

Loads the file-based agent (CLAUDE.md brain + skills/playbooks/knowledge) and runs
it against a goal you pass on the command line. The agent can search the web,
read its own skills and memory, write deliverables + learnings back to disk, and
call a built-in tools layer (web research, competitor scan, SEO audit, keyword
ideas, content scoring, trends monitoring) exposed as in-process MCP tools.

Usage:
    python marketing_agent.py "Build a 90-day plan for my cold-brew subscription"

Requires ANTHROPIC_API_KEY in the environment (see .env.example).
Install deps with: pip install -r requirements.txt
"""

import asyncio
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict

from dotenv import load_dotenv

# The Claude Agent SDK. See https://docs.claude.com/en/api/agent-sdk/overview
from claude_agent_sdk import (
    ClaudeSDKClient,
    ClaudeAgentOptions,
    tool,
    create_sdk_mcp_server,
)

# Built-in tools layer (agent/tools/). These are plain Python modules; we wrap
# them as in-process MCP tools below so the agent can call them directly.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from tools import (  # noqa: E402
    web_research,
    competitor_scan,
    seo_audit,
    keyword_ideas,
    content_scorer,
    trends_monitor,
)

load_dotenv()

REPO_ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = REPO_ROOT / "agent" / "out"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def _ok(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Wrap a JSON-able payload as a successful MCP tool result."""
    return {"content": [{"type": "text", "text": json.dumps(payload, indent=2, default=str)}]}


def _err(message: str) -> Dict[str, Any]:
    """Wrap an error as an MCP tool result that keeps the agent loop alive."""
    return {"content": [{"type": "text", "text": message}], "is_error": True}


# --- Built-in tools, exposed via the SDK @tool decorator ---------------------
# Each handler delegates to the matching module in agent/tools/ and returns the
# result as JSON text. readOnlyHint=True lets Claude batch these calls.

@tool(
    "web_research",
    "Run multi-query web research on an objective: plans sub-queries, searches "
    "the web, scrapes the top results, and returns a structured digest with "
    "source URLs to cite. Use before any market/strategy claim.",
    {"objective": str},
)
async def t_web_research(args: Dict[str, Any]) -> Dict[str, Any]:
    try:
        max_sources = int(args.get("max_sources", 6))
        return _ok(web_research.research(args["objective"], max_sources=max_sources))
    except Exception as e:
        return _err(f"web_research failed: {e}")


@tool(
    "competitor_scan",
    "Fetch competitor URLs and extract positioning signals (title, meta "
    "description, H1s, pricing hints, CTAs) into a comparison structure. "
    "Pass 'urls' as a comma-separated string or a list.",
    {"urls": str},
)
async def t_competitor_scan(args: Dict[str, Any]) -> Dict[str, Any]:
    try:
        raw = args["urls"]
        urls = raw if isinstance(raw, list) else [u.strip() for u in str(raw).split(",") if u.strip()]
        return _ok(competitor_scan.scan(urls))
    except Exception as e:
        return _err(f"competitor_scan failed: {e}")


@tool(
    "seo_audit",
    "Fetch a page and report on-page SEO basics: title/meta lengths, heading "
    "hierarchy, word count, internal/external links, image alt coverage, plus "
    "a list of concrete issues and a 0-100 score.",
    {"url": str},
)
async def t_seo_audit(args: Dict[str, Any]) -> Dict[str, Any]:
    try:
        return _ok(seo_audit.audit(args["url"]))
    except Exception as e:
        return _err(f"seo_audit failed: {e}")


@tool(
    "keyword_ideas",
    "Expand a seed term into keyword/topic ideas grouped by search intent "
    "(informational, commercial, comparison, local, questions). Uses live "
    "autocomplete with an offline fallback.",
    {"seed": str},
)
async def t_keyword_ideas(args: Dict[str, Any]) -> Dict[str, Any]:
    try:
        return _ok(keyword_ideas.ideas(args["seed"]))
    except Exception as e:
        return _err(f"keyword_ideas failed: {e}")


@tool(
    "content_scorer",
    "Score a draft against a target keyword + readability. Returns a 0-100 "
    "score, metrics (keyword density, Flesch reading ease, headings, length), "
    "and concrete fixes. Provide 'draft' and 'keyword'.",
    {"draft": str, "keyword": str},
)
async def t_content_scorer(args: Dict[str, Any]) -> Dict[str, Any]:
    try:
        target = int(args.get("target_words", 800))
        return _ok(content_scorer.score(args["draft"], args["keyword"], target_words=target))
    except Exception as e:
        return _err(f"content_scorer failed: {e}")


@tool(
    "trends_monitor",
    "Pull recent items for a topic from RSS/news feeds (defaults to Google "
    "News) so the agent can spot what is trending. Returns recent items with "
    "title, link, published date, and summary.",
    {"topic": str},
)
async def t_trends_monitor(args: Dict[str, Any]) -> Dict[str, Any]:
    try:
        limit = int(args.get("limit", 10))
        return _ok(trends_monitor.monitor(args["topic"], limit=limit))
    except Exception as e:
        return _err(f"trends_monitor failed: {e}")


# Bundle the tools into one in-process MCP server.
marketing_tools_server = create_sdk_mcp_server(
    name="marketing_tools",
    version="1.0.0",
    tools=[
        t_web_research,
        t_competitor_scan,
        t_seo_audit,
        t_keyword_ideas,
        t_content_scorer,
        t_trends_monitor,
    ],
)

# Fully-qualified tool names follow the mcp__<server>__<tool> convention.
MARKETING_TOOL_NAMES = [
    "mcp__marketing_tools__web_research",
    "mcp__marketing_tools__competitor_scan",
    "mcp__marketing_tools__seo_audit",
    "mcp__marketing_tools__keyword_ideas",
    "mcp__marketing_tools__content_scorer",
    "mcp__marketing_tools__trends_monitor",
]


def load_brain() -> str:
    """Read CLAUDE.md as the system prompt so CLI and Cowork share one brain."""
    brain = (REPO_ROOT / "CLAUDE.md").read_text(encoding="utf-8")
    index_path = REPO_ROOT / "knowledge" / "index.md"
    memory = index_path.read_text(encoding="utf-8") if index_path.exists() else ""
    return (
        brain
        + "\n\n---\n# Current memory (knowledge/index.md)\n\n"
        + memory
        + "\n\n---\n# Runtime notes\n"
        + f"- Repo root: {REPO_ROOT}\n"
        + f"- Write deliverables to: {OUT_DIR}\n"
        + "- Read skills from skills/, playbooks from playbooks/, memory from knowledge/.\n"
        + "- You have BUILT-IN TOOLS (in-process MCP server 'marketing_tools'):\n"
        + "  web_research, competitor_scan, seo_audit, keyword_ideas, content_scorer,\n"
        + "  trends_monitor. Prefer these for research/analysis (see the\n"
        + "  'autonomous-research' skill) and save findings to knowledge/.\n"
        + "- ALWAYS append results to knowledge/experiments/experiments-log.md before finishing.\n"
    )


async def run(goal: str) -> None:
    options = ClaudeAgentOptions(
        system_prompt=load_brain(),
        # Built-in file/shell/web tools + our in-process marketing tools.
        allowed_tools=[
            "Read", "Write", "Edit", "Glob", "Grep", "Bash", "WebSearch", "WebFetch",
            *MARKETING_TOOL_NAMES,
        ],
        mcp_servers={"marketing_tools": marketing_tools_server},
        # Let it operate on the repo (skills, playbooks, knowledge, out/).
        cwd=str(REPO_ROOT),
        permission_mode="acceptEdits",
        model=os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-6"),
    )

    print(f"\n=== Marketing Agent ===\nGoal: {goal}\n")

    async with ClaudeSDKClient(options=options) as client:
        await client.query(goal)
        async for message in client.receive_response():
            # Stream assistant text to the console as it works.
            for block in getattr(message, "content", []) or []:
                text = getattr(block, "text", None)
                if text:
                    print(text, end="", flush=True)
    print("\n\n=== Done. Check agent/out/ for deliverables and knowledge/ for learnings. ===")


def main() -> None:
    if len(sys.argv) < 2:
        print('Usage: python marketing_agent.py "<your marketing goal>"')
        raise SystemExit(1)
    goal = " ".join(sys.argv[1:])
    asyncio.run(run(goal))


if __name__ == "__main__":
    main()
