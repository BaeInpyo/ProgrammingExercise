"""
Solve Strongly Connected Components problem inspired by https://www.youtube.com/watch?v=qz9tKlF431k.
I solved this problem with kosaraju's algorithm.
"""

import sys
import os

sys.setrecursionlimit(10**9)    # set max recursion limit

# freopen equivalent
abs_dir = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(abs_dir, "input.txt"), "r")

def readline():
    """ wrapper function for sys.stdin.readline() """
    return sys.stdin.readline()

def dfs(u, visited, adj_list, stack):
    """
    start dfs from vertex u.
    In first dfs with original graph, use stack as stack itself.
    In second dfs with reversed graph, use stack as list that contains scc.
    """
    visited[u] = True
    for v in adj_list[u]:
        if not visited[v]:
            dfs(v, visited, adj_list, stack)

    stack.append(u)
    return  # end of dfs

def solve(adj_list):
    n = len(adj_list)
    reverse_adj_list = { vertex: [] for vertex in range(1, n+1)}
    for u in adj_list:
        for v in adj_list[u]:
            reverse_adj_list[v].append(u)  # add reverse edge

    stack = []  # stack will be retrieved later
    visited = { vertex: False for vertex in range(1, n+1) }
    for u in adj_list:
        if not visited[u]:
            dfs(u, visited, adj_list, stack)

    # now stack is filled
    visited = { vertex: False for vertex in range(1, n+1) }   # reset visited
    sccs = []
    while stack:
        u = stack.pop()
        if not visited[u]:
            scc = []
            dfs(u, visited, reverse_adj_list, scc)
            sccs.append(scc)

    # sort vertex inside scc
    for scc in sccs:
        scc.sort()
        scc.append(-1)

    # sort scc
    sccs.sort(key=lambda x: x[0])
    
    sys.stdout.write(str(len(sccs)) + "\n")
    for scc in sccs:
        sys.stdout.write(" ".join([str(x) for x in scc]) + "\n")

if __name__ == "__main__":
    vertex, edge = [int(x) for x in readline().split()]
    adj_list = { vertex: [] for vertex in range(1, vertex+1)}
    for _ in range(edge):
        u, v = [int(x) for x in readline().split()]
        adj_list[u].append(v)

    solve(adj_list)