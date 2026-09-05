# Vault access and setup

Read this reference only for first-time access, installation, vault bootstrap,
presets, or assistant mode. Ordinary reads and writes use the core skill and do
not need this setup material.

## Access an existing vault

Use the first already configured method that satisfies the request:

1. Session-start context when `hooks/load_vault_context.py` already injected the
   selected vault's `_CLAUDE.md`.
2. A configured Obsidian MCP server with the required read or write primitive.
3. Direct filesystem access to the selected vault path.

Do not install or reconfigure an MCP server merely because filesystem access is
available. If the user asks for MCP setup, follow the connector documentation
under `integrations/obsidian-mcp-server/`.

Read `_CLAUDE.md` from the selected vault before operating. If it does not
exist, inventory folders and templates and read two or three representative
notes before proposing one. Do not create it without the user's request or an
explicit command procedure.

## Bootstrap a new vault

Use the repository scripts rather than manually recreating their output:

```bash
# Interactive install and bootstrap
bash scripts/quick-install.sh

# Direct bootstrap
python scripts/bootstrap_vault.py --path /path/to/vault --name "Your Name"

# Optional preset
python scripts/bootstrap_vault.py --path /path/to/vault --name "Your Name" --preset builder

# Assistant mode
python scripts/bootstrap_vault.py --path /path/to/vault --name "Your Name" \
  --mode assistant --subject "Subject Name"
```

Available presets are `executive`, `builder`, `creator`, and `researcher`.
Omitting a preset creates the general-purpose wiki-style vault. Assistant mode
uses [`claude-md-assistant-template.md`](claude-md-assistant-template.md) for a
vault maintained on someone else's behalf.

Before running bootstrap:

- confirm the exact target path and that creating or populating it is within the
  request;
- inspect an existing target instead of overwriting it;
- do not place a fallback vault under the current repository;
- preserve any existing notes and stop on an unsafe collision.

For the generated structure, frontmatter, naming, and templates, read
[`vault-schema.md`](vault-schema.md). To generate operating guidance for an
existing vault, use [`claude-md-template.md`](claude-md-template.md) and the
canonical `/obsidian-init` procedure.

## After setup

Confirm the generated files, validate a representative note against
[`ai-first-rules.md`](ai-first-rules.md), and configure only the access method
the user requested. Hook and per-project configuration belongs in
[`hooks-and-project-vaults.md`](hooks-and-project-vaults.md).
