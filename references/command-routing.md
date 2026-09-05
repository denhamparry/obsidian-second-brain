# Canonical command routing

Read this reference when the user names a command or their request matches a
canonical command description. Select one row, then read exactly that linked
command file as the procedure. The command file's frontmatter owns its natural
language triggers and platform exclusions.

If two commands genuinely overlap, use the user's explicit command first. For
an ambiguous natural-language request, compare the two descriptions and ask
only when the choice would materially change the result. Do not combine command
bodies by default.

Each trigger cell copies the exact `triggers_en` values from its canonical file.
Match trigger phrases case-insensitively; the linked file remains authoritative.

## Vault commands

| Command | Natural-language triggers | Canonical procedure |
| --- | --- | --- |
| `/obsidian-board-hygiene` | clean up my board; triage my board; board hygiene; archive stale tasks; my board is a mess | [`commands/obsidian-board-hygiene.md`](../commands/obsidian-board-hygiene.md) |
| `/obsidian-board` | show board; kanban; what is on my board; update board | [`commands/obsidian-board.md`](../commands/obsidian-board.md) |
| `/obsidian-calendar` | review my agenda; check my calendar; what's on my schedule; what's on the calendar; agenda for this week; calendar check; reconcile calendar; what's not on my calendar; am I missing anything on my calendar; create a meeting note; log this meeting; meeting note for; prep this meeting; schedule a meeting; book a meeting; put this on my calendar; schedule this task; find a time for | [`commands/obsidian-calendar.md`](../commands/obsidian-calendar.md) |
| `/obsidian-capture` | capture this idea; save this idea; quick note; drop a thought | [`commands/obsidian-capture.md`](../commands/obsidian-capture.md) |
| `/obsidian-catchup` | catch up; catchup; what did I dump from telegram; process my captures; go through my telegram dumps; anything new from the phone; process my catchup; review what I captured; what did I capture on the go | [`commands/obsidian-catchup.md`](../commands/obsidian-catchup.md) |
| `/obsidian-daily` | todays note; create todays daily; open daily; today daily note | [`commands/obsidian-daily.md`](../commands/obsidian-daily.md) |
| `/obsidian-find` | find in vault; search my notes; where is; what did I write about | [`commands/obsidian-find.md`](../commands/obsidian-find.md) |
| `/obsidian-log` | log this work; log this session; log this dev session; obsidian log | [`commands/obsidian-log.md`](../commands/obsidian-log.md) |
| `/obsidian-person` | save this person; add person; new contact note; create person note | [`commands/obsidian-person.md`](../commands/obsidian-person.md) |
| `/obsidian-project` | new project; create project note; project setup; start a project | [`commands/obsidian-project.md`](../commands/obsidian-project.md) |
| `/obsidian-projects` | projects overview; project status; what am I working on; show projects | [`commands/obsidian-projects.md`](../commands/obsidian-projects.md) |
| `/obsidian-recap` | recap today; recap the week; summarize the week; month recap | [`commands/obsidian-recap.md`](../commands/obsidian-recap.md) |
| `/obsidian-recurring` | recurring task; monthly obligation; remind me every month; recurring payment; track a recurring | [`commands/obsidian-recurring.md`](../commands/obsidian-recurring.md) |
| `/obsidian-save` | save this; save the conversation; save to vault; obsidian save | [`commands/obsidian-save.md`](../commands/obsidian-save.md) |
| `/obsidian-task` | add task; new todo; track this; remind me | [`commands/obsidian-task.md`](../commands/obsidian-task.md) |
| `/obsidian-world` | load context; what is going on; where am I; load my world | [`commands/obsidian-world.md`](../commands/obsidian-world.md) |

## Thinking commands

