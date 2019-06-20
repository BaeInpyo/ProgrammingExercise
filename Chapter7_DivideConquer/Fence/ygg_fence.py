#!/bin/python3

import sys
import operator

"""
핵심 : 가장 작은 울타리를 기준으로 양옆 덩어리를 각각 독립된 문제로 생각해도 된다.
"""
def getMin(fenceList):
    # enumerate(list) = [(idx, value)...]
    index, value = min(enumerate(fenceList), key=operator.itemgetter(1))
    return index, value

def solution(fenceList, maxSize):
    if fenceList == []:
        return maxSize

    minFenceIdx, minFenceSize = getMin(fenceList)
    # 매 단계 펜스 덩어리의 가장 작은 울타리를 덩어리의 길이만큼 늘린것을 맥스값과 비교
    maxSize = max(maxSize, minFenceSize*len(fenceList))

    # 가장작은 울타리를 기준으로 양 옆 펜스덩어리에 대해 재귀적으로 문제를 품
    leftFence = fenceList[:minFenceIdx]
    rightFence = fenceList[minFenceIdx+1:]
    return max(solution(leftFence, maxSize), solution(rightFence, maxSize))

if __name__ == '__main__':
    C = int(sys.stdin.readline())
    for _ in range(C):
        N = int(sys.stdin.readline())
        fenceList = list(map(int, sys.stdin.readline().rstrip().split()))
        print(solution(fenceList, 0))
