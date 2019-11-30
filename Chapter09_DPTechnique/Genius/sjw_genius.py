import os
import sys

'''
NOTE
cache.shape = (5, N)
cache[i][j] = probability that music[j] starts at (time % 5)
'''

def solution(N, K, M, L, T, Q):
    cache = [[0] * N for _ in range(5)]

    # init cache
    cache[0][0] = 1

    # fill cache
    for time in range(L[0], K + 1):
        probability = [0] * N   # current probability
        for curr_music in range(N):
            for prev_music in range(N):
                _time = (time - L[prev_music]) % 5    # prev_music start at <_time>
                probability[curr_music] += cache[_time][prev_music] * T[prev_music][curr_music]

        cache[time % 5] = probability

    # if music is start between [current - L[music] + 1, current]
    # that music is running at current:30
    result = [0] * M
    for i in range(len(Q)):
        q = Q[i]
        start = K - L[q] + 1
        end = K
        for time in range(start, end + 1):
            result[i] += cache[time % 5][q]

    for i in range(len(result)):
        result[i] = round(result[i], 8)
    return result

if __name__ == '__main__':
    # freopen equivalent
    abs_path = os.path.dirname(os.path.abspath(__file__))
    sys.stdin = open(os.path.join(abs_path, 'input.txt'), 'r')

    C = int(sys.stdin.readline().strip())
    answers = []

    # read input
    for _ in range(C):
        N, K, M = [int(x) for x in sys.stdin.readline().strip().split()]
        L = [int(x) for x in sys.stdin.readline().strip().split()]
        T = []
        for _ in range(N):
            row = [float(x) for x in sys.stdin.readline().strip().split()]
            T.append(row)

        Q = [int(x) for x in sys.stdin.readline().strip().split()]
        answers.append(solution(N, K, M, L, T, Q))

    for a in answers:
        print(a)
