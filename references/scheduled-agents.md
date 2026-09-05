# Scheduled agents

Read this reference only when configuring or running scheduled vault
maintenance. Scheduled agents are opt-in and conservative: they add, update,
and link; they do not delete or archive autonomously and do not ask questions
mid-run.

## Morning

Suggested schedule: daily at 08:00.

```text
Read _CLAUDE.md. Create or update today's daily note using the vault's template
and local conventions. Pull in tasks due today or overdue. List active projects
with no recent activity in the last seven days. Do not ask questions. Save and
stop.
```

## Nightly

Suggested schedule: daily at 22:00.

```text
Read _CLAUDE.md and perform a conservative end-of-day consolidation.

1. Summarize today's daily note and move clearly completed board tasks to Done.
2. Reconcile clear stale entity or concept facts; flag ambiguous conflicts
   instead of choosing silently.
3. Synthesize patterns supported by at least two unrelated recent sources.
4. Link new orphans and refresh index.md when needed.
5. Append one concise entry to the configured operation log.

Do not delete or archive. Do not ask questions. Save and stop.
```

Every scheduled write follows the core optimistic-concurrency contract. In
particular, nightly maintenance must reread each target immediately before its
narrow mutation and preserve changes made by interactive sessions.

## Weekly review

Suggested schedule: Friday at 18:00.

```text
Read _CLAUDE.md. Follow the canonical /obsidian-recap procedure for the week,
then create the vault's weekly review note and link it from the final daily note
for that period. Do not ask questions. Save and stop.
```

## Health check

Suggested schedule: Sunday at 21:00.

```text
Read _CLAUDE.md. Run the repository's vault_health.py against the selected
vault, write a severity-grouped health report, and make no autonomous repairs.
Do not ask questions. Save and stop.
```

## Configure and manage schedules

Use the host platform's scheduling capability. Configure only schedules the
user explicitly selects, and show the exact cadence and prompt. List or remove
existing schedules through that same host capability rather than inventing
state in the vault.

### Headless execution

Custom slash commands do not expand in non-interactive `claude -p` prompts. A
headless job must tell the agent to read the canonical command file:

```bash
# Wrong: sends literal command text
claude -p "/obsidian-daily"

# Correct: loads the procedure explicitly
cd "$OBSIDIAN_VAULT_PATH" && claude --dangerously-skip-permissions \
  -p "Read ~/.claude/commands/obsidian-daily.md and carry out its instructions exactly."
```

Set an explicit `PATH` in cron or launchd environments so the configured agent,
Python, and `uv` binaries resolve. Do not add
`--dangerously-skip-permissions` to a new automation without the user's explicit
authorization and a reviewed, bounded prompt.
