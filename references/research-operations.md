# Research operations

Read this reference only for research-toolkit setup, credential behavior, cost
tracking, or help choosing a research route. For execution, read exactly one
canonical procedure selected from
[`command-routing.md`](command-routing.md): `/research`, `/research-deep`,
`/notebooklm`, `/x-read`, `/x-pulse`, `/youtube`, `/podcast`, or
`/obsidian-ingest`.

## Choose the route

- General cited web research: `/research`.
- Multi-stage open-web research that starts from vault context and propagates
  findings: `/research-deep`.
- Source-grounded synthesis from vault notes and user-supplied material:
  `/notebooklm`.
- One X post or thread: `/x-read`; current X discourse for a topic: `/x-pulse`.
- YouTube transcript and metadata: `/youtube`.
- Podcast metadata, transcript, or show-notes fallback: `/podcast`.
- Arbitrary URL, PDF, audio, screenshot, or source material:
  `/obsidian-ingest`.

The selected command file owns its current arguments, save behavior, supported
sources, and fallback rules. Do not reconstruct those details from this setup
reference.

## Environment and dependencies

- Use Python 3.10 or newer and install repository dependencies with `uv sync`.
- Research configuration is read from process environment or
  `~/.config/obsidian-second-brain/.env`.
- `OBSIDIAN_VAULT_PATH` selects the vault for scripts that write notes. Apply
  the core skill's vault-selection and existence checks before running them.
- Never print, copy into notes, or commit API keys. Read only the variables
  needed by the selected command.
- Key requirements vary by command. `/research` and `/research-deep` support
  key-less public-source fallbacks; X, enhanced metadata, cloud transcription,
  and other integrations may need their documented key. Follow the canonical
  command instead of assuming every research route needs the same providers.

## Save and propagation behavior

Research output that is saved must follow the AI-first rule, preserve source
URLs verbatim, add recency/confidence markers, update related notes, and append
the correct operation log. A command whose default is chat-only does not gain
write permission from this reference.

Keep external-source failures explicit. If one source degrades and the command
continues with others, record the missing coverage rather than presenting the
result as complete.

## Cost tracking

Grok-backed calls used by `/x-read`, `/x-pulse`, `/youtube`, and `/podcast` can
record usage in `~/.research-toolkit/usage.log`. Inspect monthly totals with:

```bash
uv run python -c "from scripts.research.lib.usage import month_total; t,c = month_total(); print(f'\${t:.2f} across {c} calls')"
```

Do not infer a budget or authorize paid work solely from this reference. Follow
the user's limits and the selected command's current behavior.