| Command | Natural-language triggers | Canonical procedure |
| --- | --- | --- |
| `/idea-discovery` | what should I work on next; idea discovery; surface next directions; what's worth pursuing | [`commands/idea-discovery.md`](../commands/idea-discovery.md) |
| `/obsidian-challenge` | challenge this; grill me on this; red team my idea; stress test this | [`commands/obsidian-challenge.md`](../commands/obsidian-challenge.md) |
| `/obsidian-connect` | connect domains; cross-pollinate; bridge ideas; find an unexpected link | [`commands/obsidian-connect.md`](../commands/obsidian-connect.md) |
| `/obsidian-decide` | extract decisions; log decisions; what did we decide; log this decision; ADR; record decision; decision record | [`commands/obsidian-decide.md`](../commands/obsidian-decide.md) |
| `/obsidian-distill` | distill this; condense this note; summarize with sources; distill this source; boil this down with provenance | [`commands/obsidian-distill.md`](../commands/obsidian-distill.md) |
| `/obsidian-emerge` | find patterns; what is emerging; surface themes; unnamed patterns | [`commands/obsidian-emerge.md`](../commands/obsidian-emerge.md) |
| `/obsidian-graduate` | promote idea; graduate this to project; make a project from this; elevate idea | [`commands/obsidian-graduate.md`](../commands/obsidian-graduate.md) |
| `/obsidian-learn` | review learnings; what have I learned; show lessons; prune learnings | [`commands/obsidian-learn.md`](../commands/obsidian-learn.md) |
| `/obsidian-panel` | convene a panel; advisor panel; get multiple perspectives on; panel review; what would the experts say about | [`commands/obsidian-panel.md`](../commands/obsidian-panel.md) |
| `/obsidian-reconcile` | find contradictions; reconcile vault; fix conflicts; vault contradictions | [`commands/obsidian-reconcile.md`](../commands/obsidian-reconcile.md) |
| `/obsidian-review` | weekly review; monthly review; review my week; review my month | [`commands/obsidian-review.md`](../commands/obsidian-review.md) |
| `/obsidian-synthesize` | synthesize; auto-synthesis; make synthesis notes; find unnamed patterns | [`commands/obsidian-synthesize.md`](../commands/obsidian-synthesize.md) |
| `/vault-deep-synthesis` | synthesize what I know about; deep synthesis on; cross-reference my notes on; what does my vault say about | [`commands/vault-deep-synthesis.md`](../commands/vault-deep-synthesis.md) |

## Research commands

| Command | Natural-language triggers | Canonical procedure |
| --- | --- | --- |
| `/notebooklm` | notebooklm; research grounded; ground research in vault; ask my notebook; source-grounded research | [`commands/notebooklm.md`](../commands/notebooklm.md) |
| `/obsidian-ingest` | ingest this source; add this article; import this; absorb this | [`commands/obsidian-ingest.md`](../commands/obsidian-ingest.md) |
| `/podcast` | summarize this podcast; podcast episode summary; extract podcast; what's in this episode | [`commands/podcast.md`](../commands/podcast.md) |
| `/research-deep` | deep research; thorough research; vault-first research; research gaps | [`commands/research-deep.md`](../commands/research-deep.md) |
| `/research` | research this; look up; find information about; perplexity research | [`commands/research.md`](../commands/research.md) |
| `/x-pulse` | x pulse; what is trending on twitter; scan x for; twitter pulse | [`commands/x-pulse.md`](../commands/x-pulse.md) |
| `/x-read` | read this x post; deep read this tweet; analyze this tweet; read this thread | [`commands/x-read.md`](../commands/x-read.md) |
| `/youtube` | summarize youtube; youtube transcript; extract video; youtube to vault | [`commands/youtube.md`](../commands/youtube.md) |

Read [`research-operations.md`](research-operations.md) as well only when the
request needs toolkit setup, credential behavior, cost tracking, or help
choosing a research source.

## Meta commands

| Command | Natural-language triggers | Canonical procedure |
| --- | --- | --- |
| `/create-command` | create command; new command; add a command; scaffold a command | [`commands/create-command.md`](../commands/create-command.md) |
| `/obsidian-architect` | document this codebase; architect this project; map this code into my vault; generate architecture notes; refresh architecture docs | [`commands/obsidian-architect.md`](../commands/obsidian-architect.md) |
| `/obsidian-export` | export vault; snapshot vault; dump vault; vault export | [`commands/obsidian-export.md`](../commands/obsidian-export.md) |
| `/obsidian-health` | vault health; check vault; audit vault; vault diagnostics | [`commands/obsidian-health.md`](../commands/obsidian-health.md) |
| `/obsidian-init` | init vault; bootstrap vault; setup vault; scan vault | [`commands/obsidian-init.md`](../commands/obsidian-init.md) |
| `/obsidian-retrieval-eval` | evaluate retrieval; how good is my vault search; retrieval eval; test vault search quality; measure find quality | [`commands/obsidian-retrieval-eval.md`](../commands/obsidian-retrieval-eval.md) |
| `/obsidian-visualize` | visualize vault; vault map; canvas of vault; show me the vault shape | [`commands/obsidian-visualize.md`](../commands/obsidian-visualize.md) |

Vault bootstrap and hook installation are not command bodies in this table.
Route those requests to [`vault-setup.md`](vault-setup.md) or
[`hooks-and-project-vaults.md`](hooks-and-project-vaults.md).
