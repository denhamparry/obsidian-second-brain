---
status: Completed
issue: denhamparry/codex#83
date: 2026-09-05
updated: 2026-09-05
---

# Codex issue #83: Split skill routing and harden concurrent writes

## Problem and outcome

The 1,344-line `SKILL.md` eagerly loads command, research, scheduling, hook, and
bootstrap procedures for routine vault updates. It also lacks an explicit
optimistic-concurrency contract for shared notes. Replace it with a materially
smaller router that retains the universal safety invariants, routes specialized
work to focused references and canonical command files, and requires bounded
reread/merge/retry behavior that never drops concurrent content.

## Source snapshot and ownership

- [denhamparry/codex#83](https://github.com/denhamparry/codex/issues/83) was
  fetched 2026-09-05 22:16 BST in state `OPEN`, labelled `enhancement`, with no
  comments.
- `denhamparry/codex` tracks `skills/obsidian-second-brain` as a relative
  symlink to the separate `denhamparry/obsidian-second-brain` repository. The
  implementation and PR therefore belong in this repository; the PR will use
  `Closes denhamparry/codex#83` so the source issue remains linked.
- The owning repository baseline is `bf63932d73e50de334fe46eabfb72cf18f7239bd`.
  Its 44 command files are the platform-neutral canonical procedures.

## Issue traceability

| Requirement | Disposition and evidence target |
| --- | --- |
| Materially smaller top-level router | Replace the 1,344-line manual with a concise router containing selection, precedence, universal safety, concurrency, and conditional reference routing. |
| Move unrelated command bodies | Route all 44 command names to exactly one canonical `commands/<name>.md` procedure through a focused command-routing reference. |
| Routine direct work log loads one focused reference | Route the daily-note, project-note, and operation-log path directly to `references/work-session-updates.md`; it must not require research, scheduling, bootstrap, or hook references. |
| Preserve vault selection | Keep active environment guidance authoritative; explicitly preserve personal-versus-organizational selection, including Nscale when configured, without hard-coding machine-specific paths into the reusable skill. |
| Preserve `_CLAUDE.md` precedence | Require selection first, then vault-local `_CLAUDE.md`; its folder, naming, metadata, privacy, and write rules override defaults. |
| Preserve AI-first metadata | Keep the required preamble, frontmatter, recency, sources, links, confidence, and anti-fabrication essentials in the router, with full schemas routed to `references/ai-first-rules.md`. |
| Preserve private-folder protection | Require explicit authorization for private or do-not-touch folders named by vault-local guidance. |
| Preserve search-before-create | Require exhaustive alias/path search before absence claims or creation; update matching notes instead of duplicating them. |
| Preserve propagation | Require each write to update relevant linked notes, daily/project surfaces, index for new notes, and the correct operation log. |
| Preserve operation-log behavior | Detect split `Logs/YYYY-MM-DD.md` versus legacy `log.md`; operation histories are append-only and never rewritten or truncated. |
| Route specialized flows | Add focused references for command routing, research setup, vault bootstrap/access, schedules, and hooks/per-project configuration. |
| Immediate reread and narrow mutation | Require a reread directly before each filesystem or MCP mutation and use section anchors or append primitives instead of broad replacement. |
| Interleaved writer preservation | Add a deterministic fixture where the first write conflicts after another writer appends; retry must merge both the concurrent entry and requested update. |
| Append-only log protection | Exercise a guard that rejects any retry result that removes or rewrites the prior operation-log prefix. |
| Bounded repeated-conflict stop | Cap retries at three per target and test a persistent-conflict result with a clear unresolved-conflict report. |
| Routing completeness | Add deterministic tests for router size, reference existence, one-to-one coverage of all 44 command files, and isolation of the routine work-session route. |
| Generated platform consistency | Run the all-platform build and smoke tests; `dist/` remains ignored and must not be committed. |
| Repository documentation | Update contributor/architecture/README pointers that currently call `SKILL.md` a full manual or link to sections moved behind references. |
| Changelog | Record the router and concurrent-write hardening under `Unreleased`. |
| Merge, deployment, and cleanup | Intentionally out of scope; leave one open cross-repository PR for user-managed review and merge. |

The issue's website links and model-guidance link are explanatory evidence, not
authorization to mutate the website repository or any live vault.

## Implementation

1. Rewrite `SKILL.md` as the universal router and safety contract, with
   conditional reference selection and no embedded command catalogue bodies.
2. Add focused references for direct work-session updates, all canonical command
   routes, research setup, vault setup/bootstrap, scheduled agents, and
   hooks/per-project vaults.
3. Add deterministic router/concurrency tests with a small in-memory optimistic
   update fixture that models narrow conditional mutation for filesystem or MCP
   adapters.
4. Repair repository documentation and changelog statements made stale by the
   split.

## Files expected to change

- `docs/plan/issues/083_split_skill_router_and_harden_concurrent_writes.md`
- `SKILL.md`
- `references/work-session-updates.md`
- `references/command-routing.md`
- `references/research-operations.md`
- `references/vault-setup.md`
- `references/scheduled-agents.md`
- `references/hooks-and-project-vaults.md`
- `references/knowledge-maintenance.md`
- `references/write-rules.md`
- `adapters/lib.sh`
- `adapters/codex-cli/adapter.sh`
- `adapters/gemini-cli/adapter.sh`
- `adapters/opencode/adapter.sh`
- `adapters/hermes/adapter.sh`
- `adapters/pi/adapter.sh`
- `tests/test_skill_router.py`
- `tests/test_smoke.py`
- `CLAUDE.md`
- `architecture.md`
- `README.md`
- `CHANGELOG.md`

## Validation

- Baseline: `uv run pytest -q` passes 27 tests and
  `uv run python scripts/sweep_non_ascii.py --check` passes. The canonical
  skill validator rejects only the existing 1,204-character description.
- Run the new router/concurrency tests independently and as part of
  `uv run pytest -q`.
- Run the canonical skill validator and require the revised skill to pass.
- Run `bash scripts/build.sh` and confirm all platform outputs are generated
  consistently without tracked `dist/` changes.
- Run `uv run python scripts/sweep_non_ascii.py --check`, Ruff over changed
  Python, complete-file shell-fence validation for changed Markdown, and
  `git diff --check`.
- Exercise the routine route manually and verify it selects only the core
  router, vault-local instructions, and `work-session-updates.md`.
- Re-fetch the source issue before branch review and inspect the full remote PR
  diff during mandatory post-PR verification.

## Risks and boundaries

- Removing duplicated prose can silently orphan a trigger or safety rule.
  Deterministic one-to-one command coverage and explicit invariant checks guard
  the refactor.
- A generic retry loop cannot make arbitrary filesystem or MCP writes atomic.
  The contract therefore requires narrow conditional mutations that reject stale
  anchors, immediate rereads, post-write verification, and a bounded stop; it
  never promises atomicity the underlying primitive cannot provide.
- Append-only logs have a stronger invariant than ordinary notes: every retry
  must preserve the complete prior content as an exact prefix.
- The Nscale/personal split is environment policy, not a portable path default.
  The router names the selection precedence but reads exact paths from active
  instructions.
- This changes agent behavior that protects shared user data. After local
  review, request one unbiased read-only reviewer using the raw issue, diff, and
  validation evidence before PR handoff.

## Research review

Approved on iteration 1/3.

- Repository ownership is explicit, so the work will produce a real diff in
  `denhamparry/obsidian-second-brain` and close the source Codex issue through a
  qualified cross-repository keyword.
- The 44 files in `commands/` already own command bodies. A routing reference
  can preserve discoverability without copying hundreds of lines into another
  manual, and a one-to-one test prevents orphaned or duplicate command routes.
- Keeping the optimistic-concurrency contract in the core router makes it apply
  to every command; the work-session reference adds concrete direct-filesystem
  and MCP behavior without forcing unrelated setup or research context into a
  routine log.
- The fixture will use temporary real files and a conditional narrow-mutation
  adapter. It intentionally models stale-anchor rejection rather than claiming
  filesystem or MCP atomicity that the underlying write primitive cannot
  guarantee.
- Contributor docs, architecture text, the README anchor, and the changelog are
  included because each currently describes `SKILL.md` as the full manual or
  points to sections that will move. No generated `dist/` artifact is tracked.
- Baseline tests are self-contained. The only baseline validator failure is the
  oversized existing skill description, directly corrected by the router
  rewrite. No unresolved scope, ownership, safety, or validation concern
  remains.

## Implementation and branch review

Implemented in `denhamparry.co.uk/feat/gh-issue-083` from
`bf63932d73e50de334fe46eabfb72cf18f7239bd`. The top-level skill is 139 lines,
all 44 canonical commands have one route with exact `triggers_en` parity, and
the direct-update path is isolated from research, scheduling, bootstrap, hook,
and command-catalogue references. The former always-loaded critical-facts rule
remains in the core; living-knowledge, two-output, synthesis, reconciliation,
and save-reminder behavior remains discoverable in a focused reference.

Self-review also found and corrected a stale instruction in
`references/write-rules.md` that prescribed whole-file replacement for section
injection. It now follows the same immediate-reread, narrow-anchor,
three-attempt, post-write-verification contract and requires a real append
primitive for operation logs.

The first independent review requested changes because non-Claude adapters did
not expose the core concurrency contract and the initial fixture had a
check-then-write gap. The adapters now extract the canonical contract directly
from `SKILL.md` for Codex, Gemini, OpenCode, Pi, and both interactive and
scheduled Hermes skills. Hermes schedule bodies also derive from the focused
schedule reference. The fixture now uses atomic conditional primitives and
tests an exactly-once append when another writer lands after commit.

Independent re-review approved the reconciled implementation with no blocking
findings. It independently confirmed the contract in all generated runtime
surfaces, all 43 Hermes command skills, and all four Hermes scheduled skills,
plus exact focused-reference prompt parity and the revised race coverage.

## Validation results

- clean-lock `.venv/bin/pytest -q`: 44 passed in 9.72 seconds.
- `uvx ruff check tests/test_skill_router.py`: passed.
- canonical `quick_validate.py`: `Skill is valid!`.
- `uv run python scripts/sweep_non_ascii.py --check`: passed with 32 preserved
  characters inside exempt code fences or spans.
- `bash scripts/build.sh`: all six platforms built successfully; `dist/`
  remained ignored.
- complete-file Markdown shell-fence validation: passed, including every
  changed Markdown file.
- `git diff --check`: passed.
- Live issue re-fetched with no comments; owning repository `origin/main`
  remains at the branch base.

## Follow-up ideas

- The repository's committed `uv.lock` predates the current `pyproject.toml`
  version and pytest dev dependency, so `uv run` refreshes it locally. The
  unrelated resolver delta was removed from this issue patch; CI uses the same
  normal unlocked test invocation and does not require a clean lockfile.

## Outcome

Implementation and independent verification are complete on
`denhamparry.co.uk/feat/gh-issue-083`. The concise router, focused references,
atomic concurrency fixture, append-only protections, and generated runtime
parity satisfy the live issue criteria. Publication will leave an open,
unmerged cross-repository PR for user-managed review and merge.
