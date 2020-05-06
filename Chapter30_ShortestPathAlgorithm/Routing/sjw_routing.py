import sys
import os
import heapq

# freopen equivalent
abs_dir = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(abs_dir, "input.txt"), "r")


# use dijkstra algorithm to find shortest path from 0 to (n-1)
def solution(n, m, adj_list):
    dist = [float("inf")] * n
    dist[0] = 1.0
    heap = [(1.0, 0)] # (cost, start)

    while heap:
        curr_cost, src = heapq.heappop(heap)
        if dist[src] < curr_cost:
            continue

        for (dst, weight) in adj_list[src].items():
            next_cost = curr_cost * weight
            if next_cost < dist[dst]:
                dist[dst] = next_cost
                heapq.heappush(heap, (next_cost, dst))

    print('%.10f' % (dist[-1]))
    # answer = str(round(dist[-1], 10)) + "\n"
    # sys.stdout.write(answer)


def readline():
    return sys.stdin.readline()

if __name__ == "__main__":
    for _ in range(int(readline())):
        n, m = [int(x) for x in readline().split()]
        adj_list = [{} for _ in range(n)]
        for _ in range(m):
            a, b, c = readline().split()
            a, b, c = int(a), int(b), float(c)
            adj_list[a][b] = c  # (dst, weight)
            # adj_list[b][a] = c  # (dst, weight)

        solution(n, m, adj_list)
