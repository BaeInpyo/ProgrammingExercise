import sys
from itertools import combinations
from pprint import pprint


def solution(e, m):
    # key: 사용 가능한 숫자 모음(numbercount), value: dict (key: 0~m-1, value: cache의 key를 이용하여 만들 모든 순열 중 나머지가 k인 갯수)
    cache = {}

    # init cache
    for comb in combinations(e, 1):
        dic = { x: 0 for x in range(m) }    # key: 나머지, value: comb로 만들 수 있는 수열 중 나머지가 key인 것의 개수
        remain = comb[0] % m
        dic[remain] += 1
        numbercount = tuple([comb.count(x) for x in range(10)])
        cache[numbercount] = dic

    # fill cache
    for i in range(2, len(e)):
        all_combs = combinations(e, i)
        for comb in all_combs:
            dic = {x: 0 for x in range(m)}
            for num in set(comb):
                pool = list(comb)
                pool.remove(num)
                numbercount = tuple([pool.count(x) for x in range(10)])
                remain = num * pow(10, len(pool)) % m
                for key in cache[numbercount]:
                    curr = (remain + key) % m
                    dic[curr] += cache[numbercount][key]

            numbercount = tuple([comb.count(x) for x in range(10)])
            cache[numbercount] = dic

    prefixes = find_prefixes(e)
    result = 0
    for pre in prefixes:
        numbers = e[:]
        for num in pre:
            numbers.remove(num)

        numbercount = tuple([numbers.count(x) for x in range(10)])
        dic = cache[numbercount]

        # calculate remain of prefix
        curr = int(''.join([str(x) for x in pre]))
        curr = pow(10, len(e) - len(pre)) * curr
        remain = curr % m
        result += dic[(m-remain) % m]

    return result

# e.g number = [4, 3, 2, 1]
# prefix 뒤에는 남은 숫자들을 어떻게 배열해도 전부다 원래의 숫자보다 작게됨
def find_prefixes(number):
    pool = number[:]
    result = []

    for idx in range(len(number)):
        if idx != 0:
            pool.pop(0)

        for n in range(10):
            if n < number[idx] and \
                n in pool and \
                    (idx == 0 and n != 0 or idx != 0):
                result.append(number[:idx] + [n])

    return result


if __name__ == '__main__':
    # freopen equivalent
    sys.stdin = open('input.txt', 'r')

    c = int(sys.stdin.readline().strip())
    answers = []
    for _ in range(c):
        e, m = sys.stdin.readline().strip().split() # string
        e = [int(x) for x in e]
        m = int(m)
        answers.append(solution(e, m))

    for a in answers:
        print(a)


