#!/usr/bin/env python3
"""PreToolUse hook: block file edits to protected paths.

How Claude Code talks to this script:
- Before running a matched tool, Claude Code sends the tool call as JSON
  on stdin, e.g. {"tool_name": "Edit", "tool_input": {"file_path": "..."}}
- Exit code 0  -> the tool call is ALLOWED to proceed
- Exit code 2  -> the tool call is BLOCKED, and whatever this script
  prints to stderr is shown to the agent as the reason

The plumbing below is complete. Your one job (TODO 2 of 2): decide what
to protect.
"""

import json
import sys
from pathlib import PurePosixPath

# ✏️ TODO 2 of 2 — which paths are protected?
# List path prefixes (folders) that the agent must never write into.
# Think: which folder holds the workshop's irreplaceable source data?
# Example shape:  PROTECTED_PREFIXES = ["some_folder/", "other/"]
PROTECTED_PREFIXES = ["TODO/"]


def main() -> None:
    payload = json.load(sys.stdin)
    tool_input = payload.get("tool_input", {})

    # Edit/Write/MultiEdit all carry the target as file_path
    file_path = tool_input.get("file_path", "")
    if not file_path:
        sys.exit(0)  # nothing to check

    # Normalize: strip any leading ./ and resolve relative to the repo
    path = PurePosixPath(file_path.replace("\\", "/"))
    parts = path.parts

    for prefix in PROTECTED_PREFIXES:
        prefix_name = prefix.strip("/")
        if prefix_name in parts:
            print(
                f"BLOCKED by hook: '{file_path}' is inside the protected "
                f"'{prefix_name}/' folder. This folder is read-only - "
                "work with copies in memory instead.",
                file=sys.stderr,
            )
            sys.exit(2)

    sys.exit(0)


if __name__ == "__main__":
    main()
