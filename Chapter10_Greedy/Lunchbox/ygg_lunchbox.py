import sys

def solution(M,E):
    M_E = list(zip(M,E))
    M_E.sort(key=lambda x: x[1], reverse=True)
    maximum = 0
    currMSum = 0
    for m, e in M_E:
        currMSum += m
        maximum = max(currMSum + e, maximum)
    return maximum
        
if __name__ == '__main__':
    #sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline().rstrip())
    for _ in range(C):
        N = int(sys.stdin.readline().rstrip())
        M = list(map(int, sys.stdin.readline().rstrip().split()))
        E = list(map(int, sys.stdin.readline().rstrip().split()))
        print(solution(M,E))


