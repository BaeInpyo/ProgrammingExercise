import sys
import os


def solution(sushi, budget):
    sushi.sort(key=lambda x: x['value'] / x['price'], reverse=True)   # value / price
    result = 0  # sum of value
    remain = budget - sum([x['price'] for x in sushi])

    # pick best value/price sushi as mush as possible
    if remain > 0:
        r, q= divmod(remain, sushi[0]['price'])
        result += r * sushi[0]['value']  # add value
        remain = budget - sushi[0]['price'] * r
    else:
        remain = budget

    # below are similar with knapsack problem
    cache = dict()  # key: remain, value: sum of value
    cache[0] = 0    # init cache

    # fill cache
    for i in range(1, remain+1):
        candidates = []
        for s in sushi:
            if s['price'] <= i:
                candidates.append(cache[i - s['price']] + s['value'])

        if not candidates:
            cache[i] = 0
        else:
            cache[i] = max(candidates)

    return result + cache[remain]


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
