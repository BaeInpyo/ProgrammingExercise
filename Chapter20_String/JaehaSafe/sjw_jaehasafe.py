import sys
import os
from collections import defaultdict

abs_dir = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(abs_dir, "input.txt"), "r")


def solution(n, states):
    cache = {}  # key(state1, state2), value: number of left rotates

    m = len(states[0])
    result = 0  # number of counts start from left rotate
    for idx in range(n):
        src_state = states[idx]
        dst_state = states[idx + 1]

        # left rotate
        for count in range(1, m):
            intermid_state = src_state[count:] + src_state[:count]
            key1 = (src_state, intermid_state)
            key2 = (intermid_state, src_state)
            cache[key1] = min(cache.get(key1, m), count)
            cache[key2] = min(cache.get(key2, m), m - count)
            if intermid_state == dst_state:
                if idx % 2 == 0:
                    # print("left ", src_state, "=>", dst_state, ": ", cache[key1])
                    result += cache[key1]
                else:
                    # print("right ", src_state, "=>", dst_state, ": ", m - cache[key1])
                    result += m - cache[key1]

    return str(n * m - result)

if __name__ == "__main__":
    C = int(sys.stdin.readline().strip())
    answers = [None] * C
    for idx in range(C):
        N = int(sys.stdin.readline().strip())
        states = [None] * (N + 1)
        for jdx in range(N + 1):
            states[jdx] = sys.stdin.readline().strip()

        answers[idx] = solution(N, states)

    sys.stdout.write("\n".join(answers) + "\n")