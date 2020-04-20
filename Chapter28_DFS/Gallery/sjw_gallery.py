"""
We can think of gallery as node and hollway as edge.
We will install camera on nodes so that it's adjacent nodes are watched.
To minimize number of installed cameras, we will do dfs from all nodes, then
install camera only if there is child node that is not watched.
We also have to consider a case that all children nodes are watched but current
node is not watched. (See has_parent parameter in dfs())
Below is helpful test cases
4 3
0 1
2 3
3 4

9 8
0 1
1 2
2 3
3 4
0 5
5 6
6 7
7 8
"""

import os
import sys

abs_dir = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(abs_dir, "input.txt"), "r")


def solution(g, h, hollways):
    def dfs(here, adj, visited, watched, has_parent):
        """ start dfs from here then return number of installed camera """
        if here in visited: # here is already visited
            return 0

        visited.add(here)   # mark as visited

        children = set.difference(adj[here], visited)
        ret = sum([dfs(child, adj, visited, watched, True) \
                   for child in children])

        # install camera here if
        # 1. There is unwatched child
        # 2. here does not have parent and here is not watched
        if set.difference(children, watched) or \
           ((not has_parent) and (here not in watched)):
            ret += 1    # insert camera here
            watched.add(here)
            watched.update(adj[here])
        return ret

    adj = [set() for _ in range(g)]
    visited, watched = set(), set()
    for start, end in hollways:
        adj[start].add(end)
        adj[end].add(start)

    ret = sum([dfs(i, adj, visited, watched, False) for i in range(g)])
    print(ret)


if __name__ == "__main__":
    for _ in range(int(input())):
        G, H = [int(x) for x in sys.stdin.readline().split()]
        hollways = [None] * H
        for idx in range(H):
            hollways[idx] = [int(x) for x in sys.stdin.readline().split()]

        solution(G, H, hollways)
