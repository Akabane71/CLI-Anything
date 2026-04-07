# Test Strategy — cli-anything-dify-workflow

## Overview

| File | Type | Description |
|------|------|-------------|
| `test_core.py` | Unit | CLI commands via Click CliRunner, no backend needed |
| `test_full_e2e.py` | E2E | Full workflow lifecycle: create → edit → validate → export |

## Running Tests

```bash
# Unit tests (no backend needed)
python -m pytest cli_anything/dify_workflow/tests/test_core.py -v

# E2E tests (no backend needed — file-based operations)
python -m pytest cli_anything/dify_workflow/tests/test_full_e2e.py -v

# All tests
python -m pytest cli_anything/dify_workflow/tests/ -v
```

## Coverage

Target: 80% minimum for core commands.
