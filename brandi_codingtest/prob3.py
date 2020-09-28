"""
Bellman-Ford를 이용하여 음의 cycle detect 하는 문제
"""

def read_input():
    N, M = [int(x) for x in input().split()]
    graph = [[float("inf")] * N for _ in range(N)]
    for _ in range(M):
        A, B, C = [int(x) for x in input().split()]
        graph[A-1][B-1] = min(graph[A-1][B-1], C)

    return N, M, graph

def solution(N, M, graph):
    src, dst = 0, N-1
    dists = [float("inf")] * N
    dists[0] = 0
    cycle = False
    for count in range(N):
        for u in range(N):
            for v in range(N):
                if dists[v] > dists[u] + graph[u][v]:
                    dists[v] = dists[u] + graph[u][v]
                    if count == N-1:
                        cycle = True

    if cycle == True or dists[N-1] == float("inf"):
        print("bug")
    else:
        print(dists[N-1])


if __name__ == "__main__":
    N, M, graph = read_input()
    solution(N, M, graph)
    #print("N, M, graph:", N, M, graph)