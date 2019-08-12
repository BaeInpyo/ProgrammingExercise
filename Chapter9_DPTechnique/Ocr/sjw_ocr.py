import sys


"""
전략

주어진 문장을 n개의 word로 이루어진 list A라고 하자.
cache_val[i][j] = 길이가 i이고 Wj로 끝나는 문장 중 조건부 확률의 최대값이라고 하자.
그러면 다음의 수식이 성립한다.
1) cache_val[i][j] = max(cache_val[i-1][k] * (Wk 다음에 Wj가 나타날 확률) * (Ai를 Wj로 분류할 확률), 0 <= k < m)

1 <= i <= n, 0 <= j < m의 순서로 cache_val을 채울 수 있고
cache_val[n][:] 중 max인 값이 최대 조건부 확률이다.

주어진 문장에 대해 조건부 확률의 최대값이 아니라 조건부 확률이 최대인 문장을 직접 구해야 하므로 back tracking을 위해 cache_recon도 이용한다.

cache_recon[i][j] = 1) 수식의 cache_val[i][j]의 값을 설정하게한 단어의 index이다.
cache_val[0][j]의 값을 설정하게한 단어는 j이다.


"""


def solution(sentence, word_to_idx, idx_to_word, B, T, M, m, n):
    cache_val = [[0] * m for _ in range(n+1)]
    cache_recon = [[0] * m for _ in range(n+1)]

    # initialize cache
    first_word_index = word_to_idx[sentence[0]]
    for j in range(m):
        cache_val[1][j] = B[j] * M[first_word_index][j]
        cache_recon[1][j] = j

    # fill table
    for i in range(2, n+1):
        for j in range(m):
            cand = []
            curr_word_index = word_to_idx[sentence[i-1]]
            for k in range(m):
                cand.append(cache_val[i-1][k] * T[k][j] * M[j][curr_word_index])

            max_value = max(cand)
            max_index = cand.index(max_value)
            cache_val[i][j] = max_value
            cache_recon[i][j] = max_index

    # make sentence
    max_value = max(cache_val[n])
    index = cache_val[n].index(max_value)
    result = [idx_to_word[index]]
    i = n
    while i > 1:
        index = cache_recon[i][index]
        result.insert(0, idx_to_word[index])
        i -= 1

    return ' '.join(result)



if __name__ == "__main__":
    # freopen equivalent
    sys.stdin = open("input.txt", "r")

    answers = []

    m, q = [int(x) for x in sys.stdin.readline().strip().split()]
    idx_to_word = sys.stdin.readline().strip().split()
    word_to_idx = { x[1]: x[0] for x in enumerate(idx_to_word) }
    B = [float(x) for x in sys.stdin.readline().strip().split()]

    T = [0] * m
    for i in range(m):
        T[i] = [float(x) for x in sys.stdin.readline().strip().split()]

    M = [0] * m
    for i in range(m):
        M[i] = [float(x) for x in sys.stdin.readline().strip().split()]

    for _ in range(q):
        line = sys.stdin.readline().strip().split()
        n, sentence = int(line[0]), line[1:]
        answers.append(solution(sentence, word_to_idx, idx_to_word, B, T, M, m, n))

    for a in answers:
        print(a)



