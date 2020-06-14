import sys



def solution(adj, edges, V):
    result = 0

    for edge in edges:
        if not update(adj, V, edge):
            result += 1

    return result

def update(adj, V, edge):
    a, b, c = edge
    if adj[a][b] <= c:
        return False
    for i in range(V):
        for j in range(V):
            adj[i][j] = min(adj[i][j], adj[i][a]+c+adj[b][j], adj[i][b]+c+adj[a][j])
    return True

def floyd(adj, V):
    for k in range(V):
        for i in range(V):
            for j in range(V):
                adj[i][j] = min(adj[i][j], adj[i][k]+adj[k][j])
    
    return adj
    
if __name__ == '__main__':
    sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline().rstrip())
    for _ in range(C):
        V, M, N = [int(x) for x in sys.stdin.readline().rstrip().split()]
        adj = [[float('inf')]*i+[0]+[float('inf')]*(V-i-1) for i in range(V)]
        for _ in range(M):
            a, b, c = [int(x) for x in sys.stdin.readline().rstrip().split()]
            adj[a][b] = min(adj[a][b], c)
            adj[b][a] = min(adj[b][a], c)
        
        adj = floyd(adj, V)
        edges = [[int(x) for x in sys.stdin.readline().rstrip().split()] for _ in range(N)]

        print(solution(adj, edges, V))


