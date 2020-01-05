import sys
import math

def solution(N, M, Z):
    if Z >= 99: # 99일때도 답이 없음에 유의
        return -1
    fr, to = 0, 2000000000
    while True:
        mid = (fr + to)//2
        newN, newM = N+mid, M+mid
        newZ = math.floor(100*newM/newN) # newZ를 구하는 수식의 순서에도 유의하라고 함. 55.9999999 와같이 될 수 있다고 함
        if newZ > Z:
            if to-fr == 1:
                return fr
            to = mid
        else:
            if to-fr == 1:
                return to
            fr = mid
    return fr
    
if __name__ == '__main__':
    sys.stdin = open('input.in', 'r')
    T = int(sys.stdin.readline().rstrip())
    for _ in range(T):
        N, M = list(map(int, sys.stdin.readline().rstrip().split()))
        print(solution(N, M, math.floor(100*M/N)))


