import sys

'''
Strategy
If remain numbers and turn are given, regardless of past state, the score of Hyunwoo and Seoha will get is same.
So cache key is (remain numbers, turn) and it's value is (HyunWoo's scroe, Seoha's score).
'''

def get_score(cache, numbers, turn, left, right, hw, sh):
    # left and right is leftmost and rightmost index of remained
    # turn: 0 for hw, 1 for sh
    result = [0, 0]

    # basecase
    if left > right:
        return hw, sh

    # basecase
    if left == right:
        result[turn] += numbers[left]
        return hw + result[0], sh + result[1]

    # check cache
    key = (left, right, turn)
    if key in cache:
        _hw, _sh = cache[key]
        return hw + _hw, sh + _sh

    # consid er 4 case
    # case1: select left
    case1 = get_score(cache, numbers, 1 - turn, left+1, right, hw, sh)
    case1 = [case1[0], case1[1]]
    case1[turn] += numbers[left]

    # case2: select right
    case2 = get_score(cache, numbers, 1 - turn, left, right-1, hw, sh)
    case2 = [case2[0], case2[1]]
    case2[turn] += numbers[right]

    # case3: remove left
    case3 = get_score(cache, numbers, 1 - turn, left+2, right, hw, sh)

    # case4: remove right
    case4 = get_score(cache, numbers, 1 - turn, left, right-2, hw, sh)

    cases = [case1, case2, case3, case4]
    cases.sort(key=lambda x: x[turn] - x[1-turn])   # sort by diff ASC

    # set cache
    cache[key] = tuple(cases[-1])

    return tuple(cases[-1])


def solution(numbers):
    cache = dict()
    hw, sh = get_score(cache, numbers, turn=0, left=0, right=len(numbers)-1, hw=0, sh=0)
    return hw - sh


if __name__ == '__main__':
    # freopen equivalent
    sys.stdin = open('input.txt', 'r')

    C = int(sys.stdin.readline().strip())
    answers = []

    for _ in range(C):
        n = int(sys.stdin.readline().strip())
        numbers = [int(x) for x in sys.stdin.readline().strip().split()]
        answers.append(solution(numbers))

    for a in answers:
        print(a)
