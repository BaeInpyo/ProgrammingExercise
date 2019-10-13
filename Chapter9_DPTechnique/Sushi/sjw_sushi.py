import sys
import os
from fractions import gcd
from functools import reduce
from itertools import combinations

'''
- lcm([1, 20]) = 232,792,560 (somewhat big number)
- sum(lcm(n1, n2) for n1, n2 in [1, 200]) = 147,630,370 (still big number)
'''

def solution_reduce_budget(sushi, budget):
    # reduce total budget to small enough
    # this can lead to fewer iteration
    def lcm(a, b):
        return int(a * b / gcd(a, b))

    sushi.sort(key=lambda e: e['value'] / e['price'], reverse=True)   # sort by value per price
    sushi_cleaned = []  # remove unnecessary sushi

    # if s2['price'] is multiple of s1['price'] and s1 has better (value / price)
    # then s2 is unnecessary because s2 can be replaced by s1
    for i in range(len(sushi)):
        curr_price = sushi[i]['price']
        if all([curr_price % e['price'] for e in sushi_cleaned]):
            sushi_cleaned.append(sushi[i])

    lcm_pairs = [lcm(x[0], x[1]) for x in combinations([e['price'] for e in sushi_cleaned], 2)]
    sum_lcm_pairs = sum(lcm_pairs)

    value = 0   # sum of values
    if budget > sum_lcm_pairs:
        count = (budget - sum_lcm_pairs) // sushi_cleaned[0]['price']   # pick best (value / price) AMAP
        budget -= count * sushi_cleaned[0]['price']
        value += count * sushi_cleaned[0]['value']

    # fill cache on reduced budget
    cache = [0] * (budget + 1)
    for i in range(1, budget + 1):
        candidates = []
        for s in sushi_cleaned:
            if i >= s['price']:
                curr = s['value'] + cache[i - s['price']]
                candidates.append(curr)

        # find max
        if candidates:
            cache[i] = max(candidates)

    return value + cache[-1]


def solution_minimal_window(sushi, budget):
    # below are similar with knapsack problem
    # sliding cache
    cache = [0] * 201

    # init cache
    for i in range(1, 201):
        candidates = []
        for s in sushi:
            if s['price'] <= i:
                candidates.append(cache[i - s['price']] + s['value'])

        if candidates:
            cache[i] = max(candidates)

    # fill cache
    for i in range(201, budget+1):
        value = 0
        for s in sushi:
            curr = cache[(i - s['price']) % 201] + s['value']
            if curr > value:
                value = curr

        cache[i % 201] = value

    return cache[budget % 201]


if __name__ == '__main__':
    # freopen equivalent
    abs_path = os.path.dirname(os.path.abspath(__file__))
    sys.stdin = open(os.path.join(abs_path, 'input.txt'), 'r')

    c = int(sys.stdin.readline().strip())
    answers = []
    for _ in range(c):
        n, m = [int(x) for x in sys.stdin.readline().strip().split()]   # read n, m
        sushi = []
        for _ in range(n):
            price, value = [int(x) for x in sys.stdin.readline().strip().split()]   # read price and value
            sushi.append((int(price/100), value))

        sushi = list(set(sushi))    # keep unique (price, value)
        sushi = [{'price': x[0], 'value': x[1]} for x in sushi]    # convert to list of dict

        answer = solution_reduce_budget(sushi, int(m/100))
        answers.append(answer)

    for a in answers:
        print(a)
