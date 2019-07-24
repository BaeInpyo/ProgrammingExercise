#!/bin/python3

import sys
#import random
import math
sys.setrecursionlimit(1500)
envDict = {} # key: (start,s), value: err
pSum = {}
pSqSum = {}

# 부분합 초기화
def initSum(numbers):
    pSum[0], pSqSum[0] = numbers[0], numbers[0]**2
    for i in range(1,len(numbers)):
        pSum[i] = pSum[i-1]+numbers[i]
        pSqSum[i] = pSqSum[i-1]+numbers[i]**2

# 구간의 평균에대한 에러를 반환
def getErrWithMean(fr, to, numbers):
    if fr == 0:
        partialSum = pSum[to]
        partialSqSum = pSqSum[to]
    else:
        partialSum = pSum[to] - pSum[fr-1]
        partialSqSum = pSqSum[to] - pSqSum[fr-1]

    mean = round(partialSum/(to-fr+1))
    currErr = partialSqSum - 2*mean*partialSum + (mean**2)*(to-fr+1)
    return currErr

def solution(start, s, numbers):
    minErr = math.inf

    # 캐싱된 환경이면 바로 리턴
    if envDict.get((start, s), False):
        return envDict[(start,s)]

    # 남은 숫자 수 보다 s가 같거나 크면 에러는 항상 0
    if len(numbers)-start <= s:
        envDict[(start,s)] = 0
        return 0

    # s가 1이면 재귀콜 필요없이 남은 모든 숫자에서 에러구함
    if s == 1:
        currErr = getErrWithMean(start, len(numbers)-1, numbers)
        envDict[(start,s)] = currErr
        return currErr

    # 첫번째 묶음의 크기를 키워가며 에러를 비교함
    for i in range(start, len(numbers)-s+1):
        currErr = getErrWithMean(start, i, numbers)
        minErr = min(minErr, currErr+solution(i+1, s-1, numbers))

    # 최종적으로 해당 환경에대한 최소오차를 기억하고 반환
    envDict[(start,s)] = minErr
    return minErr

if __name__ == '__main__':
    C = int(sys.stdin.readline())
    for _ in range(C):
        envDict, pSum, pSqSum = {}, {}, {}
        n, s = list(map(int, sys.stdin.readline().rstrip().split()))
        numbers = sys.stdin.readline().rstrip()
        if len(numbers) > 1:
            numbers = list(map(int, numbers.split()))
        else:
            numbers = [int(numbers)]
        numbers.sort()
        initSum(numbers)
        print(solution(0, s, numbers))
        #print(' '.join([str(random.randrange(1,1000)) for i in range(100)]))
