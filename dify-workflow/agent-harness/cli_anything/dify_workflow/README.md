# cli-anything-dify-workflow

CLI harness for [Dify](https://dify.ai) workflow DSL files — create, edit,
validate, layout, and export all 5 Dify application types from the terminal.

## Install

```bash
pip install git+https://github.com/HKUDS/CLI-Anything.git#subdirectory=dify-workflow/agent-harness
```

## Quick Start

```bash
# Tutorial
cli-anything-dify-workflow guide

# Create a workflow
cli-anything-dify-workflow create --mode workflow --template llm -o wf.yaml

# Inspect structure
cli-anything-dify-workflow inspect wf.yaml

# Validate
cli-anything-dify-workflow validate wf.yaml

# Edit
cli-anything-dify-workflow edit add-node -f wf.yaml --type code --title "Process"
cli-anything-dify-workflow edit add-edge -f wf.yaml --source <src> --target <dst>

# Export
cli-anything-dify-workflow export wf.yaml -o final.yaml
```

## Supported Modes

| Mode | Description |
|------|-------------|
| `workflow` | Visual node-based workflow (Start → End) |
| `chatflow` | Visual workflow with conversation |
| `chat` | Simple chatbot |
| `agent` | Chat with tool-calling |
| `completion` | Single-turn text generation |

## Requirements

- Python >= 3.12
- No external backend needed — all operations are local file-based
