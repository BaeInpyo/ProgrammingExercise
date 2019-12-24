import sys

def pairing(RCs):
    result = []
    minIdx = -1
    minVal = 999
    for idx in range(0, len(RCs), 2):
        val = RCs[idx]/RCs[idx+1]
        if minVal > val:
            if minIdx != -1:
                result.append((RCs[minIdx], RCs[minIdx+1], minVal))
            minVal = val
            minIdx = idx
            continue
        result.append((RCs[idx], RCs[idx+1], val))
    return (RCs[minIdx], RCs[minIdx+1], minVal), result


# 현재의 R, C의 크기가 얼만큼 도미넌트 하냐에 따라 또 달라짐, 즉, 분수의 크기에만 결정되는게 아니라 얼마나 도미넌트 한지에 따라서도 선택이 달라져야함.
def solution(RCs, K, currScore):
    currR, currC, currFraction = currScore
    if K == 0:
        return currFraction
    
    minVal = 999
    minIdx = -1

    for idx in range(len(RCs)):
        newR, newC, _ = RCs[idx]
        newVal = (currR + newR) / (currC + newC)
        if minVal > newVal:
            minIdx = idx
            minVal = newVal
    
    minR, minC, _ = RCs.pop(minIdx)
    return solution(RCs, K-1, (currR+minR, currC+minC, minVal))

if __name__ == '__main__':
    sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline().rstrip())
    for _ in range(C):
        N, K = list(map(int,sys.stdin.readline().rstrip().split()))
        RCs = list(map(int,sys.stdin.readline().rstrip().split()))
        firstChoice, RCs = pairing(RCs) # 첫 선택은 무조건 가장 크기가 작은애로
        print(solution(RCs, K-1, firstChoice))
