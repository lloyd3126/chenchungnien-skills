#!/usr/bin/env python3
"""Small wrapper for the tw-stock CLI.

This script is intentionally thin: the repository CLI remains the source of
truth, and the skill can call this helper when it wants predictable defaults.
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import shutil
import subprocess
import sys


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("dataset")
    parser.add_argument("--date")
    parser.add_argument("--year")
    parser.add_argument("--month")
    parser.add_argument("--quarter")
    parser.add_argument("--market")
    parser.add_argument("--foreign")
    parser.add_argument("--format", default="jsonl")
    parser.add_argument("--limit")
    parser.add_argument("--columns")
    parser.add_argument("--output")
    parser.add_argument("--schema-only", action="store_true")
    parser.add_argument("--source-url-only", action="store_true")
    args = parser.parse_args()

    command = base_command() + ["fetch", args.dataset, "--format", args.format]
    for flag in [
        "date",
        "year",
        "month",
        "quarter",
        "market",
        "foreign",
        "limit",
        "columns",
        "output",
    ]:
        value = getattr(args, flag)
        if value:
            command.extend([f"--{flag}", str(value)])

    for flag in ["schema_only", "source_url_only"]:
        if getattr(args, flag):
            command.append(f"--{flag.replace('_', '-')}")

    return subprocess.call(command)


def base_command() -> list[str]:
    if shutil.which("tw-stock"):
        return ["tw-stock"]
    if not shutil.which("uv"):
        raise SystemExit(
            "tw-stock CLI is not available. Install tw-stock or install uv and provide TW_STOCK_CLI_DIR."
        )

    project_root = find_cli_project_root()
    if project_root:
        return ["uv", "run", "--project", str(project_root), "tw-stock"]

    return ["uv", "run", "tw-stock"]


def find_cli_project_root() -> Path | None:
    env_root = os.environ.get("TW_STOCK_CLI_DIR")
    if env_root:
        return Path(env_root).expanduser().resolve()

    for directory in [Path.cwd(), *Path.cwd().parents]:
        if (directory / "tw_stock_cli").is_dir() and (
            directory / "pyproject.toml"
        ).is_file():
            return directory

    return None


if __name__ == "__main__":
    sys.exit(main())
