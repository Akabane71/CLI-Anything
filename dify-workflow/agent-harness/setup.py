"""Setup for cli-anything-dify-workflow — Dify workflow DSL editing CLI."""

from setuptools import setup, find_namespace_packages

setup(
    name="cli-anything-dify-workflow",
    version="0.1.0",
    description="CLI for creating, editing, validating, and exporting Dify workflow DSL files",
    long_description=open("DIFY_WORKFLOW.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Akabane71",
    python_requires=">=3.12",
    packages=find_namespace_packages(include=["cli_anything.*"]),
    install_requires=[
        "dify-ai-workflow-tools>=0.1.0",
    ],
    extras_require={
        "dev": ["pytest>=7.0"],
    },
    entry_points={
        "console_scripts": [
            "cli-anything-dify-workflow=cli_anything.dify_workflow.dify_workflow_cli:cli",
        ],
    },
    package_data={
        "cli_anything.dify_workflow": ["skills/*.md"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
