import sys


def min_square(numbers):
    avg = round(sum(numbers) / len(numbers)) # 평균에서 가장 가까운 양수
    result = sum(map(lambda x: pow(x-avg, 2), numbers))
    # print('numbers, avg, result:', numbers, avg, result)
    return result


def permutation(sections, sum_square, N, S, dic):
    '''

    :param sections: 지금까지 고른 section의 조합
    :param sum_square: 지금까지 고른 section에 대한 각 영역의 제곱합
    :return: (최소제곱조합 section, 최소 제곱합)
    '''

    remain_s = S - len(sections)
    remain_n = N - sum(sections)

    assert remain_s >= 0, 'remain_s'
    assert remain_n >= 0, 'remain_n'

    if remain_s == 0 and remain_n == 0:
        return sections[:], sum_square

    if remain_s == 1:
        # print('sections:', sections, sum(sections)+1, N)
        return permutation(sections[:] + [remain_n], sum_square + dic[(sum(sections)+1, N)],
                           N, S, dic)

    cand = []
    # 최대 (remain_n - remain_s + 1)까지 가능
    for i in range(1, remain_n-remain_s+2):
        # print('curr:', sections, sum(sections)+1, sum(sections)+i+1)
        curr = permutation(sections[:] + [i], sum_square + dic[(sum(sections)+1, sum(sections)+i)],
                           N, S, dic)
        cand.append(curr)

    cand.sort(key=lambda x: x[1])
    print('cand:', cand)

    return cand[0]


def quantization(arr, S):
    N = len(arr)
    arr.sort()

    # dic[(i, j)] : [i, j] i번째 숫자와 j번째 숫자까지의 영역에서의 최소제곱합
    # i와 j는 list index가 아님에 주의
    # j도 포함하는 범위임에 주의
    dic = {}

    for i in range(N):
        for j in range(i, N):
            dic[(i+1, j+1)] = min_square(arr[i:j+1])

    print('arr:', arr)
    # print('dic')
    # keys = sorted(dic.keys())
    # for k in keys:
    #     print('k, v:', k, dic[k])

    sections, sum_square = permutation([], 0, N, S, dic)
    print('sections:', sections)
    print('sum_square:', sum_square)
    return sum_square


if __name__ == '__main__':
    # freopen equivalent
    sys.stdin = open('input.txt', 'r')

    C = int(sys.stdin.readline().strip())
    answers = []

    for _ in range(C):
        N, S = map(int, sys.stdin.readline().strip().split())
        arr = list(map(int, sys.stdin.readline().strip().split()))
        answers.append(quantization(arr, S))

    for a in answers:
        print('answer:', a)
