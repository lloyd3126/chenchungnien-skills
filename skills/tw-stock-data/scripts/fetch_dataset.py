#!/usr/bin/env python3
"""Small wrapper for the tw-stock CLI.

This script is intentionally thin: the repository CLI remains the source of
truth, and the skill can call this helper when it wants predictable defaults.
"""

from __future__ import annotations

import argparse
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
    parser.add_argument("--format", default="jsonl")
    parser.add_argument("--limit")
    parser.add_argument("--output")
    args = parser.parse_args()

    command = base_command() + ["fetch", args.dataset, "--format", args.format]
    for flag in ["date", "year", "month", "quarter", "market", "limit", "output"]:
        value = getattr(args, flag)
        if value:
            command.extend([f"--{flag}", str(value)])

    return subprocess.call(command)


def base_command() -> list[str]:
    if shutil.which("tw-stock"):
        return ["tw-stock"]
    if shutil.which("uv"):
        return ["uv", "run", "tw-stock"]
    raise SystemExit("tw-stock CLI is not available. Install tw-stock or run this helper inside the tw-stock-cli project with uv.")


if __name__ == "__main__":
    sys.exit(main())
