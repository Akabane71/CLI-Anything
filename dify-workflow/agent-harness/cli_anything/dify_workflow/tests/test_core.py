"""Unit tests for cli-anything-dify-workflow (no backend needed)."""

from __future__ import annotations

import pytest
from click.testing import CliRunner

from cli_anything.dify_workflow.dify_workflow_cli import cli


@pytest.fixture
def runner():
    return CliRunner()


class TestCLIBasics:
    """Test CLI entry point and help output."""

    def test_help(self, runner):
        result = runner.invoke(cli, ["--help"])
        assert result.exit_code == 0
        assert "Dify Workflow DSL editor" in result.output

    def test_version(self, runner):
        result = runner.invoke(cli, ["--version"])
        assert result.exit_code == 0
        assert "0.1.0" in result.output

    def test_no_args_shows_help(self, runner):
        result = runner.invoke(cli, [])
        assert result.exit_code == 0
        assert "QUICK START" in result.output or "Usage" in result.output


class TestGuide:
    """Test the guide command."""

    def test_guide_text(self, runner):
        result = runner.invoke(cli, ["guide"])
        assert result.exit_code == 0

    def test_guide_json(self, runner):
        result = runner.invoke(cli, ["guide", "-j"])
        assert result.exit_code == 0
        assert '"steps"' in result.output


class TestListNodeTypes:
    """Test the list-node-types command."""

    def test_list_all(self, runner):
        result = runner.invoke(cli, ["list-node-types"])
        assert result.exit_code == 0

    def test_list_json(self, runner):
        result = runner.invoke(cli, ["list-node-types", "-j"])
        assert result.exit_code == 0
        assert '"node_types"' in result.output

    def test_list_single_type(self, runner):
        result = runner.invoke(cli, ["list-node-types", "--type", "llm"])
        assert result.exit_code == 0

    def test_list_unknown_type(self, runner):
        result = runner.invoke(cli, ["list-node-types", "--type", "nonexistent"])
        assert result.exit_code != 0


class TestCreate:
    """Test the create command."""

    def test_create_minimal(self, runner, tmp_path):
        outfile = str(tmp_path / "test.yaml")
        result = runner.invoke(cli, ["create", "-o", outfile])
        assert result.exit_code == 0

    def test_create_llm_template(self, runner, tmp_path):
        outfile = str(tmp_path / "llm.yaml")
        result = runner.invoke(cli, [
            "create", "--template", "llm", "-o", outfile,
        ])
        assert result.exit_code == 0

    def test_create_chatflow(self, runner, tmp_path):
        outfile = str(tmp_path / "chatflow.yaml")
        result = runner.invoke(cli, [
            "create", "--mode", "chatflow", "-o", outfile,
        ])
        assert result.exit_code == 0

    def test_create_chat(self, runner, tmp_path):
        outfile = str(tmp_path / "chat.yaml")
        result = runner.invoke(cli, [
            "create", "--mode", "chat", "-o", outfile,
        ])
        assert result.exit_code == 0

    def test_create_json_output(self, runner, tmp_path):
        outfile = str(tmp_path / "test.yaml")
        result = runner.invoke(cli, ["create", "-o", outfile, "-j"])
        assert result.exit_code == 0
        assert '"status"' in result.output


class TestValidate:
    """Test the validate command."""

    def test_validate_created_workflow(self, runner, tmp_path):
        outfile = str(tmp_path / "wf.yaml")
        runner.invoke(cli, ["create", "-o", outfile])
        result = runner.invoke(cli, ["validate", outfile])
        assert result.exit_code == 0


class TestInspect:
    """Test the inspect command."""

    def test_inspect_created_workflow(self, runner, tmp_path):
        outfile = str(tmp_path / "wf.yaml")
        runner.invoke(cli, ["create", "-o", outfile])
        result = runner.invoke(cli, ["inspect", outfile])
        assert result.exit_code == 0

    def test_inspect_json(self, runner, tmp_path):
        outfile = str(tmp_path / "wf.yaml")
        runner.invoke(cli, ["create", "-o", outfile])
        result = runner.invoke(cli, ["inspect", outfile, "-j"])
        assert result.exit_code == 0
