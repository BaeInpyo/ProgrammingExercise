def _isin(tup1, tup2):
    dist = ((tup1[0] - tup2[0])**2 + (tup1[1] - tup2[1])**2)**(0.5)
    return dist + tup1[2] <= tup2[2]


class fortress():
    def __init__(self):
        self.depth = 1
        self.inner = {} # key: tuple, val: fortress
    
    def insert(self, _key, _fortress):
        for k, v in self.inner.items():
            if _isin(_key, k):
                _depth = v.insert(_key, _fortress)
                self.depth = max(self.depth, _depth + 1)
                return self.depth

        # inner_copy = self.inner.copy()
        # for k, v in self.inner.items():
        #     if _isin(k, _key):
        #         _fortress.insert(k, v)
        #         del inner_copy[k]
        # self.inner = inner_copy
        self.depth = max(self.depth, _fortress.depth + 1)
        self.inner[_key] = _fortress
        return self.depth

    def bfs(self):
        if self.depth == 1: return 0
        d1, d2 = 0, 0
        ret = 0
        for v in self.inner.values():
            ret = max(ret, v.bfs())
            if d2 < v.depth: d2 = v.depth
            if d2 > d1: d1, d2 = d2, d1
        return max(ret, d1 + d2)


for _ in range(int(input())):
    n = int(input())
    root = fortress()
    tuples = []
    for _ in range(n):
        tuples.append(tuple(map(int, input().split())))
    tuples.sort(key=lambda t: t[2], reverse=True)
    
    for xyr in tuples:
        _fortress = fortress()
        root.insert(xyr, _fortress)
    
    ret = next(iter(root.inner.values())).bfs()
    print(ret)
