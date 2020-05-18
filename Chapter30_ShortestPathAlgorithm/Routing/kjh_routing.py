import heapq

for _ in range(int(input())):
    n, m = map(int, input().split())
    adj_map = {}
    for _ in range(m):
        line = input().split()
        a, b, noise = int(line[0]), int(line[1]), float(line[2])
        if a not in adj_map:
            adj_map[a] = {b: noise}
        else:
            adj_map[a][b] = noise

    dists = [1.] + [float("inf")] * (n-1)
    heap = [(1., 0)]
    # seen = set()

    while heap:
        dist, here = heapq.heappop(heap)
        if dist > dists[here]: continue
        
        for there, noise in adj_map.get(here, {}).items():
            dist = dists[here] * noise
            if dist < dists[there]:
                dists[there] = dist
                heapq.heappush(heap, (dist, there))

    print("%.10f" % dists[n-1])
