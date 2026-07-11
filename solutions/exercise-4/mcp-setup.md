# Playwright MCP — setup per tool

The same server works in every MCP-capable agent; only the config step
differs. That portability is the point of MCP.

**Prerequisite for all tools**: Node.js ≥ 18. First browser use
downloads ~150 MB (one time) — do this before the workshop, not during.

## Claude Code

```bash
claude mcp add playwright -- npx @playwright/mcp@latest
```

New session, then `/mcp` to confirm the server and its tools are
listed. To remove later: `claude mcp remove playwright`.

## Gemini CLI

Add to your `settings.json` (`~/.gemini/settings.json`, or the
project's `.gemini/settings.json`):

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  }
}
```

Restart the CLI; `/mcp` lists the connected servers.

## Cursor / other MCP-capable tools

Same server command (`npx @playwright/mcp@latest`) in the tool's MCP
configuration — check its docs for where the JSON lives. The tool names
you'll see (`browser_navigate`, `browser_snapshot`, `browser_click`,
`browser_console_messages`, …) are identical everywhere, because they
come from the server, not the client.

## Alternative for Claude users: the Chrome extension

Claude Code + the Claude in Chrome extension (`claude --chrome`) gives
the same verify-and-fix capability steering your real Chrome — near-zero
setup, no Node, visible clicking. Claude-only and paid-plan; see the
"Chrome-extension alternative" note in SOLUTION.md for the trade-offs.
