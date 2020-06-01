import sys
import os
from collections import defaultdict


# freopen equivalent
abs_dir = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(abs_dir, "input.txt"), "r")


def solution(positive_graph, negative_graph, V):
    """
    Find shortest/longest path from vertex 0 to 1
    Since we have to consider positive/negative cycle,
    we will use bellmanford to check if negative cycle exists.
    We can also find positive cycle by flipping sign of edge.
    """

    def bellman(graph, src, target):
        """ Return shortest path from src to target"""
        upper = [float("inf")] * V
        upper[src] = 0

        for _ in range(V-1):
            updated = False
            for u in range(V):
                for v in graph[u].keys():
                    for cost in graph[u][v]:
                        if upper[v] > upper[u] + cost:
                            upper[v] = upper[u] + cost
                            updated = True

            if not updated:
                break

        exist_cycle = False
        # check if negative cycle exists
        for _ in range(V-1):
            for u in range(V):
                for v in graph[u].keys():
                    for cost in graph[u][v]:
                        if upper[v] > upper[u] + cost:
                            upper[v] = upper[u] + cost

                            if v == 1:
                                exist_cycle = True

            if exist_cycle:
                break

        if exist_cycle:
            return "INFINITY"

        return upper[target]

    past = bellman(positive_graph, 0, 1)
    if past == float("inf"):
        # if unreachable, we don't need to check longest path
        print("UNREACHABLE")
        return
    future = bellman(negative_graph, 0, 1)
    if future != "INFINITY":
        future = -future
    print(past, future)


if __name__ == "__main__":
    for _ in range(int(input())):
        positive_graph = defaultdict(lambda: defaultdict(lambda: list()))
        negative_graph = defaultdict(lambda: defaultdict(lambda: list()))
        V, W = [int(x) for x in input().split()]
        for _ in range(W):
            a, b, d = [int(x) for x in input().split()]
            positive_graph[a][b].append(d)
            negative_graph[a][b].append(-d)

        solution(positive_graph, negative_graph, V)
