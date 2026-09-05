# Hooks and per-project vaults

Read this reference only for session hooks, write validators, background agents,
or per-project vault selection. All hooks ship inert or require explicit
configuration; do not enable one without the user's request.

## Session-start context

`hooks/load_vault_context.py` can inject `_CLAUDE.md`, `index.md`, and recent log
context when a session starts. Configure it through `scripts/setup.sh` and the
host platform's documented session-start hook mechanism. Even when context is
injected, resolve the selected vault first and reread mutable note targets before
writing.

## Background consolidation

`hooks/obsidian-bg-agent.sh` is an opt-in background agent for Claude Code's
`PostCompact` event. It reads the session summary and propagates vault-worthy
items into the selected vault. It must remain add/update/link-only and no-op when
its enable flag or vault path is absent.

Use the platform-neutral declaration in
[`../hooks/obsidian-bg-agent.hook.yaml`](../hooks/obsidian-bg-agent.hook.yaml)
and the example in
[`../hooks/postcompact.hook.example.json`](../hooks/postcompact.hook.example.json)
instead of recreating hook JSON from memory. The script logs diagnostics to
`/tmp/obsidian-bg-agent.log`.

## Write-time AI-first validator

`hooks/validate-ai-first.sh` is a non-blocking post-write validator. It checks
vault Markdown for frontmatter delimiters, YAML-safe indentation, required
AI-first fields, the `## For future Claude` preamble, and banned substitution
characters. It skips configured non-note and private infrastructure paths.

Use [`../hooks/validate-ai-first.hook.yaml`](../hooks/validate-ai-first.hook.yaml)
as the platform-neutral specification. A warning does not roll back the write;
repair the note in the same session using the core reread/merge/retry contract.

## Per-project vault selection

The default setup writes `OBSIDIAN_VAULT_PATH` globally. On Claude Code, a
repository can override it with project-local `.claude/settings.json`:

```json
{
  "env": {
    "OBSIDIAN_VAULT_PATH": "/path/to/project-vault"
  }
}
```

Every hook resolves `OBSIDIAN_VAULT_PATH` when it runs, so the project override
selects the matching vault without reinstalling commands or hooks. Restart the
host session after changing project settings.

This selects one whole vault; it does not scope search within a shared vault.
Commands such as `/obsidian-find`, `/obsidian-recap`, and `/obsidian-emerge`
still see the full selected vault unless their canonical procedures add a
separate scope.

When active environment guidance defines organizational and personal vaults,
that guidance remains authoritative over this generic environment variable.
Never switch from a missing selected vault to another configured vault without
explicit direction.
