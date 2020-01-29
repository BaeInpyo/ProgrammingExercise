import sys
import os
import bisect
from collections import defaultdict

import json
import time

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

# pretty print dict
def print_dict(dic):
    print(json.dumps(dic, indent=4, sort_keys=True))

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

def get_remainder_dict(psum_list):
    """
    Key of remainder_dict is remainder, i.e, integer in range [0, k).
    Value of remainder_dict is list of index which psum_list[index] = remainder.
    For example, in case of testcase, {
        0: [0],
        1: [1, 6],
        2: [3, 4],
        3: [2, 5]
    }
    """

    remainder_dict = defaultdict(list)
    for (idx, remainder) in enumerate(psum_list):
        remainder_dict[remainder].append(idx)

    return remainder_dict

def get_range_dict(remainder_dict, k):
    """
    Key of range_dict is start_index, i.e integer in range [0, n)
    Value of range_dict is dict which has following keys: "next_index",
    "end_index". "next_index" is start index of next range. "end_index" is
    enclosing index of current range. For example, in case of testcase, {
        1: { "next_index": 2, "end_index": 6},
        2: { "next_index": 3, "end_index": 5},
        3: { "next_index": None, "end_index": 4},
    }
    """

    range_list = list()
    for remainder in range(k):
        index_list = remainder_dict[remainder]
        if len(index_list) >= 2:
            # adjacent pair makes shortest range
            # each pair is (start_index, end_index)
            pair = [(index_list[idx], index_list[idx + 1])
                for idx in range(len(index_list) - 1)]
            range_list.extend(pair)

    range_list.sort()   # sort by start_index

    range_dict = dict()
    for (idx, pair) in enumerate(range_list):
        start_index, end_index = pair
        if idx == len(range_list) - 1:
            # end of pair
            next_index = None
        else:
            # start_index of next pair
            next_index = range_list[idx + 1][0]
        range_dict[start_index] = {
            "next_index": next_index,
            "end_index": end_index
        }

    return range_dict

def get_answer1(remainder_dict, k):
    """
    return answer of problem1
    We must find range [H, T] such that sum of doll_list[H:T+1] is multiple of
    K. This sum can be also calculated with psum[T] - psum[H-1].
    To solve problem1, we will pick pair of (H, T) such that remainder of
    psum[T] and psum[H-1] is equal. (We already know that (a -b ) % c = a % c - 
    b % c)
    """

    answer = 0
    for remainder in range(k):
        count = len(remainder_dict[remainder])
        if count < 2:
            pass
        else:
            answer += count * (count - 1) // 2

    return answer % 20091101

def get_answer2(range_dict, n):
    """
    return answer of problem2
    To select as many non-overlapping range as possible, we need to consider
    all cases. In other words, we need to select all possible range from strat
    to end (0 ~ N). DP (dynamic programming) can help this. This is similar
    with Knapsack problem.
    Though this is DP problem, since N is too large (100000), we cannot use
    recursion to solve this problem. Iteration can help this.
    """

    # range_dict is empty dict
    if not range_dict:
        return 0

    cache = [0] * (n + 1)   # 1 dummy element
    keys = sorted(range_dict.keys())

    # fill cache
    for idx in reversed(range(n)):
        # idx is larger than any range pair
        if idx > keys[-1]:
            cache[idx] = 0
            continue

        start_index = keys[bisect.bisect_left(keys, idx)]
        if idx < start_index:
            # current index is not in range_dict
            # fill current cache with value in right side
            cache[idx] = cache[start_index]
        elif idx == start_index:
            # current index in in range_dict
            # compare choosing and not choosing
            end_index = range_dict[start_index]["end_index"]
            choose = cache[end_index] + 1
            not_choose = cache[start_index + 1]
            cache[start_index] = max(choose, not_choose)

    # print(cache)
    return cache[0]

def solution(n, k, doll_list):
    psum_list = get_psum_list(doll_list, k)
    remainder_dict = get_remainder_dict(psum_list)
    range_dict = get_range_dict(remainder_dict, k)
    # print(psum_list)
    # print_dict(remainder_dict)
    # print_dict(range_dict)
    answer1 = get_answer1(remainder_dict, k)
    answer2 = get_answer2(range_dict, n)

    return "{} {}".format(answer1, answer2)

if __name__ == "__main__":
    T = read_line()[0]  # number of testcase
    answers = []
    for _ in range(T):
        N, K = read_line()[:2]
        doll_list = read_line()
        answers.append(solution(N, K, doll_list))

    sys.stdout.write("\n".join(answers))