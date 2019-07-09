import sys


'''
- level을 구하기 위해 list slicing을 매번 하는 것 보다 직접 숫자 3,4,5개를 인자로 넘기는 것이 더 빠름
'''


def score_3(a, b, c):
    if a == b == c:
        return 1

    if a-b == b-c == 1 or a-b == b-c == -1:
        return 2

    if a == c != b:
        return 4

    if a-b == b-c:
        return 5

    return 10


def score_4(a, b, c, d):
    if a == b == c == d:
        return 1

    if a-b == b-c == c-d == 1 or a-b == b-c == c-d == -1:
        return 2

    if a == c and b == d and a != b:
        return 4

    if a-b == b-c == c-d:
        return 5

    return 10


def score_5(a, b, c, d, e):
    if a == b == c == d == e:
        return 1

    if a-b == b-c == c-d == d-e == 1 or a-b == b-c == c-d == d-e == -1:
        return 2

    if a == c == e and b == d and a != b:
        return 4

    if a-b == b-c == c-d == d-e:
        return 5

    return 10


def pi(arr):
    N = len(arr)

    # cache[i] = min level until ith number in arr
    cache = [None] * (N+1)

    # we cannot calculate level of array with length < 3
    # initialize when length is in [3,5]
    cache[3] = score_3(arr[0], arr[1], arr[2])
    cache[4] = score_4(arr[0], arr[1], arr[2], arr[3])
    cache[5] = score_5(arr[0], arr[1], arr[2], arr[3], arr[4])

    # fill cache
    for i in range(6, N+1):
        cand = []

        # case1: sub-array with length 3
        if cache[i-3] is not None:
            cand.append(cache[i-3] + score_3(arr[i-3], arr[i-2], arr[i-1]))

        # case2: sub-array with length 4
        if cache[i-4] is not None:
            cand.append(cache[i-4] + score_4(arr[i-4], arr[i-3], arr[i-2], arr[i-1]))

        # case1: sub-array with length 5
        if cache[i-5] is not None:
            cand.append(cache[i-5] + score_5(arr[i-5], arr[i-4], arr[i-3], arr[i-2], arr[i-1]))

        cache[i] = min(cand)

    return cache[-1]


if __name__ == '__main__':

    # freopen equivalent
    # sys.stdin = open('input.txt', 'r')

    C = int(sys.stdin.readline().strip())
    answers = []

    for _ in range(C):
        line = sys.stdin.readline().strip()
        numbers = list(map(int, line))
        answers.append(pi(numbers))

    for a in answers:
        sys.stdout.write('{}\n'.format(a))