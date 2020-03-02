for _ in range(int(input())):
    array = list(range(int(input())))
    for i, shifts in enumerate(map(int, input().split())):
        for j in range(i, i-shifts, -1):
            array[j], array[j-1] = array[j-1], array[j]
    ret = [0] * len(array)
    for i, val in enumerate(array):
        ret[val] = i+1
    print(*ret)
