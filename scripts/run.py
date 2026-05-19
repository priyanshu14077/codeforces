#!/usr/bin/env python3
"""
run.py — Execute a Codeforces solution with stdin input.

Usage:
    python scripts/run.py <path_to_solution.py>

Example:
    python scripts/run.py topics/05_arrays/1234A_beautiful_array.py

After the script runs, enter your test input line by line.
Press Ctrl+D (macOS/Linux) or Ctrl+Z then Enter (Windows) to signal EOF.
"""

import sys
import os
import subprocess
import time


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/run.py <path_to_solution.py>")
        print("Example: python scripts/run.py topics/05_arrays/1234A_solution.py")
        sys.exit(1)

    solution_path = sys.argv[1]

    if not os.path.exists(solution_path):
        print(f"❌ File not found: {solution_path}")
        sys.exit(1)

    if not solution_path.endswith(".py"):
        print(f"❌ Only Python (.py) files are supported.")
        sys.exit(1)

    print(f"🚀 Running: {solution_path}")
    print("─" * 50)
    print("📥 Enter your input below (Ctrl+D when done):")
    print("─" * 50)

    # Read all input upfront
    try:
        user_input = sys.stdin.read()
    except KeyboardInterrupt:
        print("\n⚠️  Interrupted.")
        sys.exit(1)

    print("─" * 50)
    print("📤 Output:")
    print("─" * 50)

    start = time.perf_counter()
    result = subprocess.run(
        [sys.executable, solution_path],
        input=user_input,
        text=True,
        capture_output=True,
    )
    elapsed = time.perf_counter() - start

    if result.stdout:
        print(result.stdout, end="")

    if result.stderr:
        print("─" * 50)
        print("⚠️  Stderr / Errors:")
        print(result.stderr, end="")

    print("─" * 50)
    status = "✅ Exited OK" if result.returncode == 0 else f"❌ Exit code {result.returncode}"
    print(f"{status}  |  ⏱ Time: {elapsed*1000:.2f} ms")


if __name__ == "__main__":
    main()
