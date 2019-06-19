#!/bin/python3

import sys

def flip(quadTree, idx):
    flipedTree = [quadTree[idx]+quadTree[idx+3]+quadTree[idx+4]+quadTree[idx+1]+quadTree[idx+2]]
    #예) result : ['w','b','x',...] + ['xwwbb'] + ['w','xbwwb','b',...]
    # 리스트 슬라이스 : 메모리문제? 64mb 안에서 충분함 (최대문자열길이 = 1000)
    return quadTree[:idx]+flipedTree+quadTree[idx+5:] 

# 입력의 가장 오른쪽에 있는 x#### 부터 뒤집어감, 뒤집힌 x#### 파트는 한 덩어리로 인식
def solution(quadTree):
    for idx in range(len(quadTree)-1,-1,-1):
        if quadTree[idx] == 'x':
            quadTree = flip(quadTree, idx)
    return ''.join(quadTree)

if __name__ == '__main__':
    C = int(sys.stdin.readline())
    for _ in range(C):
        #예) quadTree = ['x','w','w','b','b']
        quadTree = list(sys.stdin.readline().rstrip())
        print(solution(quadTree))
