import heapq
from collections import defaultdict

def path(bases, targets, adj):
    dists = defaultdict(lambda: 1<<63)
    heap = []
    for b in bases:
        dists[b] = 0
        heapq.heappush(heap, (0, b))

    while heap:
        dist, here = heapq.heappop(heap)
        if dist > dists[here]: continue

        for there, weight in adj.get(here, {}).items():
            dist = dists[here] + weight
            if dist < dists[there]:
                dists[there] = dist
                heapq.heappush(heap, (dist, there))
    return [dists[t] for t in targets]


for _ in range(int(input())):
    v, e, n, m = map(int, input().split())
    adj_map = {}
    for _ in range(e):
        a, b, w = map(int, input().split())
        if a not in adj_map:
            adj_map[a] = {b: w}
        else:
            adj_map[a][b] = w
        if b not in adj_map:
            adj_map[b] = {a: w}
        else:
            adj_map[b][a] = w
    targets = [int(_) for _ in input().split()]
    bases = [int(_) for _ in input().split()]

    print(sum(path(bases, targets, adj_map)))
