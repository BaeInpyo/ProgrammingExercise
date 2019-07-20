#!/bin/python3

import sys
import math

resultDict = {}

def solution(n):
    result = 0

    # base case
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 3
    elif n<=0:
        return 0

    if resultDict.get(n, False):
        return resultDict[n]

    if n%2 == 0: # 짝수길이면 ㅁㅁ or ㅁ=ㅁ
        result = (solution(n/2)**2 + solution((n-2)/2)**2)%1000000007
        resultDict[n] = result
    else: # 홀수길이면 ㅁ|ㅁ or ㅁ=|ㅁ or ㅁ|=ㅁ
        result = (solution((n-1)/2)**2 + solution(math.floor((n-2)/2))*solution(math.ceil((n-2)/2))*2)%1000000007
        resultDict[n] = result

    return result


if __name__ == '__main__':
    C = int(sys.stdin.readline())
    for _ in range(C):
        resultDict = {}
        n = int(sys.stdin.readline())
        
        total = solution(n)
        #print(total)
        if n == 1:
            sym = 1
        elif n == 2:
            sym = 2
        else:
            if n%2 == 0:
                sym = solution(n/2) + solution((n-2)/2)
            else:
                sym = solution((n-1)/2)

        print((total-sym+1000000007)%1000000007)
