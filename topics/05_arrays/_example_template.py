"""
Problem  : XXXX — Example Problem
Topic    : Arrays
Link     : https://codeforces.com/problemset/problem/XXXX/A
Difficulty: 800

--- Problem Statement ---
Given an array of n integers, find the maximum element.

--- Constraints ---
- 1 ≤ n ≤ 10^5
- -10^9 ≤ a[i] ≤ 10^9

--- Approach ---
Linear scan — iterate through the array once, tracking the max.

--- Complexity ---
- Time  : O(n)
- Space : O(1)
"""

import sys
input = sys.stdin.readline   # faster input for competitive programming


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    print(max(a))


def main():
    t = 1
    # t = int(input())   # Uncomment if multiple test cases
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
