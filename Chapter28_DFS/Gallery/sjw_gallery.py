import os
import sys

abs_dir = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(abs_dir, "input.txt"), "r")

UNWATCHED = 0
WATCHED = 1
INSTALLED = 2


def solution(g, h, hollways):
    def dfs(here, adj, visited, watched):
        """
        start dfs from here
        return number of installed camera
        - find child
        - if child is not covered, install here
        """
        if here in visited: # here is already visited
            return 0

        # print("visit:", here)
        visited.add(here)   # mark as visited

        children = set.difference(adj[here], visited)
        ret = sum([dfs(child, adj, visited, watched) for child in children])
        # ** below line is game changeer **
        if set.difference(children, watched):
        # if set.difference(adj[here], watched):
            ret += 1    # insert camera here
            watched.add(here)
            watched.update(adj[here])
            # print("insert:", here)
        return ret

    adj = [set() for _ in range(g)]
    visited, watched = set(), set()
    for start, end in hollways:
        adj[start].add(end)
        adj[end].add(start)

    ret = 0
    for i in range(g):
        ret += dfs(i, adj, visited, watched)
        if i not in watched:
            ret += 1

    print(ret)
    # print("------------------------------------------")

if __name__ == "__main__":
    for _ in range(int(input())):
        G, H = [int(x) for x in sys.stdin.readline().split()]
        hollways = [None] * H
        for idx in range(H):
            hollways[idx] = [int(x) for x in sys.stdin.readline().split()]

        solution(G, H, hollways)
