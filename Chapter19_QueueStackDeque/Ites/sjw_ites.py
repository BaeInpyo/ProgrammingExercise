"""
short type이 없어서 50M개의 input을 저장하면 64MB 초과함
"""

import sys
import os
from collections import deque
import time

abs_dir = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(abs_dir, "input.txt"), "r")


class MeasureTime():
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.function(*args, **kwargs)
        end_time = time.time()
        print("Elapsed time for function '%s': %f" %
            (self.function.__name__, end_time - start_time))
        return result


@MeasureTime
def generate_input():
    MAX_N = 50000000
    lst = [None] * MAX_N
    lst[0] = 1983
    for idx in range(1, MAX_N):
        lst[idx] = (lst[idx - 1] * 214013 + 2531011) % (2**32)

    return [(lst[idx - 1] % 10000 + 1) for idx in range(1, MAX_N + 1)]


@MeasureTime
def solution(n, k):
    global SEQUENCE
    answer = 0
    queue = deque()
    queue_sum = 0
    for idx in range(n):
        queue.append(SEQUENCE[idx])
        queue_sum += SEQUENCE[idx]

        while queue_sum > k:
            queue_sum -= queue.popleft()

        if queue_sum == k:
            answer += 1

    return str(answer)


if __name__ == "__main__":
    C = int(sys.stdin.readline().strip())
    answers = []
    SEQUENCE = generate_input()
    for _ in range(C):
        K, N = [int(x) for x in sys.stdin.readline().strip().split()]
        answers.append(solution(N, K))

    sys.stdout.write("\n".join(answers) + "\n")