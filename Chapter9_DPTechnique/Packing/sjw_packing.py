import sys


def solution(arr, N, W):
    # base case
    if N == 1:
        volume, value = arr[0][1], arr[0][2]

        if volume <= W:
            return value, 1, [arr[0][0]]    # return (value sum, count, item list)
        else:
            return 0, 0, []

    # arr = (name, volume, value)
    names = [x[0] for x in arr]
    arr.sort(key=lambda x: x[2] / x[1], reverse=True)   # sort by (value / volume) desc
    cache = [[[None, None] for _ in range(W+1)] for _ in range(N)]  # NxW cache, cache[i][j] = [value, 포함여부]

    # initialize cache
    for w in range(W+1):
        _, curr_volume, curr_value = arr[N-1]

        if curr_volume <= w:
            cache[N-1][w][0] = curr_value
            cache[N-1][w][1] = 1

        else:
            cache[N-1][w][0] = 0
            cache[N-1][w][1] = 0

    for n in reversed(range(N-1)):
        for w in range(W+1):
            curr_name, curr_volume, curr_value = arr[n]

            if curr_volume <= w:
                cand1 = curr_value + cache[n+1][w-curr_volume][0]
                cand2 = cache[n+1][w][0]

                if cand1 > cand2:
                    cache[n][w][0] = cand1
                    cache[n][w][1] = 1  # include this

                else:
                    cache[n][w][0] = cand2
                    cache[n][w][1] = 0  # exclude this

            else:
                cache[n][w][0] = cache[n+1][w][0]
                cache[n][w][1] = 0  # exclude this

    value_sum = cache[0][W][0]

    i, j = 0, W
    item_list = []
    while i < N and j >= 0:
        include = cache[i][j][1]
        assert include is not None, "include must not be None"

        if include == 1:
            item_list.append(arr[i][0])
            j -= arr[i][1]  # subtract volume, # 순서 주의!!!
            i += 1


        else:
            i += 1

    item_result = []
    for i in names:
        if i in item_list:
            item_result.append(i)
    return value_sum, len(item_result), item_result



if __name__ == "__main__":
    # freopen equivalent
    sys.stdin = open("input.txt", "r")

    C = int(sys.stdin.readline().strip())
    answers = []

    for _ in range(C):
        N, W = [int(x) for x in sys.stdin.readline().strip().split()]
        arr = []

        for __ in range(N):
            name, volume, value = sys.stdin.readline().strip().split()
            volume, value = int(volume), int(value)
            arr.append((name, volume, value))

        answers.append(solution(arr, N, W))

    for a in answers:
        value_sum, count, item_list = a

        if count == 0:
            sys.stdout.write("{} {}\n".format(0, 0))

        else:
            sys.stdout.write("{} {}\n".format(value_sum, count))
            for name in item_list:
                sys.stdout.write("{}\n".format(name))