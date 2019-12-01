import sys
import math
import itertools

def getDistance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def getClosestBase(bases, base):
    resultIdx = 0
    minDistance = 99999

    for idx, currBase in enumerate(bases):
        currDistance = getDistance(currBase[0],currBase[1],base[0],base[1])
        if currDistance < minDistance:
            minDistance = currDistance
            resultIdx = idx
    return resultIdx, minDistance

def solution(bases, currIdx, distanceLimit, visitDict):
    visitDict[currIdx] = True
    if len(bases) == len(visitDict):
        return True
    currBase = bases[currIdx]
    for idx, base in enumerate(bases):
        if idx == currIdx:
            continue
        if (not visitDict.get(idx, False)) and getDistance(currBase[0],currBase[1],base[0],base[1]) <= distanceLimit:
            if solution(bases, idx, distanceLimit, visitDict):
                return True
    return False
    
if __name__ == '__main__':
    #sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline().rstrip())
    for _ in range(C):
        N = int(sys.stdin.readline().rstrip())
        bases = [tuple(map(float, sys.stdin.readline().rstrip().split())) for _ in range(N)]
        combinations = itertools.combinations(range(N),2)
        distances = sorted([getDistance(bases[i][0],bases[i][1], bases[j][0],bases[j][1]) for i, j in combinations])

        while len(distances)>0: # 2진탐색 적용
            medianIdx = (len(distances)-1)//2 
            currDistance = distances[medianIdx]
            visitDict = {}
            result = solution(bases, 0, currDistance, visitDict) # 현재 제한거리로 모든 노드를 연결시킬수 있는지 확인
            if result:
                minDistance = currDistance
                distances = distances[0:medianIdx]
            else:
                distances = distances[medianIdx+1:]

        print(format(round(minDistance,2), ".2f"))


