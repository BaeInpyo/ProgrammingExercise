import sys
import os


def solution(sushi, budget):
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
        n, m = [int(x) for x in sys.stdin.readline().strip().split()]
        sushi = []
        for _ in range(n):
            price, value = [int(x) for x in sys.stdin.readline().strip().split()]
            sushi.append((int(price/100), value))

        sushi = list(set(sushi))    # keep unique (price, value)
        sushi = [{'price': x[0], 'value': x[1]} for x in sushi]    # convert to list of dict

        answer = solution(sushi, int(m/100))
        answers.append(answer)

    for a in answers:
        print(a)
