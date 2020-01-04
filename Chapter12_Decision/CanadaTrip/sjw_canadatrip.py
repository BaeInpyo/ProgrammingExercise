import sys, os
import math
import bisect

# freopen equivalent
abs_path = os.path.abspath(os.path.dirname(__file__))
sys.stdin = open(os.path.join(abs_path, 'input.txt'), 'r')

'''
Since K is smaller than number of possible signs, the answer is in range
[0, max(L)]. If location is given, we can calculate number of signs appear
before location and on location in O(n) time.

If we search the range [0, max(L)] using binary search, it's time complexity
will O(log(max(L)) * n) = O(n)
'''

# return range of number of sings in location
def count_signs(information, location):
    before, on = 0, 0
    for item in information:
        L, M, G = item['L'], item['M'], item['G']
        # count signs before location
        if L - M <= location < L:
            before += (location - (L - M) + G - 1) // G
        elif location == L:
            before += M // G
        elif location > L:
            before += (M // G) + 1

        # count signs on location
        if L - M <= location <= L and (location - (L - M)) % G == 0:
            on += 1

    return before, on

def solution(information, K):
    start = 0
    end = max([item['L'] for item in information]) + 1

    while end > start:
        mid = (start + end) // 2
        before, on = count_signs(information, mid)

        if before >= K:
            # search [start, mid]
            end = mid
        elif before + on < K:
            # search [mid, end]
            start = mid
        else:
            return mid

    return mid



if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())
    answers = []
    for _ in range(T):
        N, K = [int(x) for x in sys.stdin.readline().strip().split()]
        information = []
        for _ in range(N):
            L, M, G = [int(x) for x in sys.stdin.readline().strip().split()]
            information.append({
                'L': L,
                'M': M,
                'G': G,
            })

        answers.append(solution(information, K))

    sys.stdout.write('\n'.join([str(x) for x in answers]))
