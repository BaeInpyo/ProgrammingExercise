import sys
import os
import math

PI = math.pi
IMPOSSIBLE = 101

'''
Strategy
Since area to cover is circular shape, every point can be represented using central angle.
And for the case of 0 degree, it's the very next to 360 degree. For convenience, we can extend the range of central angle from (0~2PI) to (0~4PI).
After extension, we don't have to think about if guard point convers 0 or not
We can find answer by finding combinations of guard points that cover range longer than 2PI.

In summary,
1. convert coverage of each guard point to range of central angle (0 ~ 4PI)
2. for all guard point as start point, select next guard point that has the longest coverage
'''


# convert (x, y, r) to (start, end)
# 0 <= start, end <= 4PI
def xyr_to_degree(x, y, r):
    center = math.atan2(y, x)
    if center < 0:
        center += 2 * math.pi   # if (x, y) is in third or fourth quadrant, center < 0, so convert it

    val = (128 - r * r) / 128   # according to law of cosine, https://ko.wikipedia.org/wiki/%EC%BD%94%EC%82%AC%EC%9D%B8_%EB%B2%95%EC%B9%99#%EC%A0%95%EC%9D%98
    _range = math.acos(val)
    start, end = center - _range, center + _range

    # shift 2PI
    if start < 0:
        center += 2 * PI
        start += 2 * PI
        end += 2 * PI
    return center, start, end


# select next gp given first_gp with greedy policy
def greedy(first_gp, gps):
    result = 1
    _, start, end = first_gp

    while end - start < 2 * PI:
        delta_left, delta_right = 0, 0
        for gp in gps:
            _, curr_start, curr_end = gp
            if start <= curr_start <= end or start <= curr_end <= end:
                delta_left = max(delta_left, start - curr_start)
                delta_right = max(delta_right, curr_end - end)
            else:
                continue

        # extend to left
        if delta_left > delta_right and delta_left > 0:
            start -= delta_left
            result += 1

        # extend to right
        elif delta_right > delta_left and delta_right > 0:
            end += delta_right
            result +=1

        # nothing to select
        else:
            return IMPOSSIBLE

    return result


def solution(n, gps):
    gps = [xyr_to_degree(*gp) for gp in gps]
    result = IMPOSSIBLE
    for first_gp in gps:
        _result = greedy(first_gp, gps)
        result = min(result, _result)   # find the smallest answer

    return 'IMPOSSIBLE' if result == IMPOSSIBLE else result

if __name__ == '__main__':
    # freopen equivalent
    abs_path = os.path.dirname(os.path.abspath(__file__))
    sys.stdin = open(os.path.join(abs_path, 'input.txt'), 'r')

    c = int(sys.stdin.readline())
    answers = []
    for _ in range(c):
        n = int(sys.stdin.readline())
        gps = []    # list of (y, x, r)
        for __ in range(n):
            y, x, r = [float(x) for x in sys.stdin.readline().strip().split()]
            gps.append((x, y, r))

        answers.append(solution(n, gps))

    for a in answers:
        print(a)