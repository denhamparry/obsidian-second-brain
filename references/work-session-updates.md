# Work-session and direct note updates

Read this reference for the common continuity path: record work in an existing
daily note, update the related project note, and append one operation-log entry.
It also governs any similarly small direct filesystem or MCP note update.

Do not load command routing, research, scheduling, bootstrap, or hook references
for this path unless the request independently needs one of them.

## Resolve the targets

1. The core skill has already selected the vault and loaded its local guidance.
   Use the vault's own folders, section names, templates, and timezone.
2. Search for the project by title, aliases, repository, and likely folder.
   Update the existing project note; do not create a near-duplicate.
3. Resolve today's daily note using the selected vault's local date and naming
   convention. Create it from the configured template only when exhaustive
   search proves it does not exist.
4. Resolve the operation log:
   - use `Logs/YYYY-MM-DD.md` when `Logs/` exists;
   - otherwise use legacy root `log.md`;
   - if vault-local instructions define another append-only log, follow them.
5. Treat the daily note, project note, and operation log as three independent
   concurrency targets. A successful update to one does not permit a stale
   write to another.

## Prepare narrow deltas

Keep each requested change concise and place it under an existing semantic
anchor when possible:

- daily note: the local `Progress`, `Completed`, `Work`, or equivalent section;
- project note: `Recent activity`, `Status`, `Decisions`, or the closest
  vault-defined section;
- operation log: one timestamped append describing the operation and affected
  notes.

Preserve all other text byte-for-byte where the write primitive permits. Do not
replace a complete note just to add a bullet or refresh one section.

## Reread, merge, and retry

Apply the core optimistic-concurrency contract separately to each target:

1. Read the target during discovery and construct only the intended delta.
2. Immediately before mutation, reread the same target.
3. If it changed since discovery, merge the concurrent content into the working
   view before the first mutation attempt.
4. Use a narrow conditional section anchor, frontmatter key, or append
   primitive. The mutation must fail rather than overwrite when its expected
   content is stale.
5. On an anchor or version mismatch, reread, merge, and retry. Stop after three
   failed attempts for that target and report the unresolved conflict.
6. Reread after success. Verify the requested addition, every concurrent entry
   observed during retries, and the unaffected surrounding content.

For direct filesystem tools, prefer a narrow patch with exact context. For MCP,
prefer `append_content` for append-only targets and a bounded section-update
primitive for existing notes. If the MCP exposes only a broad write, reread
immediately before it, limit the replacement to the smallest supported region,
and verify immediately afterward. Never describe that fallback as atomic.

## Append-only operation logs

Operation logs have a stronger invariant than ordinary notes:

- reread immediately before appending;
- append exactly one new entry without sorting or normalizing older entries;
- after the write, require the complete pre-write content to remain an exact
  prefix of the result;
- if another writer appended first, retain that entry and append after it;
- never use a whole-file replacement, truncate-and-rewrite, or retry result that
  changes existing bytes.

If no safe append primitive exists, stop and report the limitation instead of
risking operation history.

## Propagate and report

After all three targets verify successfully:

- confirm links between the daily note and project note when local rules require
  them;
- update `index.md` only if a new note was created;
- avoid a second operation-log entry for propagation performed as part of the
  same logical update;
- report the exact notes changed and whether any retry merged concurrent work.

If one target reaches the retry limit, preserve every successful target, report
the partial result and conflict clearly, and do not claim the whole operation
completed.
