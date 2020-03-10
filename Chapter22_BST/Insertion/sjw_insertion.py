import sys
import os

abs_dir = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(abs_dir, "input.txt"), "r")


"""
We can found that moves[i] = numbre of k such that k < i and arr[k] < arr[i]
If we iterate moves backwords, we can find element in original list in
reverse order.

For example,
moves           idx    moves[idx]       remains             original
[0 1 1 2 3]     4      3                [1, 2, 3, 4, 5]     [2]
[0 1 1 2 3]     3      2                [1, 3, 4, 5]        [3, 2]
[0 1 1 2 3]     2      1                [1, 4, 5]           [4, 3, 2]
[0 1 1 2 3]     1      1                [1, 5]              [1, 4, 3, 2]
"""

def solution(n, moves):
    remains = list(range(1, n + 1))
    original = [0] * n
    for idx in reversed(range(1, n)):
        count = moves[idx]
        # pop (count + 1)th biggest number from remains
        original[idx] = remains.pop(-count-1)

    original[0] = remains[0]
    sys.stdout.write(" ".join([str(x) for x in original]) + "\n")


if __name__ == "__main__":
    for _ in range(int(input())):
        N = int(input())
        moves = [int(x) for x in sys.stdin.readline().strip().split()]
        solution(N, moves)
