import sys
import os
from itertools import combinations

'''
Strategy
- If word1 is substring of word2, then we can only consider word2
- If we already selected N words, then solution only depends on (last word in selected N words, set of remained words)
- (N-1) words in front do not affect solution
'''

'''
merged(word1, word2) = diff(word1, word2) + word2
E.g, word1 = 'abcde' and word2 = 'cdefg', then diff(word1, word2) = 'ab'
'''
def diff(word1, word2):
    # since each word does not fully overlap each other, the maximum overlaped length equals to (length of shorter word)-1
    for length in reversed(range(1, min(len(word1), len(word2)))):
        if word2.startswith(word1[-length:]):
            return word1[:-length]
    # does not overlap at all
    return word1

# remove if word1 is substring of word2
def remove_substrings(words):
    words = set(words)
    result = set(words)
    for word1 in words:
        for word2 in words:
            # skip two words are same
            if word1 == word2:
                continue
            if word1.find(word2) != -1:
                result.discard(word2)

    return result

def get_min_string(diff_cache, answer_cache, last, remained):
    if remained == ():
        return last

    key = (last, remained)
    if key in answer_cache:
        return answer_cache[key]

    candidates = []
    _remained = set(remained)
    for first in remained:
        _remained.remove(first)
        diff = diff_cache[(last, first)]
        curr = diff_cache[(last, first)] + get_min_string(diff_cache, answer_cache, first, tuple(_remained))
        candidates.append(curr)
        _remained.add(first)

    candidates.sort(key=len)
    answer_cache[key] = candidates[0]
    return answer_cache[key]

def solution_recur(words):
    diff_cache = dict()     # cache for diff of 2 words
    answer_cache = dict()   # cache for saving answer
    words = remove_substrings(words)    # remove substrings
    digit = len(words)

    # fill diff_cache
    for word1 in words:
        for word2 in words:
            if word1 == word2:
                continue

            key = (word1, word2)
            diff_cache[key] = diff(word1, word2)

    candidates = []
    for word in words:
        words.remove(word)
        candidates.append(get_min_string(diff_cache, answer_cache, word, tuple(words)))
        words.add(word)

    candidates.sort(key=len)
    return candidates[0]

def solution_iter(words):
    diff_cache = dict()
    answer_cache = dict()
    words = remove_substrings(words)
    digit = len(words)

    # fill diff_cache
    for word1 in words:
        for word2 in words:
            if word1 == word2:
                continue

            key = (word1, word2)
            diff_cache[key] = diff(word1, word2)

    # init answer_cache
    for word in words:
        key = (word, ())            # (last, remained)
        answer_cache[key] = word    # merged string

    # fill answer_cache
    for length in range(1, digit):
        for remained in combinations(words, length):
            for last in words:
                if last in remained:
                    continue

                # last must be not in remained
                candidates = []
                for first in remained:
                    _remained = tuple(word for word in remained if word != first)
                    key = (first, _remained)
                    cached = answer_cache[key]
                    merged = diff_cache[(last, first)] + cached
                    candidates.append(merged)

                candidates.sort(key=lambda x: len(x), reverse=False)    # sort by length ASC
                key = (last, remained)
                answer_cache[key] = candidates[0]

    candidates = []
    for last in words:
        remained = tuple(word for word in words if word != last)
        key = (last, remained)
        value = answer_cache[key]
        candidates.append(value)

    candidates.sort(key=lambda x: len(x), reverse=False)    # sort by length ASC
    return candidates[0]


if __name__ == "__main__":
    # freopen equivalent
    sys.stdin = open(os.path.join(os.path.dirname(__file__), "input.txt"), "r")

    C = int(sys.stdin.readline().strip())
    answers = []
    for _ in range(C):
        k = int(sys.stdin.readline().strip())
        words = []
        for _ in range(k):
            words.append(sys.stdin.readline().strip())

        words = list(set(words))    # remove duplicate
        answers.append(solution_iter(words))

    for a in answers:
        print(a)
