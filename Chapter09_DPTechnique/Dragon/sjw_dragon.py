import sys


"""
Nth generation dragon curve's length is 3*2^n - 1, we cannot find this directly.
I found that every dragon curve has repeat some patterns every 6 character.
Dragon curve consists of (FX, YF, +, -).
FX and YF appears alternatively.
Sign (+, -) has following pattern.
Nth sign is equal to toggle of (2k-N)th sign where k is a integer that is maximum power of 2 smaller than N.
That is, k = 2^([logN]).
"""


SIGN = ['+', '-']


def sign(n):
    # return nth sign
    def log2(num):
        # return [log2(num)]
        assert num >= 1

        result = 0
        while True:
            if num == 1:
                break
            result += 1
            num = num // 2

        return result

    assert n >= 1

    # if n is power of 2, then sign is +
    k = pow(2, log2(n))
    if n == k:
        return 0

    return 1 - sign(2*k - n)


def solution(n, p, l):
    result = []
    for idx in range(p-1, p-1+l):
        curr = None
        if idx % 6 in [0, 4]:
            curr = 'F'
        elif idx % 6 == 1:
            curr = 'X'
        elif idx % 6 in [2, 5]:
            curr = SIGN[sign((idx//3) + 1)]
        elif idx % 6 == 3:
            curr = 'Y'

        result.append(curr)

    return ''.join(result)


if __name__ == "__main__":
    # freopen equivalent
    sys.stdin = open("input.txt", "r")

    c = int(sys.stdin.readline().strip())
    answers = []

    for _ in range(c):
        n, p, l = [int(x) for x in sys.stdin.readline().strip().split()]
        answers.append(solution(n, p, l))

    for a in answers:
        print(a)
