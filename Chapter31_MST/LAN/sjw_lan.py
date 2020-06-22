"""
1. We can think that given graph is dense graph such that all nodes (u, v)
    are connected
2. We are given some edges already connected.
3. Our goal is to make MST with already connected edges.
4. We know 2 ways to find MST, PRIM and KRUSCAL. Time complexity of each one is
    V^2/ElogV and ElogE.
5. Since given graph is dense, we select PRIM with V^2 time complexity.
**6. To implement easier, we can set distance at (u, v) for already connected
    edges to 0.
"""

import sys
import os
import math

# freopen equivalent
abs_dir = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(abs_dir, "input.txt"), "r")

def readline():
    return [int(x) for x in sys.stdin.readline().split()]

def get_distance(x1, y1, x2, y2):
    """ return distance between (x1, y1) and (x2, y2) """
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def solution(V, xs, ys, already):
    """
    Do PRIM algorithm with time complexity of V^2.

    Args:
        V       (int)   :   number of vertices
        xs      (list)  :   x coordinates of buildings
        ys      (list)  :   y coordinates of buildings
        already (list)  :   list of already conencted buildings
    """
    # initialize graph
    graph = dict()
    for v in range(V):
        graph[v] = dict()
    for u in range(V):
        for v in range(V):
            x1, y1, x2 ,y2 = xs[u], ys[u], xs[v], ys[v]
            graph[u][v] = get_distance(x1, y1, x2, y2)

    # set distance between already selected buildings to 0
    for (u, v) in already:
        graph[u][v] = 0
        graph[v][u] = 0

    # start PRIM algorithm
    distance = [float("inf")] * V   # distance from selected vertices
    selected = [False] * V          # selected vertices

    # start from building 0
    distance[0] = 0
    selected[0] = True
    for v in range(V):
        distance[v] = min(distance[v], graph[0][v]) # update distance from 0

    answer = 0
    for _ in range(V-1):
        not_selected = [(distance[v], v) for v in range(V) if not selected[v]]
        min_dist, min_vertex = min(not_selected, key=lambda x: x[0])

        # add vertex that has minimal distance
        selected[min_vertex] = True
        answer += min_dist
        # update distance from new vertex to all other vertices
        for v in range(V):
            distance[v] = min(distance[v], graph[min_vertex][v])

    print(answer)
    return

if __name__ == "__main__":
    for _ in range(readline()[0]):
        N, M = readline()
        xs = readline()
        ys = readline()
        already = []
        for _ in range(M):
            already.append(readline())

        solution(N, xs, ys, already)
