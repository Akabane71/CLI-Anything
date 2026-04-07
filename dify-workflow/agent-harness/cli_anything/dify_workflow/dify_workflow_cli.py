"""cli-anything-dify-workflow — Thin wrapper that re-exports the dify-workflow CLI.

This harness wraps the existing ``dify-workflow`` CLI under the
cli-anything naming convention so it can be discovered by the CLI-Hub
and used by AI agents.

Install the upstream package first::

    pip install dify-ai-workflow-tools
"""

from __future__ import annotations

import click


@click.group(invoke_without_command=True)
@click.version_option(version="0.1.0", prog_name="cli-anything-dify-workflow")
@click.option("--json", "json_mode", is_flag=True, default=False,
              help="Force JSON output on all sub-commands (agent-friendly).")
@click.pass_context
def cli(ctx, json_mode):
    """Dify Workflow DSL editor — create, edit, validate, layout, and export
    all 5 Dify application types from the command line.

    \b
    QUICK START:
      cli-anything-dify-workflow guide             → interactive tutorial
      cli-anything-dify-workflow list-node-types    → see all 22 node types
      cli-anything-dify-workflow create -o my.yaml  → create a workflow
      cli-anything-dify-workflow inspect my.yaml    → view its structure
      cli-anything-dify-workflow validate my.yaml   → check if valid
      cli-anything-dify-workflow export my.yaml     → export to stdout
    """
    ctx.ensure_object(dict)
    ctx.obj["json_mode"] = json_mode
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())


def _register_commands():
    """Import and register all commands from the upstream dify_workflow package."""
    try:
        from dify_workflow.cli import cli as upstream_cli
    except ImportError:
        click.echo(
            "Error: dify-ai-workflow-tools is not installed.\n"
            "Install it with: pip install dify-ai-workflow-tools",
            err=True,
        )
        return

    # Re-register every command from the upstream CLI group
    for name, cmd in upstream_cli.commands.items():
        cli.add_command(cmd, name)


_register_commands()

if __name__ == "__main__":
    cli()
