---
name: obsidian-second-brain
description: Operate an Obsidian vault as an AI-first knowledge base. Use when the user asks to read, search, create, update, reconcile, or organize vault notes; log work or decisions; manage people, projects, tasks, boards, or daily notes; run a named Obsidian command; ingest or research sources into the vault; audit or bootstrap a vault; or configure its scheduled agents and hooks.
---

# Obsidian second brain

Operate the selected vault as a connected, self-rewriting knowledge base. Keep
the universal rules below in context, then load only the focused reference or
canonical command needed for the request.

## Select the vault and its rules

1. Apply active user, repository, and environment instructions before choosing
   a vault. When those instructions distinguish organizational work from a
   personal vault, work context wins over account type. For example, any Nscale
   work uses the configured Nscale vault; non-Nscale personal work uses the
   configured personal vault. Read the exact paths from active instructions
   instead of hard-coding a machine-specific path here.
2. Confirm the selected path exists and is accessible before writing. If it is
   unavailable, report that exact path and stop the write. Do not silently use
   another vault, the current repository, or a newly created fallback.
3. Use a configured Obsidian MCP server when it exposes the needed operation;
   otherwise use direct filesystem tools. The safety and concurrency rules are
   identical for both access methods.
4. Read `_CLAUDE.md` at the selected vault root before operating on notes unless
   its contents were already injected for this session. Also read any other
   vault-local guidance required by active instructions. Vault-local rules for
   folders, naming, frontmatter, privacy, auto-save behavior, and propagation
   override defaults in this skill. Where they are silent, use this skill's
   defaults.
5. On an unfamiliar vault, inventory its structure and read representative
   notes in each target folder before introducing a format or section pattern.
6. If the vault has `CRITICAL_FACTS.md`, load it as compact session context and
   treat it as authoritative current-state data. Update it only when a critical
   fact actually changes, preserving history in the related canonical note.

## Universal vault invariants

### AI-first notes

Every created or updated note must remain useful when retrieved without the
current conversation:

- include the required `## For future Claude` preamble;
- preserve rich frontmatter with `type`, `date`, `tags`, and `ai-first: true`,
  plus type-specific fields;
- use `[[wikilinks]]` for people, projects, decisions, ideas, and concepts;
- preserve source URLs and add recency markers to external claims;
- distinguish stated facts, strong evidence, weaker inference, and speculation;
- never fabricate facts, entities, dates, or absence; mark unknowns `TBD`.

For schemas, examples, or audits, read
[`references/ai-first-rules.md`](references/ai-first-rules.md). For detailed
formatting and section-update rules, read
[`references/write-rules.md`](references/write-rules.md).

### Search before create

Before creating a note, search exhaustively by plausible title, alias, folder,
and related entity. Update the existing note when it represents the same thing.
If similar results are ambiguous, show them and resolve the target instead of
silently creating a duplicate or claiming nothing exists.

### Privacy and preservation

- Honor every private, ask-first, read-only, and do-not-touch folder named by
  vault-local guidance. Do not inspect or mutate one merely because another
  note links to it.
- Treat `raw/` source material as immutable unless the user explicitly requests
  a correction to that source.
- Preserve historical facts. When a fact changes, retain the previous state and
  append the new state with event and transaction time where the vault schema
  supports it.
- Archive rather than delete unless the user explicitly authorizes deletion.
  Do not modify templates during ordinary note operations.

### Propagation and operation logs

Never create an orphaned update. Propagate the change to the relevant daily
note, project or person note, task or board, and `index.md` when a new note is
created, as required by vault-local rules.

Every mutation also gets an operation-log entry. Use `Logs/YYYY-MM-DD.md` when
the vault has the split log layout; otherwise append to legacy `log.md`.
Operation logs are append-only history: never replace, reorder, truncate, or
rewrite existing entries.

### Optimistic concurrency for every write

An initial read is discovery evidence, not write authorization. For each direct
filesystem or MCP mutation:

1. Reread that exact target immediately before the mutation and retain the
   current content, version, or narrow anchor used by the write.
2. Apply the smallest conditional change: an append primitive for append-only
   data, or a narrow section/frontmatter patch whose expected anchor rejects
   stale content. Never replace a broad note region merely because it was read
   earlier.
3. If the anchor or version no longer matches, treat it as a concurrent update.
   Reread the latest content, merge the requested delta with every concurrent
   addition, and retry. Make at most three attempts per target.
4. After a successful mutation, reread and verify that both the requested change
   and all previously observed concurrent content remain.
5. If three attempts conflict, stop that target and report the exact note,
   requested change, and conflicting region. Never fall back to blind overwrite
   or truncation.

For operation logs, the complete pre-write content must remain an exact prefix
after every retry. Prefer MCP append operations when available. A backend that
cannot reject a stale section update requires an immediate reread, the narrowest
available mutation, and post-write verification; do not claim it is atomic.

## Route the request

Choose one primary route. Load only its listed reference, plus a canonical
command file when that reference selects one.

| Request | Read next |
| --- | --- |
| Routine work-session continuity: update an existing daily note, project note, and operation log | [`references/work-session-updates.md`](references/work-session-updates.md) |
| A named `/obsidian-*`, thinking, meta, or other canonical command, or a natural-language request matching one | [`references/command-routing.md`](references/command-routing.md), then exactly one selected `commands/<name>.md` |
| Research command setup, credentials, cost behavior, or source-specific routing | [`references/research-operations.md`](references/research-operations.md) |
| First-time access, install, vault bootstrap, presets, or assistant mode | [`references/vault-setup.md`](references/vault-setup.md) |
| Morning, nightly, weekly, or health-check schedules and headless execution | [`references/scheduled-agents.md`](references/scheduled-agents.md) |
| Session hooks, write validators, background agents, or per-project vault configuration | [`references/hooks-and-project-vaults.md`](references/hooks-and-project-vaults.md) |
| Insight-saving, living-knowledge refresh, automatic synthesis, reconciliation, or proactive save behavior | [`references/knowledge-maintenance.md`](references/knowledge-maintenance.md) |
| New note schema, AI-first audit, or advanced write/refresh behavior | [`references/ai-first-rules.md`](references/ai-first-rules.md) and, only when needed, [`references/write-rules.md`](references/write-rules.md) |
| Folder-layout or bootstrap-template details | [`references/vault-schema.md`](references/vault-schema.md) or [`references/claude-md-template.md`](references/claude-md-template.md) |

Do not load the command catalogue, research setup, schedules, bootstrap, or hook
instructions for a routine direct work-session update. Do not load every
canonical command when one route matches.

## Completion

Report the notes or configuration changed, the relevant propagation and log
updates, and any unresolved conflict. Never claim a write succeeded until the
post-write reread confirms it.
