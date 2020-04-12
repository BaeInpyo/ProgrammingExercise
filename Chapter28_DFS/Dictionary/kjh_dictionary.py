def topological_sort(here, adj, visited, stack):
    neighbors = adj.get(here, set())
    visited.add(here)
    for there in neighbors:
        if there not in visited:
            topological_sort(there, adj, visited, stack)
    stack.append(here)


for _ in range(int(input())):
    adj = {}
    prev = None
    for _ in range(int(input())):
        curr = input().strip()
        if prev is not None:
            for p, c in zip(prev, curr):
                if p != c:
                    if p in adj:
                        adj[p].add(c)
                    else:
                        adj[p] = set(c)
                    break
        prev = curr
    visited, stack = set(), []
    for k in adj:
        if k not in visited:
            topological_sort(k, adj, visited, stack)
    
    stack.reverse()
    invalid = False
    for i in range(len(stack)-1):
        a = stack[i]
        for b in stack[i+1:]:
            if b in adj and a in adj[b]:
                invalid = True
    if invalid == True:
        print("INVALID HYPOTHESIS")
    else:
        print("".join(stack + [x for x in "abcdefghijklmnopqrstuvwxyz" if x not in set(stack)]))
