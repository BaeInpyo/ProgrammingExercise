import sys


def solution(n):
    """
    Total number of tiling cases follows the formula 'f(n) = f(n-1) + f(n-2), n >= 3'.
    If we can calculate possible symmetric tiling cases, then we can also get possible asymmetric tiling
    by subtract it from total number of tiling.

    Let's think of symmetric tiling cases
    - if n is odd, n = 2k+1
        -  middle tile must be vertical, so f(k) will be number of symmetric tiling if we fill rest with same tiling
    - if n is even, n = 2k
        - f(k) can be one case of symmetric tiling, same as above odd case
        - f(k-1) also can be case of symmetric tiling if we fill 2 vertical tiles from kth to (k+1)th columns

    :param n: width
    :return: number of possible asymmetric tiling
    """

    if n <= 2:
        return 0

    cache = [0] * (n+1)
    cache[1], cache[2] = 1, 2

    for i in range(3, n+1):
        cache[i] = (cache[i-2] + cache[i-1]) % 1000000007

    k = n // 2  # this cares both odd and even case of n
    ans = (cache[n] - cache[k] - cache[k-1]) % 1000000007
    return ans


if __name__ == '__main__':
    # freopen equivalent
    sys.stdin = open('input.txt', 'r')

    C = int(sys.stdin.readline().strip())
    answers = []

    for _ in range(C):
        n = int(sys.stdin.readline().strip())
        answers.append(solution(n))

    for a in answers:
        sys.stdout.write('{}\n'.format(a))
