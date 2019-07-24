import sys


def solution(arr, N, S):
    """
    After check example inputs, you can think that we can get answer by
    - sort original array ascending order
    - then split array into S chunks that can minimize squared error

    Let's consider cache[i][j] is 'minimum sum of squared error of j chunks of ARR[i:]'.
    Then cache[i][j] = min of (min_square(ARR[i:k]) + cache[k][j-1]) for k in range [i+1, N-j]
    Our target is, therefore, cache[0][S]

    Since we cannot memorize array itself as index of cache, we use start position of array, 'i', as index.

    Additionally I define 3 more caches, 'sum_arr' and 'sum_square_arr', 'min_square' to calculate min_square quickly.
    'sum_arr' is array of length N and 'sum_arr[i]' is sum of sorted array [a0, a1, ... ai].
    'sum_square_arr' is also array of length N and 'sum_square_arr[i]' is squared sum of sorted [a0^2, a1^2, ... ai^2].
    For example, if arr = [1, 2, 3], then sum_square_arr = [1, (1+2), (1+2+3)] and sum_square_arr = [1, (1+4), (1+4+9)].

    min_square[i][j] = minimum squared error of [ai, ... aj] where 0 <= i < N and i <= j < N

    :param N:   length of integer array
    :param S:   maximum number of chunck
    :return:    minimum sum of splited chunk
    """
    if S >= N:
        return 0

    arr.sort()  # sort original array ascending order

    cache = [[None for _ in range(S+1)] for _ in range(N)]
    sum_arr, sum_square_arr, min_square =[0] * N, [0] * N, [[None] * (N) for _ in range(N)]

    # initialize sum_arr, sum_square_arr
    accumulated, accumulated_sq = 0, 0
    for i in range(N):
        accumulated += arr[i]
        accumulated_sq += (arr[i] * arr[i])
        sum_arr[i] = accumulated
        sum_square_arr[i] = accumulated_sq

    # initialize min_square
    for i in range(N):
        for j in range(i, N):
            if i == 0:
                avg = int((sum_arr[j] / (j+1)) + 0.5)
                min_square[i][j] = sum_square_arr[j] - 2 * avg * (sum_arr[j]) + (j+1) * avg * avg
            else:
                avg = int(((sum_arr[j] - sum_arr[i-1]) / (j-i+1)) + 0.5)
                min_square[i][j] = sum_square_arr[j] - sum_square_arr[i-1] - 2 * avg * (sum_arr[j] - sum_arr[i-1]) \
                + (j-i+1) * avg * avg

    # initialize cache
    # case: S=1
    for i in range(N):
        cache[i][1] = min_square[i][N-1]

    # initialize cache
    # case: if N=S, cache[n][s] = 0
    for i in range(1, S+1):
        cache[N-i][i] = 0

    for j in range(2, S+1):
        for i in range(N-j):
            cand = [ min_square[i][k-1] + cache[k][j - 1] for k in range(i + 1, N - j + 2) ]
            cache[i][j] = min(cand)

    return cache[0][S]


if __name__ == '__main__':
    # freopen equivalent
    sys.stdin = open('input.txt', 'r')

    C = int(sys.stdin.readline().strip())
    answers = []

    for _ in range(C):
        N, S = map(int, sys.stdin.readline().strip().split())
        arr = list(map(int, sys.stdin.readline().strip().split()))
        answers.append(solution(arr, N, S))

    for a in answers:
        sys.stdout.write('{}\n'.format(a))
