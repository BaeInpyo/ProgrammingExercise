import sys


"""
At first glance, we can calculate LIS by finding all sub-sequences and conditioning IS(Increasing Sub-sequence) and
calculate maximum length. But there can be 2^n sub-sequences, it's intractable.

LIS has next characteristic.
A: given number list
cache[i] = length of LIS that ends up with Ai
cache[i] = max(cache[k]) + 1 where k < i and Ak < Ai

We can use cache_recon to re-construct LIS and cache_recon has following characteristic.
cache_recon[i] = list of ks that made cache[i] 

Since we want to find Kth LIS itself, we should use cache_recon.
Instead of finding all LISs and sort it, calculate number of LISs start with given number.
"""


def start_with_num(num, length, cache_recon, num_to_idx, idx_to_num):
    if length == 1:
        return 1

    result = 0
    start_index = num_to_idx[num]
    for i in range(start_index+1, len(cache_recon)):
        curr = cache_recon[i]
        if start_index in curr:
            result += start_with_num(idx_to_num[i], length-1, cache_recon, num_to_idx, idx_to_num)

    return result


def find_all_LIS(num, length, cache_recon, num_to_idx, idx_to_num):
    if length == 1:
        return [[num]]

    candidates = []
    start_index = num_to_idx[num]
    for i in range(start_index+1, len(cache_recon)):
        curr = cache_recon[i]
        if start_index in curr:
            candidates.extend(find_all_LIS(idx_to_num[i], length-1, cache_recon, num_to_idx, idx_to_num))

    return [[num] + x for x in candidates]


def solution(N, K, arr):
    num_to_idx = { x[1]: x[0] for x in enumerate(arr) }
    idx_to_num = arr

    # initialize cache
    cache = [1] * N
    cache_recon = [[i] for i in range(N)]

    # fill cache
    for i in range(1, N):
        candidates = []
        for j in range(i):
            if arr[j] < arr[i]:
                candidates.append((j, cache[j]))

        if not candidates:
            continue

        candidates.sort(key=lambda x:x[0])
        max_length = max([x[1] for x in candidates]) + 1
        max_indexes = [x[0] for x in candidates if x[1] == max_length-1]

        cache[i] = max_length
        cache_recon[i] = max_indexes

    LIS_length = max(cache)
    k = 0
    # find kth LIS
    for num in sorted(arr):
        swn = start_with_num(num, LIS_length, cache_recon, num_to_idx, idx_to_num)
        if k < K <= k + swn:
            all_LISs = find_all_LIS(num, LIS_length, cache_recon, num_to_idx, idx_to_num)
            all_LISs.sort()
            return all_LISs[K-k-1]

        else:
            k += swn


if __name__ == "__main__":
    # freopen equivalent
    sys.stdin = open("input.txt", "r")

    C = int(sys.stdin.readline().strip())
    answers = []

    for _ in range(C):
        N, K = [int(x) for x in sys.stdin.readline().strip().split()]
        arr = [int(x) for x in sys.stdin.readline().strip().split()]
        answers.append(solution(N, K, arr))

    for a in answers:
        print(len(a), a)

