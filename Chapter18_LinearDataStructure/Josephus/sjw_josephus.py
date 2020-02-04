import sys
import os
from collections import deque

# freopen equivalent
abs_dir = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(abs_dir, "input.txt"), "r")


def read_line():
    """
    return line and return list of integer
    """

    return [int(x) for x in sys.stdin.readline().strip().split()]


def solution_queue(n, k):
    """
    Use queue to solve problem. Timed out.
    """

    # first soldier always dies
    queue = deque(range(2, n + 1))
    while(len(queue) > 2):

        # skip (k - 1) soldiers
        for _ in range(k - 1):
            curr = queue.popleft()
            queue.append(curr)

        queue.popleft() # kill kth soldier

    queue = list(queue)
    queue.sort()
    return "{} {}".format(queue[0], queue[1])


def solution_iteration(n, k):
    """
    Use list only. Time Complexity is O(nk). Timed out too.
    """

    soldiers = [False] + [True] * (n - 1)
    num_soldiers = n - 1

    idx = 0
    while num_soldiers > 2:
        skip = 0
        # skip (k-1) soldiers
        while skip < k - 1:
            if soldiers[idx]:
                skip += 1

            idx = (idx + 1) % n

        # kill kth soldier
        while not soldiers[idx]:
            idx = (idx + 1) % n

        # print("delete idx:", idx)
        soldiers[idx] = False
        num_soldiers -= 1

    answer = [str(idx + 1) for (idx, alive) in enumerate(soldiers) if alive]
    return " ".join(answer)


def solution(n, k):
    """
    Use list to keep alive soldiers.
    Time complexity is (N^2) but since this problem has very short time limit
    actual execution time is more important than complexity.
    """

    soldiers = [num for num in range(1, n + 1)]
    index = 0
    while len(soldiers) > 2:
        soldiers.pop(index)
        index = (index + k - 1) % len(soldiers)

    return " ".join([str(num) for num in soldiers])


if __name__ == "__main__":
    C = read_line()[0]
    answers = []
    for _ in range(C):
        N, K = read_line()
        answers.append(solution(N, K))

    sys.stdout.write("\n".join(answers) + "\n")