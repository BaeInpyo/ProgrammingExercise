import sys
import math


def getNumOfDivisor(num, limit):
    maxDivisor = int(math.sqrt(num))
    result = 0
    for i in range(1,maxDivisor+1):
        if result > limit:
            return -1
        if num % i == 0:
            result += 2
    
    if maxDivisor**2 == num:
        result += 1
    
    return result


def solution(n, lo, hi):
    result = 0
    for num in range(lo, hi+1):
        if n == getNumOfDivisor(num, n):
            result += 1
    return result
    
if __name__ == '__main__':
    sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline().rstrip())
    for _ in range(C):
        n, lo, hi = [int(x) for x in sys.stdin.readline().rstrip().split()]
        print(solution(n, lo, hi))

    

