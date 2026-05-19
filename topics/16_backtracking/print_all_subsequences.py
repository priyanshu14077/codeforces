"""
Problem  : E — Print All Subsequences
Topic    : Backtracking
Link     : (Codeforces contest group)
Difficulty: —
Date     : 2026-05-20

--- Problem Statement ---
Given an array of N distinct integers, print all non-empty subsequences.

--- Constraints ---
- 1 ≤ N ≤ 15
- 1 ≤ A[i] ≤ 1000

--- Approach ---
Classic backtracking / recursion on subsets.

At each index we have two choices:
  1. SKIP  — don't include a[index] in the current subsequence
  2. INCLUDE — add a[index] and move forward

When we reach the end (index == N), print the current subsequence
if it's non-empty. This visits all 2^N subsets.

Recursion tree for [1, 2, 3]:

                     []
              /             |
           []               [1]
         /    |           /     |
       []    [2]        [1]    [1,2]
      / |   /   |      /  |   /    |
    [] [3] [2] [2,3] [1] [1,3][1,2][1,2,3]

--- Complexity ---
- Time  : O(2^N * N)  — 2^N subsets, each up to N elements to print
- Space : O(N)        — recursion depth + current list
"""

import sys
input = sys.stdin.readline


def solve(index: int, arr: list, current: list, n: int) -> None:

    if index == n:
        if current:                         
            print(*current)
        return


    solve(index + 1, arr, current, n)


    current.append(arr[index])
    solve(index + 1, arr, current, n)
    current.pop()                          


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    solve(0, arr, [], n)


if __name__ == "__main__":
    main()
