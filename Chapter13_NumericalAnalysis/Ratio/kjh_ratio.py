
if __name__ == "__main__":
    _MAX = 2000000000
    def solve(_m, _n):
        if (_m + _MAX)*100 // (_n + _MAX) == _m*100 // _n: return -1

        low, high = 0, _MAX
        while low+1 < high:
            mid = (low+high) // 2
            if _m*100 // _n == (_m+mid)*100 // (_n+mid):
                low = mid
            else:
                high = mid

        return high

    for _ in range(int(input())):
        n, m = map(int, input().split())
        ans = solve(m, n)
        print(ans)
