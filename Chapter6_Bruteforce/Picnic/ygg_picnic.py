#!/bin/python3

import os
import sys

def solution(S, students, pair_dict, depth):
    """
    S : 전체 학생수
    students : 선택받은 학생 리스트 True or False
    pair_dict : 짝 정보를 담은 사전, 중복되는 짝은 없음 (예: (1,2)페어가 있으면 (2,1)은 없음)
                또한 두 숫자중 더 작은 수를 키로 하여 저장하고 있음 (예: (3,1)이 입력에 있었으면 1을 키로 하여 저장)
    depth : 재귀콜의 깊이 = 이번 콜에 짝 선택권이 있는 학생의 인덱스
    """

    result = 0

    # 콜이 마지막 학생이 선택하는 차례까지오면 - 재귀의 바닥
    if depth == S-1:
        # 재귀의 바닥에서 모든 학생이 선택받았을 경우 정답에 +1
        if sum(students) == S:
            return 1

    # 이번에 선택할 차례인 학생이 스스로가 이미 선택받았을 경우 다음 순번에게 바로 차례를 넘김
    if students[depth]:
        return solution(S, students, pair_dict, depth+1)

    # 이번 차례의 학생이 가진 선택권을 가져옴
    choices = pair_dict.get(depth, [])
    for choice in choices:
        # 각 선택케이스 별로 체크하고 다음 순번을 재귀 콜 함
        # 이때 선택하려는 학생이 이미 앞에서 선택받았으면 패스
        if students[choice]:
            continue
        students[depth], students[choice] = True, True
        result += solution(S, students, pair_dict, depth+1)
        # python object argument : call by ref? 잘 몰라서 일단 되돌리기,,,
        students[depth], students[choice] = False, False

    return result

if __name__ == '__main__':
    C = int(input())
    for _ in range(C):
        S, P = list(map(int, input().rstrip().split()))
        pairs = list(map(int, input().rstrip().split()))
        pair_dict = {}
        for i in range(P):
            buddy = [pairs[i*2], pairs[i*2+1]]
            buddy.sort()
            pair_dict[buddy[0]] = pair_dict.get(buddy[0],[]) + [buddy[1]]

        #print([False]*S, pair_dict)
        # in case 2 : [False, False, False, False] {0: [1, 3, 2], 1: [2, 3], 2: [3]}
        print(solution(S, [False]*S, pair_dict, 0))
