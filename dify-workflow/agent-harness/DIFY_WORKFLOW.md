# Dify Workflow CLI — Harness Architecture

## Overview

The **Dify Workflow CLI** (`cli-anything-dify-workflow`) provides a stateful CLI
for creating, editing, validating, laying out, and exporting
[Dify](https://dify.ai) workflow DSL files — covering all 5 Dify application
types: Workflow, Chatflow, Chat, Agent, and Text Generation.

Built from reverse engineering of Dify frontend + backend source code for
DSL v0.6.0.

## Architecture

```
Agent ─── cli-anything-dify-workflow ─── Local YAML/JSON DSL files
                     │
                     ├── create      → Generate app from template
                     ├── edit        → Modify workflow graph nodes/edges
                     ├── config      → Edit model configuration
                     ├── validate    → Multi-layer validation
                     ├── checklist   → Frontend pre-publish checks
                     ├── inspect     → Structure view (tree/JSON/Mermaid)
                     ├── layout      → Auto-arrange node positions
                     ├── export      → Export YAML/JSON
                     ├── import      → Import + validate + re-export
                     └── diff        → Compare two DSL files
```

## Backend Requirements

- Python >= 3.12
- No external services required — all operations are local file-based

## Key Design Decisions

1. **All 5 modes**: Unlike Dify's web UI, this CLI covers every app type.
2. **Frontend-aligned validation**: Mirrors Dify's `use-checklist.ts`
   pre-publish chain so generated YAML imports without warnings.
3. **Agent-friendly**: Every command supports `--json-output` / `-j` for
   structured JSON output.
4. **Progressive discovery**: `--help` on every command includes examples,
   supported values, and next-step guidance.

## Test Strategy

- **Unit tests** (`test_core.py`): Mock-based, no backend needed.
  Tests CLI commands via Click's `CliRunner`.
- **E2E tests** (`test_full_e2e.py`): Full workflow lifecycle —
  create → edit → validate → export.
