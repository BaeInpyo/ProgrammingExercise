import sys
import math
envDict = {}
signs = []

def solution(gen, startIdx, endIdx, sign):
    totalStringLen = 3*(2**gen)-1
    halfStringIdx = int(totalStringLen/2)
    if gen == 0:
        return

    if startIdx < halfStringIdx and endIdx < halfStringIdx:
        solution(gen-1, startIdx, endIdx, '+')
        #signs.append(sign)

    elif startIdx > halfStringIdx and endIdx > halfStringIdx:
        solution(gen-1, startIdx-halfStringIdx-1, endIdx-halfStringIdx-1, '-')
        #signs.append(sign)
    
    elif startIdx == halfStringIdx:
        signs.append(sign)
        solution(gen-1, 0, endIdx-halfStringIdx, '-')
        
    elif endIdx == halfStringIdx:
        solution(gen-1, startIdx, halfStringIdx-1, '+')
        signs.append(sign)
        
    else:
        #dfs 순으로 부호들을 집어넣음
        solution(gen-1, startIdx, halfStringIdx-1, '+')
        signs.append(sign)
        solution(gen-1, 0, endIdx-halfStringIdx-1, '-')
        
    return


if __name__ == '__main__':
    #sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline())
    for _ in range(C):
        signs = []
        N, P, L = list(map(int, sys.stdin.readline().rstrip().split()))
        solution(N, P-1, P+L-2, '+')
        if P%6 == 1:
            result = 'FX'
            xTurn = False
        elif P%6 == 4:
            result = 'YF'
            xTurn = True
        elif P%6 == 2:
            result = 'X'
            xTurn = False
        elif P%6 == 5:
            result = 'F'
            xTurn = True
        elif P%6 == 3:
            result = ''
            xTurn = False
        elif P%6 == 0:
            result = ''
            xTurn = True

        for sign in signs:
            if xTurn:
                result += sign + 'FX'
                xTurn = False
            else:
                result += sign + 'YF'
                xTurn = True
        print(result[:L])

        
