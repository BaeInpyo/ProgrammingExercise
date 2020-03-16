import sys
import os
import heapq

# freopen equivalent
abs_dir = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(abs_dir, "input.txt"), "r")


def get_generator(a, b):
    curr =  1983
    while True:
        yield curr
        curr = (curr * a + b) % 20090711


def solution(n, a, b):
    gen = get_generator(a, b)

    if n == 1:
        return next(gen)

    result = 0
    first = next(gen)
    second = next(gen)
    result = first + min(first, second)
    left_max_heap = [-min(first, second)]
    right_min_heap = [max(first, second)]

    for _ in range(n-2):
        left_max = -heapq.heappop(left_max_heap)
        right_min = heapq.heappop(right_min_heap)
        num = next(gen)
        nums = sorted([left_max, right_min, num])

        # keep len(left) >= len(right)
        if len(left_max_heap) == len(right_min_heap):
            # if len(left) == len(right), add 2 items to left and 1 items to right
            heapq.heappush(left_max_heap, -nums[0])
            heapq.heappush(left_max_heap, -nums[1])
            heapq.heappush(right_min_heap, nums[2])
        else:
            # if len(left) = len(right) + 1, add 1 items to left and 2 items to right
            heapq.heappush(left_max_heap, -nums[0])
            heapq.heappush(right_min_heap, nums[1])
            heapq.heappush(right_min_heap, nums[2])

        # median is always top of left_max_heap
        result += (-left_max_heap[0])

    result %= 20090711
    print(result)
    return


if __name__ == "__main__":
    for _ in range(int(input())):
        N, a, b = [int(x) for x in input().split()]
        solution(N, a, b)