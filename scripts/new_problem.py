#!/usr/bin/env python3
"""
new_problem.py — Scaffold a new Codeforces problem solution file.

Usage:
    python scripts/new_problem.py

Follow the prompts to specify the topic, problem ID, and name.
"""

import os
import sys
from datetime import date

TOPICS = {
    "1":  ("01_introduction_to_cpp", "Introduction to C++"),
    "2":  ("02_loops", "Loops"),
    "3":  ("03_pattern_printing", "Pattern Printing"),
    "4":  ("04_functions", "Functions"),
    "5":  ("05_arrays", "Arrays"),
    "6":  ("06_2d_arrays", "2D Arrays"),
    "7":  ("07_strings", "Strings"),
    "8":  ("08_sorting_and_searching", "Sorting and Searching"),
    "9":  ("09_sets_and_maps", "Sets and Maps"),
    "10": ("10_prefix_sums", "Prefix Sums and Contribution"),
    "11": ("11_sliding_window_two_pointers", "Sliding Window and Two Pointers"),
    "12": ("12_binary_search", "Binary Search"),
    "13": ("13_number_theory", "Number Theory (Basics)"),
    "14": ("14_bit_manipulation", "Bit Manipulation"),
    "15": ("15_recursion", "Recursion"),
    "16": ("16_backtracking", "Backtracking"),
    "17": ("17_mixed_practice", "Mixed Practice"),
    "c1": ("../contests/contest_1", "Contest I"),
    "c2": ("../contests/contest_2", "Contest II"),
    "c3": ("../contests/contest_3", "Contest III"),
    "c4": ("../contests/contest_4", "Contest IV"),
    "c5": ("../contests/contest_5", "Contest V"),
}

TEMPLATE = '''"""
Problem  : {problem_id} — {problem_name}
Topic    : {topic_name}
Link     : {link}
Difficulty: {difficulty}
Date     : {date}

--- Problem Statement ---
(Paste the problem statement here)

--- Constraints ---
- 

--- Approach ---
(Describe your approach here)

--- Complexity ---
- Time  : O()
- Space : O()
"""

import sys
input = sys.stdin.readline   # faster input


def solve():
    # TODO: Write your solution here
    pass


def main():
    t = 1
    # t = int(input())   # Uncomment if multiple test cases
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
'''


def choose_topic():
    print("\n📚 Choose a topic:")
    print("─" * 40)
    for key, (_, name) in TOPICS.items():
        prefix = "🏆 Contest" if key.startswith("c") else f"  {key:>2}."
        print(f"  {prefix}  {name}")
    print("─" * 40)
    while True:
        choice = input("Enter number (e.g. 5 or c1): ").strip().lower()
        if choice in TOPICS:
            return TOPICS[choice]
        print("  ❌ Invalid choice, try again.")


def main():
    # Determine repo root (one level up from scripts/)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)

    print("🆕 New Problem Scaffold")
    print("=" * 40)

    folder_rel, topic_name = choose_topic()

    problem_id = input("\nProblem ID (e.g. 1234A): ").strip()
    problem_name = input("Problem Name (e.g. Beautiful Array): ").strip()
    link = input("Codeforces Link (press Enter to skip): ").strip() or "https://codeforces.com"
    difficulty = input("Difficulty (e.g. 800 / 1000 / 1200): ").strip() or "?"

    # Build filename
    safe_name = problem_name.lower().replace(" ", "_")
    filename = f"{problem_id}_{safe_name}.py"

    # Resolve folder path
    if folder_rel.startswith("../"):
        folder_path = os.path.join(repo_root, folder_rel[3:])
    else:
        folder_path = os.path.join(repo_root, "topics", folder_rel)

    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, filename)

    if os.path.exists(file_path):
        print(f"\n⚠️  File already exists: {file_path}")
        overwrite = input("Overwrite? (y/N): ").strip().lower()
        if overwrite != "y":
            print("Aborted.")
            sys.exit(0)

    content = TEMPLATE.format(
        problem_id=problem_id,
        problem_name=problem_name,
        topic_name=topic_name,
        link=link,
        difficulty=difficulty,
        date=date.today().isoformat(),
    )

    with open(file_path, "w") as f:
        f.write(content)

    rel = os.path.relpath(file_path, repo_root)
    print(f"\n✅ Created: {rel}")
    print(f"   Run it with: python scripts/run.py {rel}")


if __name__ == "__main__":
    main()
