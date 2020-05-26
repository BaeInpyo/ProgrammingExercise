import sys
import os
import heapq

# freopen equivalent
abs_dir = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(abs_dir, "input.txt"), "r")


def solution(V, E, places, stations, graph):
    """
    Use dijkstra algorithm to find shortest path to reach fire places

    V           int     number of vertices
    E           int     number of edges
    places      list    list of int that represents fire places
    stations    list    list of int that represents fire stations
    graph       dict    graph[u][v] represents weight
    """

    # initialize distance
    dist = { v: float("inf") for v in range(1, V+1) }

    # every fire station can be starting point of dijkstra
    for station in stations:
        dist[station] = 0
    heap = [(0, station) for station in stations]

    # dijkstra with heap
    while heap:
        curr_dist, u = heapq.heappop(heap)
        for v in graph[u]:
            if dist[v] > curr_dist + graph[u][v]:
                dist[v] = curr_dist + graph[u][v]
                heapq.heappush(heap, (dist[v], v))

    # dijkstra is end
    answer = sum([dist[place] for place in places])
    sys.stdout.write(str(answer) + "\n")
    return


def readline():
    return sys.stdin.readline()

if __name__ == "__main__":
    for _ in range(int(readline())):
        V, E, n, m = map(int, readline().split())
        graph = { v: dict() for v in range(1, V+1) }
        for _ in range(E):
            a, b, t = map(int, readline().split())
            graph[a][b] = t
            graph[b][a] = t

        places = list(map(int, readline().split()))
        stations = list(map(int, readline().split()))

        solution(V, E, places, stations, graph)