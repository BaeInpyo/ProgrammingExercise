"""
Inspired by Dijkstra algorithm
Problem URL: https://www.acmicpc.net/problem/1753
"""

import sys
import os
import heapq


# # freopen equivalent
# abs_dir = os.path.dirname(os.path.abspath(__file__))
# sys.stdin = open(os.path.join(abs_dir, "input.txt"), "r")


def solution(adjlist, V, src):
    """
    Print shortest cost from src to every vertex using dijkstra algorithm with
    heap.

    :param: adjlist dict    adjlist[u][v] = weight between (u, v)
    :param: V       int     number of vertex (1 to V)
    :param: src     int     starting vertex
    """

    dist = [float('inf') for _ in range(V+1)]
    dist[src] = 0
    heap = [(0, src)]   # (cost, vertex)
    while heap:
        cost, u = heapq.heappop(heap)
        for v in adjlist[u].keys():
            if dist[v] > dist[u] + adjlist[u][v]:
                dist[v] = dist[u] + adjlist[u][v]
                heapq.heappush(heap, (dist[v], v))

    for u in range(1, V+1):
        if dist[u] == float("inf"):
            sys.stdout.write("INF\n")
        else:
            sys.stdout.write(str(dist[u]) + "\n")



if __name__ == "__main__":
    V, E = [int(x) for x in sys.stdin.readline().strip().split()]
    K = int(sys.stdin.readline().strip())

    # use adjacent list because V<=20,000
    adjlist = [dict() for _ in range(V+1)]
    for _ in range(E):
        u, v, w = [int(x) for x in sys.stdin.readline().strip().split()]
        adjlist[u][v] = min(adjlist[u].get(v, float("inf")), w)

    # print(adjlist)
    solution(adjlist, V, K)