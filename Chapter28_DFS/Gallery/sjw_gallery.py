import os
import sys

abs_dir = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(abs_dir, "input.txt"), "r")

UNWATCHED = 0
WATCHED = 1
INSTALLED = 2


def solution(g, h, hollways):
    def dfs(here):
        nonlocal installed
        visited[here] = True
        children = [0, 0, 0]
        for there in adj[here]:
            if not visited[there]:
                children[dfs(there)] += 1

        if children[UNWATCHED]:
            installed += 1
            return INSTALLED
        if children[INSTALLED]:
            return WATCHED
        return UNWATCHED

    visited = [False] * g
    installed = 0
    adj = [[] for _ in range(g)]
    for start, end in hollways:
        adj[start].append(end)

    for u in range(g):
        if (not visited[u]) and (dfs(u) == UNWATCHED):
            installed += 1

    print(installed)

if __name__ == "__main__":
    for _ in range(int(input())):
        G, H = [int(x) for x in sys.stdin.readline().split()]
        hollways = [None] * H
        for idx in range(H):
            hollways[idx] = [int(x) for x in sys.stdin.readline().split()]

        solution(G, H, hollways)
