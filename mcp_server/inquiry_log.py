"""A small MCP server that records visitor questions the assistant couldn't answer.

MCP (Model Context Protocol) is the standard way to give an AI assistant tools.
Claude Code starts this script, talks to it over standard input/output, and
sees the three functions below as tools it can call.

Run by hand to check it starts:   python mcp_server/inquiry_log.py
(It will wait silently for messages. Press Ctrl+C to stop.)
"""

import json
from datetime import datetime, timezone
from pathlib import Path

from mcp.server.mcpserver import MCPServer

# Where inquiries are saved: data/inquiries.json in the project folder.
DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "inquiries.json"

# The server object. The name is what Claude Code shows in its tool list.
mcp = MCPServer("inquiry-log")


def load() -> list[dict]:
    """Read saved inquiries, or return an empty list if none yet."""
    if not DATA_FILE.exists():
        return []
    return json.loads(DATA_FILE.read_text(encoding="utf-8"))


def save(items: list[dict]) -> None:
    """Write inquiries back to disk, creating the data folder if needed."""
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    DATA_FILE.write_text(json.dumps(items, indent=2), encoding="utf-8")


@mcp.tool()
def log_inquiry(question: str, visitor_email: str = "", notes: str = "") -> str:
    """Record a visitor question the assistant could not answer from the documents.

    Args:
        question: The visitor's question, as close to their words as possible.
        visitor_email: Their email address if they gave one, otherwise empty.
        notes: Anything else useful for the owner (dates, group size, context).
    """
    items = load()
    entry = {
        "id": len(items) + 1,
        "logged_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "question": question.strip(),
        "visitor_email": visitor_email.strip(),
        "notes": notes.strip(),
    }
    items.append(entry)
    save(items)
    return f"Logged inquiry #{entry['id']}. The owner will see it in the next report."


@mcp.tool()
def update_inquiry(inquiry_id: int, visitor_email: str = "", notes: str = "") -> str:
    """Add details to an inquiry that was already logged, instead of logging a new one.

    Use this when the visitor gives their email or more context after the
    question was logged.

    Args:
        inquiry_id: The number returned by log_inquiry.
        visitor_email: Their email address, if newly given.
        notes: Extra details to append (dates, group size, chaperones).
    """
    items = load()
    for entry in items:
        if entry["id"] == inquiry_id:
            if visitor_email.strip():
                entry["visitor_email"] = visitor_email.strip()
            if notes.strip():
                # Keep earlier notes and add the new ones on a new line.
                entry["notes"] = (entry["notes"] + "\n" + notes.strip()).strip()
            save(items)
            return f"Updated inquiry #{inquiry_id}."
    return f"No inquiry #{inquiry_id} found. Use log_inquiry to create one."


@mcp.tool()
def list_inquiries() -> str:
    """Return every logged inquiry as JSON, newest first. Used for reports."""
    items = load()
    items.sort(key=lambda item: item["logged_at"], reverse=True)
    return json.dumps(items, indent=2)


if __name__ == "__main__":
    # "stdio" means: talk over standard input/output, which is how Claude Code connects.
    mcp.run(transport="stdio")
