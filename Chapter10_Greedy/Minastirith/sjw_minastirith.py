import sys
import os
import math

RADIUS = 8
IMPOSSIBLE = 101    # since n <= 100

'''
- circle can be represented with degree from 0 to 2 * PI
- each gp can be represented using (center, range) or [center - range, center + range]
    - if center - range < 0 or center + range > 2 * PI, we must handle it properly
- first, pick any gp that covers 0. (Let's say there are k gps that cover 0)
- remove range of gp picked in First, then we have completely linear range from e1 to e2
- from now select gp that starts between 0 and e1 and extends most to right
    - we can remove circular by this way
'''

# convert (x, y, r) to (center, range)
def xyr_to_degree(x, y, r):
    center = math.atan2(y, x)
    if center < 0:
        center += 2 * math.pi   # if (x, y) is in third or fourth quadrant, -0.5 * PI < atan2(y, x) < 0

    val = (128 - r * r) / 128   # according to law of cosine, https://ko.wikipedia.org/wiki/%EC%BD%94%EC%82%AC%EC%9D%B8_%EB%B2%95%EC%B9%99#%EC%A0%95%EC%9D%98
    _range = math.acos(val)
    return center, _range

# return list of gps that cover zero
def find_cover_zero(gps):
    result = []
    for (center, _range) in gps:
        if center - _range < 0 or center + _range > 2 * math.pi:
            result.append((center, _range))
    return result

# given first gp, select best (extends to right most) gp iteratively
def greedy(first, gps):
    result = 1
    center, _range = first
    gps = [x for x in gps if x != first]    # exclude first gp
    start = center + _range
    start = start if start < 2 * math.pi else start - 2 * math.pi   # adjust to be in [0, 2 * PI]
    end = center - _range
    end = end + 2 * math.pi if end < 0 else end                     # adjust to be in [0, 2 * PI]

    assert(end > start)
    assert(0 <= start <= 2 * math.pi)
    assert(0 <= end <= 2 * math.pi)
    # now we need to fill range [start, end]
    right_max = 0
    while gps:
        selected_gp = None
        # find gp that extends to right most
        for curr_g in gps:
            center, _range = curr_g
            curr_start = max(center - _range, 0)
            curr_end = center + _range
            if curr_start <= start and curr_end > right_max:
                right_max = curr_end
                selected_gp = curr_g
        if selected_gp is not None:
            result += 1
            start = right_max   # set start using picked gp
            gps = [x for x in gps if x != selected_gp]  # pop selected gp
        if selected_gp is None or right_max >= 2 * math.pi:
            break

    if right_max >= end:
        return result
    else:
        return IMPOSSIBLE   # impossible, since n <= 100

def solution(n, gps):
    gps = [xyr_to_degree(*e) for e in gps]  # convert from (x, y, r) to (center, range)
    first_gps = find_cover_zero(gps)        # gps that cover zero are candidate of first pick
    result = IMPOSSIBLE
    for f in first_gps:
        _result = greedy(f, gps)
        if _result < IMPOSSIBLE:
            result = _result

    if result == IMPOSSIBLE:
        return 'IMPOSSIBLE'
    else:
        return result


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
            gps.append((y, x, r))

        answers.append(solution(n, gps))

    for a in answers:
        print(a)