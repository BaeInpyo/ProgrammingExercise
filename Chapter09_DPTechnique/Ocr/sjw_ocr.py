import sys


"""
Let's consider given sentence 'A' as list of n words, i.e. A1, ... An where Ak denotes kth word in sentence.
We want to find the new sentence 'B' that maximizes conditional probability of B given A ( P(B|A) ).
There can be m^n cases that B can occur. So we cannot calculate all these cases.

After taking a time, I found that
P(B|A) = P(B1...Bn | A1...An) = P(B1...Bn-1 | A1...An-1) * P(Bn was mis-classified as An) * P(Bn-1 leads to Bn).
  
We can derive below relation.
W: our vocabulary of size m
S: given sentence with length n
B: list of length m that denotes B[i] = P(Wi appears at first position of sentence)
T: matrix of size (m x m) that denotes T[i][j] = P(Wi leads to Wj)
M: matrix of size (m x m) that denotes M[i][j] = P(classify Wi as Wj)
cache[i][j]: maximum conditional probability, i.e P(B|S) where B is end with Wj and length of B is i \
    0 <= i < n, 0 <= j < m
cache[i][j] = max(cache[i-1][k] * T[k][j] * M[j][Si's index])
cache[0][j] = B[j] * M[0][S0's index]
cache_recon[i][j] = index of k that made cache[i][j]
cache_recon[0][j] = j

Then, maximum conditional probability is max(cache[n-1]) and we can construct that sentence by following cache_recon.  
"""


def find_max(arr):
    max_index = 0
    max_value = arr[0]

    for index, value in enumerate(arr):
        if value > max_value:
            max_value = value
            max_index = index

    return max_index, max_value


def solution(sentence, word_to_idx, idx_to_word, B, T, M, m, n):
    cache = [[0] * m for _ in range(n)]
    cache_recon = [[0] * m for _ in range(n)]

    # initialize cache
    word_index = word_to_idx[sentence[0]]
    for j in range(m):
        cache[0][j] = B[j] * M[j][word_index]
        cache_recon[0][j] = j

    # fill cache and cache_recon
    for i in range(1, n):
        for j in range(m):
            candidates = [0] * m
            for k in range(m):
                candidates[k] = cache[i-1][k] * T[k][j]

            max_index, max_value = find_max(candidates)
            si_index = word_to_idx[sentence[i]]
            max_value *= M[j][si_index]
            cache[i][j] = max_value
            cache_recon[i][j] = max_index

    # re-construct sentence
    max_index, _ = find_max(cache[n-1])
    result = [idx_to_word[max_index]]
    i, j = n-1, max_index
    while True:
        if i == 0:
            break

        j = cache_recon[i][j]
        i -= 1
        result.insert(0, idx_to_word[j])

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
