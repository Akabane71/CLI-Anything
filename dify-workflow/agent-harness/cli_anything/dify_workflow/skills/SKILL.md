---
name: cli-anything-dify-workflow
description: >
  CLI for creating, editing, validating, laying out, and exporting Dify
  workflow DSL files. Supports all 5 Dify application types: Workflow,
  Chatflow, Chat, Agent, and Text Generation.
version: 0.1.0
entrypoint: cli-anything-dify-workflow
---

# Dify Workflow CLI — Agent Skill

## Quick Start

```bash
# Install
pip install git+https://github.com/HKUDS/CLI-Anything.git#subdirectory=dify-workflow/agent-harness

# Verify
cli-anything-dify-workflow --version
```

## Command Groups

| Command | Description |
|---------|-------------|
| `guide` | Step-by-step tutorial (6 steps) |
| `list-node-types` | List all 22 supported Dify node types |
| `create` | Create a new app from template (5 modes) |
| `inspect` | View workflow structure (tree / JSON / Mermaid) |
| `validate` | Multi-layer validation (structure + node data + frontend + variables + connectivity + cycle) |
| `checklist` | Pre-publish checklist mirroring Dify frontend |
| `edit add-node` | Add a node to the workflow graph |
| `edit remove-node` | Remove a node (and connected edges) |
| `edit update-node` | Update a node's data fields via JSON |
| `edit add-edge` | Connect two nodes with an edge |
| `edit remove-edge` | Remove an edge by ID |
| `edit set-title` | Change a node's display title |
| `config` | Edit model configuration (chat/agent/completion) |
| `export` | Export workflow to YAML or JSON |
| `import` | Import, validate, and re-export a workflow |
| `diff` | Compare two workflow files |
| `layout` | Auto-layout nodes (strategies: tree, hierarchical, linear, vertical, compact) |

## Supported Application Modes

| Mode | Dify mode | Architecture |
|------|-----------|-------------|
| `workflow` | `workflow` | Start → ... → End (single execution) |
| `chatflow` | `advanced-chat` | Start → ... → Answer (multi-turn) |
| `chat` | `chat` | model_config (simple chatbot) |
| `agent` | `agent-chat` | model_config + tool_calling |
| `completion` | `completion` | model_config (single-turn) |

## Supported Node Types (22)

`start`, `end`, `answer`, `llm`, `tool`, `code`, `if-else`,
`template-transform`, `http-request`, `knowledge-retrieval`,
`question-classifier`, `parameter-extractor`, `variable-aggregator`,
`assigner`, `list-operator`, `iteration`, `loop`, `agent`,
`document-extractor`, `human-input`, `knowledge-index`, `datasource`

## Agent Guidance

- **Always** use `-j` / `--json-output` for machine-readable output.
- **Discovery**: Run `cli-anything-dify-workflow --help` to list all commands.
  Use `<command> --help` for detailed usage, examples, and next steps.
- **Typical workflow**:
  1. `create -o app.yaml --mode workflow --template llm`
  2. `inspect app.yaml -j` → see current structure
  3. `edit add-node -f app.yaml --type code --title "Process"`
  4. `edit add-edge -f app.yaml --source <src> --target <new_id>`
  5. `validate app.yaml -j` → check for errors
  6. `export app.yaml -o final.yaml`
- **Errors**: Non-zero exit code + human-readable message on stderr.
  With `-j`, error details are included in JSON output.
- **No backend required**: All operations are local file-based.
