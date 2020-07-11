def bipartite_match(adj, n, m):
    a_match = [-1] * n
    b_match = [-1] * m

    def dfs(a):
        if visited[a]: return False
        visited[a] = True
        for b in range(m):
            if (adj[a][b]):
                if b_match[b] == -1 or dfs(b_match[b]):
                    a_match[a] = b
                    b_match[b] = a
                    return True
        return False
    
    size = 0
    for start in range(n):
        visited = [0] * n
        if dfs(start):
            size += 1
    return size
    
def cascade_set_id(k, i, j):
    id_ = id_inc[k]
    while i < size and j < size and i >= 0 and j >= 0 \
            and grid[i][j] == '.':
        id_map[k][i][j] = id_
        i += 1
        j += 1 if k == 0 else -1

for _ in range(int(input())):
    grid = [input() for _ in range(int(input()))]

    size = len(grid)
    id_map = [[[-1] * size for _ in range(size)], [[-1] * size for _ in range(size)]]
    id_inc = [0, 0]

    for k in range(2):
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == '.' and id_map[k][i][j] == -1:
                    cascade_set_id(k, i, j)
                    id_inc[k] += 1

    n, m = id_inc
    adj = [[0] * m for _ in range(n)]
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == '.':
                a = id_map[0][i][j]
                b = id_map[1][i][j]
                adj[a][b] = 1
    
    print(bipartite_match(adj, n, m))
