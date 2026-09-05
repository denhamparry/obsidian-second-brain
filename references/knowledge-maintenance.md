# Knowledge maintenance

Read this reference only when a request produces a durable insight, asks the
vault to synthesize or reconcile knowledge, or needs proactive save behavior.
Named commands still route through `command-routing.md` to exactly one
canonical command procedure.

## Keep the vault alive

New information should make existing knowledge more current and connected, not
merely add another isolated note. When supported by the evidence and requested
scope:

- update related entity, concept, person, and project notes;
- reconcile stale claims while preserving their history and provenance;
- document an unresolved contradiction as an open question rather than
  choosing without evidence;
- create a synthesis only when a real cross-source pattern is present;
- preserve raw sources and link every derived claim back to them.

Use `/obsidian-reconcile` for vault-wide contradiction maintenance and
`/obsidian-synthesize` for a vault-wide search for unnamed patterns. Use
`/obsidian-emerge` for recent patterns and `/vault-deep-synthesis` for a named
topic. Select the command through the command router; do not combine their
procedures.

## Two outputs for durable insight

When an explicitly selected vault interaction produces an insight worth
keeping, provide both:

1. the user-facing answer; and
2. a concise vault update in the relevant note or notes.

The vault update is not authorization to exceed the user's request. Apply
vault-local auto-save policy, privacy boundaries, propagation rules, and the
core concurrency contract. If the interaction is read-only or the user did not
authorize a write, offer the save instead of performing it.

## Synthesis threshold

Create an automatic synthesis page only when at least three unrelated sources
support a meaningful recurring concept, reinforced claim, time-sequenced trend,
or unexpected entity connection. Record the source notes and confidence. Search
for an existing synthesis first and update it when it represents the same
pattern.

Do not force a synthesis to satisfy this behavior. A weak or single-source
observation remains an observation, and contradictory sources remain explicit.

## Proactive save reminders

When vault-local rules permit reminders, offer `/obsidian-save` after a long
insight-producing exchange, when the user signals wrap-up, or when a logical
work block completes. Ask once and do not claim anything was saved until the
selected procedure finishes and verifies its writes.
