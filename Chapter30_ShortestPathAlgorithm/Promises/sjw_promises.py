import sys
import os

# # freopen equivalent
# abs_dir = os.path.dirname(os.path.abspath(__file__))
# sys.stdin = open(os.path.join(abs_dir, "input.txt"), "r")


def readline():
    """Read input from stdin

    This function reads input from stdin and return list of int.
    We use sys.stdin.readline() instead of input() because there can be a
    huge amount of input numbers.

    Returns:
        list of int
    """
    return [int(x) for x in sys.stdin.readline().split()]


def build_graph(V, edges):
    """Return graph with given edges

    Given number of vertices and edges, return graph such that
    graph[u][v] = distance from u and v. If u and v is not connected directly,
    graph[u][v] provides float("inf").

    Args:
        V       (int):  number of vertices
        edges   (list): edges[i] consists of 3 int value which, u, v, distance
    Returns:
        graph   (dict): graph
    """
    graph = { u: dict() for u in range(V) }
    for u in range(V):
        for v in range(V):
            if u==v:
                graph[u][v] = 0
            else:
                graph[u][v] = float("inf")

    for (u, v, distance) in edges:
        graph[u][v] = distance
        graph[v][u] = distance

    return graph

def solution(graph, dist, edges):
    """Print number of unnecessary loads

    A new load (u, v, distance) can be necessary load if it satisfies among
    next conditions
    1. u and v is not connected previously
    2. distance is shorter than dist[u][v]

    We will use floyd algorithm for building dist[u][v].

    Note:
        Since we construct each load sequentially, graph becomes changed.

    Args:
        graph   (dict): dictionary that represents graph
        dist    (dict): dictionary that represents dist which is completely same
                        with graph
        edges:  (list): loads to be constructed

    Returns:
        This function does not return any value. Instead, print number of
        useless loads
    """
    V = len(graph)
    # do floyd algorithm
    for k in range(V):
        for u in range(V):
            for v in range(V):
                dist[u][v] = min(dist[u][v], dist[u][k] + dist[k][v])

    result = 0
    for (u, v, distance) in edges:
        # print(u, v, distance)
        if distance < dist[u][v]:
            dist[u][v] = distance
            """
            Since u and v are connected, we need to updated every paths
            that can pass through (u, v) or (v, u)
            """
            for start in range(V):
                for end in range(V):
                    dist[start][end] = min(
                        dist[start][end],
                        dist[start][u] + dist[u][v] + dist[v][end],
                        dist[start][v] + dist[v][u] + dist[u][end]
                    )
        else:
            result += 1

        # print("dist below")
        # for u in range(V):
        #     for v in range(V):
        #         print(u, v, dist[u][v])

    print(result)
    return

if __name__ == "__main__":
    for _ in range(readline()[0]):
        V, M, N = readline()
        prev_edges, next_edges = [], []
        for _ in range(M):
            prev_edges.append(readline())
        for _ in range(N):
            next_edges.append(readline())
        
        graph = build_graph(V, prev_edges)
        dist = build_graph(V, prev_edges)   # initail dist is same with graph
        solution(graph, dist, next_edges)
