"""End-to-end tests for cli-anything-dify-workflow.

These tests exercise a full workflow lifecycle:
  create → edit → validate → inspect → export
All operations are file-based; no external backend is needed.
"""

from __future__ import annotations

import json

import pytest
from click.testing import CliRunner

from cli_anything.dify_workflow.dify_workflow_cli import cli


@pytest.fixture
def runner():
    return CliRunner()


class TestWorkflowLifecycle:
    """Full lifecycle: create → add node → add edge → validate → export."""

    def test_full_workflow_lifecycle(self, runner, tmp_path):
        wf = str(tmp_path / "workflow.yaml")
        export_path = str(tmp_path / "exported.yaml")

        # 1. Create
        result = runner.invoke(cli, [
            "create", "--template", "llm", "-o", wf, "-j",
        ])
        assert result.exit_code == 0, result.output
        info = json.loads(result.output)
        assert info["status"] == "created"
        assert info["mode"] == "workflow"

        # 2. Inspect
        result = runner.invoke(cli, ["inspect", wf, "-j"])
        assert result.exit_code == 0, result.output

        # 3. Add a code node
        result = runner.invoke(cli, [
            "edit", "add-node", "-f", wf,
            "--type", "code", "--title", "Process Data", "-j",
        ])
        assert result.exit_code == 0, result.output
        node_info = json.loads(result.output)
        new_node_id = node_info["node_id"]

        # 4. Validate
        result = runner.invoke(cli, ["validate", wf])
        assert result.exit_code == 0, result.output

        # 5. Export
        result = runner.invoke(cli, [
            "export", wf, "--output", export_path,
        ])
        assert result.exit_code == 0, result.output

    def test_chatflow_lifecycle(self, runner, tmp_path):
        wf = str(tmp_path / "chatflow.yaml")

        # Create chatflow
        result = runner.invoke(cli, [
            "create", "--mode", "chatflow", "-o", wf, "-j",
        ])
        assert result.exit_code == 0, result.output

        # Validate
        result = runner.invoke(cli, ["validate", wf])
        assert result.exit_code == 0, result.output

        # Inspect with mermaid
        result = runner.invoke(cli, ["inspect", wf, "--mermaid"])
        assert result.exit_code == 0, result.output

    def test_chat_app_lifecycle(self, runner, tmp_path):
        f = str(tmp_path / "chat.yaml")

        result = runner.invoke(cli, [
            "create", "--mode", "chat", "--name", "Test Bot", "-o", f, "-j",
        ])
        assert result.exit_code == 0, result.output

        result = runner.invoke(cli, ["validate", f])
        assert result.exit_code == 0, result.output

    def test_agent_app_lifecycle(self, runner, tmp_path):
        f = str(tmp_path / "agent.yaml")

        result = runner.invoke(cli, [
            "create", "--mode", "agent", "-o", f, "-j",
        ])
        assert result.exit_code == 0, result.output

        result = runner.invoke(cli, ["validate", f])
        assert result.exit_code == 0, result.output

    def test_completion_app_lifecycle(self, runner, tmp_path):
        f = str(tmp_path / "completion.yaml")

        result = runner.invoke(cli, [
            "create", "--mode", "completion", "-o", f, "-j",
        ])
        assert result.exit_code == 0, result.output

        result = runner.invoke(cli, ["validate", f])
        assert result.exit_code == 0, result.output


class TestEditOperations:
    """Test edit node/edge operations end-to-end."""

    def test_add_and_remove_node(self, runner, tmp_path):
        wf = str(tmp_path / "wf.yaml")
        runner.invoke(cli, ["create", "-o", wf])

        # Add node
        result = runner.invoke(cli, [
            "edit", "add-node", "-f", wf,
            "--type", "code", "--title", "MyCode", "-j",
        ])
        assert result.exit_code == 0, result.output
        node_id = json.loads(result.output)["node_id"]

        # Remove node
        result = runner.invoke(cli, [
            "edit", "remove-node", "-f", wf, "--id", node_id, "-j",
        ])
        assert result.exit_code == 0, result.output

    def test_set_title(self, runner, tmp_path):
        wf = str(tmp_path / "wf.yaml")
        runner.invoke(cli, ["create", "-o", wf])

        # Add a node
        result = runner.invoke(cli, [
            "edit", "add-node", "-f", wf,
            "--type", "code", "--title", "Old Title", "-j",
        ])
        node_id = json.loads(result.output)["node_id"]

        # Set new title
        result = runner.invoke(cli, [
            "edit", "set-title", "-f", wf,
            "--id", node_id, "--title", "New Title", "-j",
        ])
        assert result.exit_code == 0, result.output


class TestLayoutCommand:
    """Test layout auto-arrangement."""

    def test_layout_tree(self, runner, tmp_path):
        wf = str(tmp_path / "wf.yaml")
        runner.invoke(cli, ["create", "--template", "llm", "-o", wf])

        result = runner.invoke(cli, [
            "layout", wf, "--strategy", "tree",
        ])
        assert result.exit_code == 0, result.output


class TestDiffCommand:
    """Test diff between two files."""

    def test_diff_identical(self, runner, tmp_path):
        f1 = str(tmp_path / "a.yaml")
        f2 = str(tmp_path / "b.yaml")
        runner.invoke(cli, ["create", "-o", f1])
        runner.invoke(cli, ["create", "-o", f2])

        result = runner.invoke(cli, ["diff", f1, f2])
        assert result.exit_code == 0
