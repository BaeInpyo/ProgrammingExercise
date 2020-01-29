import sys
import os


# freopen equivalent
abs_dir = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(abs_dir, "input.txt"), "r")


# decorator for measuring time
# used only when debugging
class MeasureTime():
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        t0 = time.time()
        answer = self.function(*args, **kwargs)
        t1 = time.time()
        print("Elapsed:", t1 - t0)
        return answer


# read line and return list of integer
def read_line():
    return [int(x) for x in sys.stdin.readline().strip().split()]


def get_psum_list(doll_list, k):
    """
    return partial sum list
    Since we are only interested in remainder, keep remainder on psum_list.
    Also add dummy [0] to front of psum_list.
    psum[i] = sum(doll_list[:i]) % k (1 <= i <= n).
    For example, in case of testcase, [0, 1, 3, 2, 2, 3, 1].
    """

    # to avoid expension cost of list, use fixed size list
    psum_list = [0] * len(doll_list)
    psum = 0
    for (idx, count) in enumerate(doll_list):
        psum += count
        psum %= k
        psum_list[idx] = psum

    return [0] + psum_list

def get_answer1(psum_list, k):
    """
    To solve problem1, we only need count of r for r in range(k).
    Then, the answer is number of cases to pick 2 of them.
    """

    count = [0] * k
    for psum in psum_list:
        count[psum] += 1

    answer = 0
    for num in count:
        answer += (num * (num - 1)) // 2    # nC2

    return answer % 20091101

def get_answer2(psum_list, n, k):
    """
    To solve problem2, we can use DP (dynamic programming). At each point in
    range(n), we can choose order which covers this point or not choose.
    """

    cache = [0] * (n + 1)
    last = [None] * k # last[i] = last index of i in psum_list
    for end in range(n + 1):
        start = last[psum_list[end]]
        last[psum_list[end]] = end

        if end == 0:
            # first is dummy
            continue

        if start is None:
            # there is no order ends at current index
            cache[end] = cache[end - 1]

        else:
            # pick order ends at current index
            choose = cache[start] + 1

            # ignore order
            not_choose = cache[end - 1]

            # update current with max one
            cache[end] = max(choose, not_choose)

    return cache[n]


def solution(n, k, doll_list):
    psum_list = get_psum_list(doll_list, k)
    answer1 = get_answer1(psum_list, k)
    answer2 = get_answer2(psum_list, n, k)

    return "{} {}".format(answer1, answer2)


if __name__ == "__main__":
    T = read_line()[0]  # number of testcase
    answers = []
    for _ in range(T):
        N, K = read_line()[:2]
        doll_list = read_line()
        answers.append(solution(N, K, doll_list))

    sys.stdout.write("\n".join(answers))