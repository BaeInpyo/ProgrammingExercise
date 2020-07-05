
def network_flow(cap):
    source, sink = 0, 1
    max_flow = 0
    while True:
        # bfs to find parents
        parent = [-1] * len(cap)
        queue = [source]
        parent[source] = source
        while queue and parent[sink] == -1:
            u = queue.pop(0)
            for i, v in enumerate(cap[u]):
                if v > 0 and parent[i] == -1:
                    queue.append(i)
                    parent[i] = u

        # if no path to sink
        if parent[sink] == -1: break

        # bottleneck flow in path
        path_flow = float("inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, cap[parent[s]][s])
            s = parent[s]
        
        max_flow += path_flow

        # update cap
        s = sink
        while s != source:
            cap[parent[s]][s] -= path_flow
            cap[s][parent[s]] += path_flow
            s = parent[s]

    return max_flow
        

for _ in range(int(input())):
    n, m = map(int, input().split())
    wins = [int(x) for x in input().split()]
    max_wins = max(wins[1:])
    size = n+m+2
    cap = [[0] * size for _ in range(size)]
    for i in range(m):
        cap[0][2+i] = 1 # 0 to ith match
        a, b = map(int, input().split())
        cap[2+i][2+m+a] = cap[2+i][2+m+b] = 1 # ith match to a, b
    
    w = wins[0]
    # X to 1
    cap[2+m][1] = 0
    for i in range(1, n):
        cap[2+m+i][1] = w - wins[i] - 1

    # cannot force to flow thru X
    ret = -1
    tot_flow = 0
    for _ in range(m+1):
        if max_wins < w:
            tot_flow += network_flow(cap)
            if tot_flow == m and cap[2+m][1] == 0:
                ret = w
                break
        for i in range(n):
            cap[2+m+i][1] += 1
        w += 1

    print(ret)
