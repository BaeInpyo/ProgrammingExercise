import sys


'''
- 어떻게 재귀적으로 DP를 구현할 것인지?
'''


def level(arr):
    '''

    :param arr: list of integer whose length is in [3, 5], e.g. inclusive in both side
    :return: correspnding level

    level1: every integer in arr is same
    level2: monotonically increasing or decreasing by 1
    level3: 2 integers appears alternatively
    level4: integers compose sequence with same difference, e.g. arithmetic sequence
    level5: others
    '''

    # level1: all elements are same
    if len(set(arr)) == 1:
        return 1

    # level2: monotonically increase or decrease
    a1 = arr[:-1]   # (a^1, ... a^(n-1))
    a2 = arr[1:]    # (a^2, ... a^n)
    diff = [x-y for (x, y) in zip(a1, a2)]
    if len(set(diff)) == 1 and (diff[0] == 1 or diff[0] == -1):
        return 2

    # level3: 2 integers appears alternatively
    a1 = [x[1] for x in enumerate(arr) if x[0] % 2 == 0]
    a2 = [x[1] for x in enumerate(arr) if x[0] % 2 != 0]
    if a1[0] != a2[0] and len(set(a1)) == len(set(a2)) == 1:
        return 4

    # level4: arithmetic sequence
    a1 = arr[:-1]  # (a^1, ... a^(n-1))
    a2 = arr[1:]  # (a^2, ... a^n)
    diff = [x - y for (x, y) in zip(a1, a2)]
    if len(set(diff)) == 1:
        return 5

    # level5: other cases
    return 10


def pi(arr):
    N = len(arr)

    # cache[i] = min level until ith number in arr
    cache = [None] * (N+1)

    # we cannot calculate level of array with length < 3
    # initialize when length is in [3,5]
    for i in [3, 4, 5]:
        cache[i] = level(arr[:i])

    # fill cache
    for i in range(6, N+1):
        cand = []

        # case1: sub-array with length 3
        if cache[i-3] is not None:
            cand.append(cache[i-3] + level(arr[i-3:]))

        # case2: sub-array with length 4
        if cache[i-4] is not None:
            cand.append(cache[i-4] + level(arr[i-4:]))

        # case1: sub-array with length 5
        if cache[i-5] is not None:
            cand.append(cache[i-5] + level(arr[i-5:]))

        cache[i] = min(cand)

    return cache[-1]


if __name__ == '__main__':
    # freopen equivalent
    # sys.stdin = open('input.txt', 'r')

    C = int(sys.stdin.readline().strip())
    answers = []

    for _ in range(C):
        line = sys.stdin.readline().strip()
        numbers = [int(x) for x in line]
        answers.append(pi(numbers))

    for a in answers:
        sys.stdout.write('{}\n'.format(a))


