def dfs(here: int):
    visited.add(here)
    if here not in adj: return 0
    neighbors = adj[here]
    
    to_visit = [there for there in neighbors if there not in visited]
    ret = sum([dfs(n) for n in to_visit])
    unwatched = {n for n in to_visit if n not in watched}
    if unwatched:
        watched.update(neighbors)
        watched.add(here)
        return ret + 1
    return ret


for _ in range(int(input())):
    g, h = map(int, input().split())
    adj, visited, watched = {}, set(), set()
    for _ in range(h):
        a, b = map(int, input().split())
        if a not in adj: adj[a] = set()
        if b not in adj: adj[b] = set()
        adj[a].add(b)
        adj[b].add(a)

    ret = 0
    for i in range(g):
        if i not in visited: # visited side effected
            ret += dfs(i)
            if i not in watched: ret += 1
    print(ret)
