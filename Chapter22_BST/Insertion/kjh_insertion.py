for _ in range(int(input())):
    arr = list(range(1, int(input())+1))
    ret = []
    for i in reversed(list(map(int, input().split()))):
        ret.append(arr.pop(-i-1))
    print(*reversed(ret))
