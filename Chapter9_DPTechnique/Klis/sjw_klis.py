import sys


"""
전략

주어진 list A에 대해서 LIS는 다음의 성질을 만족한다.
1) cache[i] = Ai로 끝나는 LIS의 길이라고 하자.
2) cache[i] = Ak < Ai, k < i를 만족하는 k중 Ak가 가장큰 k들에 대해 cache[k] + 1

2)의 조건을 만족하는 k가 여러개인 경우 LIS를 여러개 만들 수 있다.
cache_recon을 이용하여 cache_recon[i] = cache[i]를 만들게한 k값들의 list 로 저장을 하면
cache와 cache_recon을 만든 후 cache_recon[n]부터 시작하여 모든 LIS를 구할 수 있다.

이 LIS를 사전순으로 정렬하면 KLIS를 구할 수 있다.
정렬을 하지 않아도, 각 분기마다 몇개씩 갈래가 있는지 알 수 있으므로 KLIS를 단번에 구할 수 있다.
"""


def solution(N, K, arr):
    pass


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

