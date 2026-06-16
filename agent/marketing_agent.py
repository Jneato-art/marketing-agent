"""
Marketing Agent — autonomous runtime.

Loads the file-based agent (CLAUDE.md brain + skills/playbooks/knowledge) and runs
it against a goal you pass on the command line. The agent can search the web,
read its own skills and memory, and write deliverables + learnings back to disk.

Usage:
    python marketing_agent.py "Build a 90-day plan for my cold-brew subscription"

Requires ANTHROPIC_API_KEY in the environment (see .env.example).
"""

import asyncio
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

# The Claude Agent SDK. See https://docs.claude.com/en/api/agent-sdk/overview
from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions

load_dotenv()

REPO_ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = REPO_ROOT / "agent" / "out"
OUT_DIR.mkdir(parents=True, exist_ok=True)


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
        + "- ALWAYS append results to knowledge/experiments/experiments-log.md before finishing.\n"
    )


async def run(goal: str) -> None:
    options = ClaudeAgentOptions(
        system_prompt=load_brain(),
        # Give the agent the tools it needs: read/write files, run shell, search web.
        allowed_tools=["Read", "Write", "Edit", "Glob", "Grep", "Bash", "WebSearch", "WebFetch"],
        # Let it operate on the repo (skills, playbooks, knowledge, out/).
        cwd=str(REPO_ROOT),
        permission_mode="acceptEdits",
        model=os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-6"),
        # To connect marketing tools, add MCP servers here, e.g.:
        # mcp_servers={"bloom": {...}, "mailchimp": {...}},
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
