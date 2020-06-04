def bf_fast(edges, dist):
    for a, b, d in edges:
        if dist[a] + d < dist[b]:
            dist[b] = dist[a] + d

def bf_slow(edges, dist):
    for a, b, d in edges:
        if dist[a] + d > dist[b]:
            dist[b] = dist[a] + d


for _ in range(int(input())):
    v, w = [int(_) for _ in input().split()]
    edges = []
    for _ in range(w):
        a, b, d = [int(_) for _ in input().split()]
        edges.append((a,b,d))

    dist = {i: float("inf") for i in range(v)}
    dist[0] = 0
    for _ in range(v):
        bf_fast(edges, dist)
    ret1 = dist[1]
    for _ in range(v):
        bf_fast(edges, dist)
    if ret1 != dist[1]:
        ret1 = "INFINITY"

    dist = {i: float("-inf") for i in range(v)}
    dist[0] = 0
    for _ in range(v):
        bf_slow(edges, dist)
    ret2 = dist[1]
    for _ in range(v):
        bf_slow(edges, dist)
    if ret2 != dist[1]:
        ret2 = "INFINITY"

    if ret1 == float("inf") or ret2 == float("-inf"):
        print("UNREACHABLE")
    else:
        print(ret1, ret2)
