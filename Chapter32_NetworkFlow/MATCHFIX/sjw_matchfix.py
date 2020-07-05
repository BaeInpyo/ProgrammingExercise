"""
Problem URL: https://algospot.com/judge/problem/read/MATCHFIX
"""

import os
import sys

# freopen equivalent
abs_dir = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(abs_dir, "input.txt"), "r")

def solution(N, M, wins, matches):
    pass

def networkFlow():
    """Return maximum flow"""


if __name__ == "__main__":
    for _ in range(int(input())):
        N, M = [int(x) for x in input().split()]
        wins = [int(x) for x in input().split()]
        matches = {}
        for _ in range(M):
             a, b = [int(x) for x in input().split()]
             a, b = min(a, b), max(a, b)    # a <= b
             matches[(a, b)] = matches.get((a, b), 0) + 1

        solution(N, M, wins, matches)