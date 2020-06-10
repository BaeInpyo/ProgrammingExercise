import sys
import os

# freopen equivalent
abs_dir = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(abs_dir, "input.txt"), "r")

def readline():
    return sys.stdin.readline()

def do_floyd(graph, V, delays):
    """
    When doing floyd, apply weights on node.
    We can change order of iterate to anyway. So change it to sorted order of
    weight of each node    
    """

    dist = [[float("inf")]*(V+1) for _ in range(V+1)]
    delayed_dist = [[float("inf")]*(V+1) for _ in range(V+1)]

    delays = [(delay, idx+1) for (idx, delay) in enumerate(delays)]
    delays = sorted(delays) # change order of iteration

    # set edge weight
    for i in range(1, V+1):
        for j in range(1, V+1):
            if i==j:
                dist[i][j] = 0
            elif i in graph and j in graph[i]:
                dist[i][j] = graph[i][j]

    # do floyd algorithm
    for k in range(V):
        delay, k = delays[k]
        for i in range(1, V+1):
            for j in range(1, V+1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                delayed_dist[i][j] = min(delayed_dist[i][j], dist[i][k] + dist[k][j] + delay)

    return delayed_dist


if __name__ == "__main__":
    V, E = [int(x) for x in readline().split()]
    delays = [int(x) for x in readline().split()]
    graph = dict()
    for _ in range(E):
        # consider both direction, i.e, u->v and v->u
        u, v, w = [int(x) for x in readline().split()]
        if u in graph:
            if v in graph[u]:
                graph[u][v] = min(graph[u][v], w)
            else:
                graph[u][v] = w
        else:
            graph[u] = { v: w }

        if v in graph:
            if u in graph[v]:
                graph[v][u] = min(graph[v][u], w)
            else:
                graph[v][u] = w
        else:
            graph[v] = { u: w }

    dist = do_floyd(graph, V, delays)
    for _ in range(int(readline())):
        u, v = [int(x) for x in readline().split()]
        sys.stdout.write(str(dist[u][v]) + "\n")
