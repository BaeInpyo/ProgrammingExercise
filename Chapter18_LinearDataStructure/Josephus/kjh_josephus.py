for _ in range(int(input())):
    n, k = map(int, input().split())
    a, i = [i+1 for i in range(n)], 0
    while len(a) > 2:
        del a[i]
        i = (i + k - 1) % len(a)
    print(min(a), max(a))
