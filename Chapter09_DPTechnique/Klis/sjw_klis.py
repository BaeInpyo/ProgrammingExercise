import sys


"""
We can calculate LIS by finding all sub-sequences and conditioning IS(Increasing Sub-sequence) and
calculate maximum length. But there can be 2^n sub-sequences, it's intractable.

LIS has next characteristic.
A: given number list
cache[i] = length of LIS that ends up with Ai
cache[i] = max(cache[k]) + 1 where k < i and Ak < Ai

We can use cache_recon to re-construct LIS and cache_recon has following characteristic.
cache_recon[i] = list of ks that made cache[i] 

Since we want to find Kth LIS itself, we should use cache_recon.
Find all LISs and sorting it will very inefficient because LIS as at most 2^(n/2), e.g. [2, 1, 4, 3, 6, 5].

We can back track from last element of LIS to first element of LIS using cache_recon.
This can be represented as tree. Each node in tree has 2 value. First is index in A and second is the number of LISs
that pass node.

In summary, we can calculate Kth using following method.
1. Make cache and cache_recon.
2. Back track cache_recon and make tree. Be careful at connectivity between parent and child (Not fully connected).
3. Traverse tree to find Kth LIS.
"""


def find_next(curr, k):
    # find next node in curr using k
    # return index of curr
    if k <= curr[0][1]:
        return 0, 0

    end = curr[0][1]
    for i in range(len(curr) - 1):
        start = end
        end = start + curr[i+1][1]
        if start <= k <= end:
            return i+1, start


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
    # each node in tree is (index, count)
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

    # traverse tree
    result = []

    for depth in range(max_length):
        # root
        if depth == 0:
            curr = tree[depth]
        # below root
        elif depth < max_length:
            prev = result[-1]
            curr = [x for x in tree[depth] if prev in cache_recon[x[0]]]    # consider connectivity

        next_index, accumulated = find_next(curr, K)
        result.append(curr[next_index][0])
        K -= accumulated

    result = [arr[x] for x in result]    # index to number
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

