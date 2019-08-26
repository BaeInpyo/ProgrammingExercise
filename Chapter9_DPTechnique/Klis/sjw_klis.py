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


def find_next(curr, k):
    # find next node in curr using k
    # return index of curr

    # case: only 1 node to go
    if len(curr) == 1:
        return 0

    # check prev index constraint

    if k <= curr[0][1]:
        return 0

    for i in range(len(curr) - 1):
        start = curr[i][1]
        end = start + curr[i+1][1]
        if start <= k <= end:
            return i+1


def solution(N, K, arr):
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

    # initialize tree
    # each node is (index, count)
    max_length = max(cache)
    max_indexes = [x[0] for x in enumerate(cache) if x[1] == max_length]
    tree = [(x, 1) for x in max_indexes]  # (index, count)
    tree.sort(key=lambda x: arr[x[0]])  # sort by arr[index]
    tree = [tree]

    # fill tree
    for _ in reversed(range(1, max_length)):
        dic = {}
        for node in tree[0]:
            index, count = node
            parent = cache_recon[index]
            for p in parent:
                if p in dic:
                    dic[p] += count
                else:
                    dic[p] = count

        curr = list(dic.items())    # (index, count)
        curr.sort(key=lambda x: arr[x[0]])   # sort by arr[index]
        tree.insert(0, curr)    # insert at first

    assert len(tree) == max_length

    # travel tree
    result = []

    # root
    curr = tree[0]
    if len(curr) == 1 or K <= curr[0][1]:
        result.append(curr[0])
    else:
        for i in range(len(curr)-1):
            start = curr[i][1]
            end = start + curr[i+1][1]
            if start <= K <= end:
                result.append(curr[i+1])
                K -= curr[i+1][1]

    # internal nodes
    for depth in range(1, max_length-1):
        prev = result[-1]   # (index, count)
        curr = [x for x in tree[depth] if prev[0] in cache_recon[x[0]]]     # apply cache_recon for connectivity
        next_index = find_next(curr, K)

        if next_index != 0:
            K -= curr[next_index][1]

        result.append(curr[next_index]) # append number in arr

    # leaf node
    prev = result[-1]
    curr = [x for x in tree[max_length-1] if prev[0] in cache_recon[x[0]]]  # apply cache_recon for connectivity
    result.append(curr[K-1])

    result = [arr[x[0]] for x in result]

    return result


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
        print(len(a))
        print(' '.join([str(x) for x in a]))

