#!/bin/python3

import sys
import random
import math
from functools import reduce
sys.setrecursionlimit(1500)
envDict = {} # key: (start,s), value: err

# 숫자 리스트 => 평균값, 평균값에 대한 에러
def getErrWithMean(numbers):
    mean = round(sum(numbers)/len(numbers))
    currErr = reduce(lambda x,y: x+(mean-y)**2, numbers, 0)
    return mean, currErr


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
        currNumbers = numbers[start:]
        _, currErr = getErrWithMean(currNumbers)
        envDict[(start,s)] = currErr
        return currErr

    # 첫번째 묶음의 크기를 키워가며 에러를 비교함
    for i in range(start, len(numbers)-s+1):
        currNumbers = numbers[start:i+1]
        mean, currErr = getErrWithMean(currNumbers)
        minErr = min(minErr, currErr+solution(i+1, s-1, numbers))

    # 최종적으로 해당 환경에대한 최소오차를 기억하고 반환
    envDict[(start,s)] = minErr
    return minErr

if __name__ == '__main__':
    C = int(sys.stdin.readline())
    for _ in range(C):
        envDict = {}
        n, s = list(map(int, sys.stdin.readline().rstrip().split()))
        numbers = sys.stdin.readline().rstrip()
        if len(numbers) > 1:
            numbers = list(map(int, numbers.split()))
        else:
            numbers = [int(numbers)]
        numbers.sort()
        print(solution(0, s, numbers))
        #print(' '.join([str(random.randrange(1,1000)) for i in range(100)]))
