import sys
import string
from itertools import combinations, chain


'''
Strategy

- Remove duplicates from original word list of length k if exist and use k' words
- Now, we need to calculate k'! permutations of word to find shortest string
- Since 1 <= k' <= 15, max are 15! which is intractable
- If we want to calculate a!, we can reuse results of (a-1)!
'''


# merge given 2 words and return list of shortest merged string
# if w1w2 and w2w1 are same length, return both
def merge_word(word1, word2):
    min_len = min(len(word1), len(word2))
    w12 = word1 + word2
    w21 = word2 + word1
    for i in reversed(range(min_len)):
        if word1.endswith(word2[:i+1]):
            w12 = word1 + word2[i+1:]
            break

    for i in reversed(range(min_len)):
        if word2.endswith(word1[:i+1]):
            w21 = word2 + word1[i+1:]
            break

    if len(w12) == len(w21):
        return [w12, w21]
    else:
        return [min(w12, w21, key=len)]


def solution(words):
    digit = len(words)
    cache = dict()

    # init cache
    for comb in combinations(range(digit), 1):
        curr_word = words[comb[0]]

        cache[comb] = {curr_word}

    # fill cache
    for i in range(2, digit+1):
        for comb in combinations(range(digit), i):
            results = set()
            for j in range(i):
                curr_word = words[comb[j]]
                curr_comb = comb[:j] + comb[j+1:]
                prev = cache[curr_comb] # cached result
                next = [merge_word(curr_word, p) for p in prev]
                next = set(chain(*next))
                next = { x for x in next if len(x) == len(min(next, key=len)) } # extract shortest
                results.update(next)

            results = { x for x in results if len(x) == len(min(next, key=len)) } # extract shortest
            cache[comb] = results

    key = tuple(range(digit))
    result = cache[key].pop()
    return result


if __name__ == "__main__":
    # freopen equivalent
    sys.stdin = open("input.txt", "r")

    C = int(sys.stdin.readline().strip())
    answers = []
    for _ in range(C):
        k = int(sys.stdin.readline().strip())
        words = []
        for _ in range(k):
            words.append(sys.stdin.readline().strip())

        words = list(set(words))    # remove duplicate
        answers.append(solution(words))

    for a in answers:
        print(a)
