import os
import sys

# freopen equivalent
abs_dir = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(abs_dir, "input.txt"), "r")


class RMQ:
    def __init__(self, arr):
        def init(arr, left, right, curr):
            """
            self.req[curr] represents arr[left:right+1]
            return minimum value in range [left, right]
            """

            # leaf node
            if left == right:
                self.rmq[curr] = arr[left]
                return self.rmq[curr]

            mid = (left + right) // 2
            min_left = init(arr, left, mid, curr*2)
            min_right = init(arr, mid+1, right, curr*2 + 1)
            self.rmq[curr] = min(min_left, min_right)
            return self.rmq[curr]

        self.n = len(arr)
        self.rmq = [None] * (self.n * 4)
        self.MAX = 30000
        init(arr, 0, self.n - 1, 1)


    def query(self, left, right):
        def _query(left, right, curr, curr_left, curr_right):
            """
            return minimum of intersection between [left, right] and
            [curr_left, curr_right]
            """

            # 2 ranges are disjoint
            if curr_right < left or right < curr_left:
                return self.MAX

            # [left, right] covers [curr_left, curr_right]
            if left <= curr_left and curr_right <= right:
                return self.rmq[curr]

            # consider both range
            mid = (curr_left + curr_right) // 2
            min_left = _query(left, right, curr*2, curr_left, mid)
            min_right = _query(left, right, curr*2+1, mid+1, curr_right)
            return min(min_left, min_right)

        return _query(left, right, 1, 0, self.n - 1)


if __name__ == "__main__":
    for _ in range(int(input())):
        N, Q = [int(x) for x in sys.stdin.readline().strip().split()]
        heights = [int(x) for x in sys.stdin.readline().strip().split()]

        # init RMQ (Ranged Minimum Queue)
        min_rmq = RMQ(heights)
        max_rmq = RMQ([-x for x in heights])
        answers = [None] * Q
        for idx in range(Q):
            a, b = [int(x) for x in sys.stdin.readline().strip().split()]
            _max = -max_rmq.query(a, b)
            _min = min_rmq.query(a, b)
            answers[idx] = str(_max - _min)

        sys.stdout.write("\n".join(answers) + "\n")


