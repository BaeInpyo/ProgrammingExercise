from collections import OrderedDict
import sys
envDict = {}
pickDict = {}

def solution(prevNum, currIdx, numList):
    result = 0

    if currIdx >= len(numList):
        return 0

    if envDict.get((prevNum, currIdx), -1) != -1:
        return envDict[(prevNum, currIdx)]

    currNum = numList[currIdx]

    if prevNum < currNum:
        pickCase = solution(currNum, currIdx+1, numList) + 1
        skipCase = solution(prevNum, currIdx+1, numList)

        if pickCase >= skipCase:
            pickDict[prevNum][currIdx] = currNum

        envDict[(prevNum, currIdx)] = max(pickCase, skipCase)
        return max(pickCase, skipCase)
            
    else:
        skipCase = solution(prevNum, currIdx+1, numList)
        envDict[(prevNum, currIdx)] = skipCase
        return skipCase

    return result

def getAllLIS(currPrevNum):
    result = []

    if pickDict[currPrevNum] == {}:
        return ['']

    prevPickedNum = 999999
    # pickDict을 일단 idx순으로 정렬
    candList = sorted(list(pickDict[currPrevNum].items()), key=lambda x:x[0])
    for _, candNum in candList:
        # 인덱스가 이전에 픽됐던 숫자보다 크고 and 이전에 픽됐던 숫자보다 크기가 작다면 경우의수에 추가
        if candNum < prevPickedNum:
            prevPickedNum = candNum
            result += (map(lambda x: str(candNum)+' '+x.rstrip(), getAllLIS(candNum)))
    return result

def initPickDict(x):
    pickDict[int(x)] = {}
    return int(x)

if __name__ == '__main__':
    #sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline())
    for _ in range(C):
        envDict = {}
        pickDict = {0:{}}
        N, K = list(map(int, sys.stdin.readline().rstrip().split()))
        numList = list(map(initPickDict, sys.stdin.readline().rstrip().split()))

        print(solution(0, 0, numList))
        print(sorted(getAllLIS(0))[K-1])

        # pickDict : {(7, 3): 8, (6, 3): 8, (6, 2): 7, (5, 3): 8, (5, 2): 7, (5, 1): 6, (3, 7): 4, (2, 7): 4, (2, 6): 3, (1, 7): 4, (1, 6): 3, (1, 5): 2, (0, 7): 4, (0, 6): 3, (0, 5): 2, (0, 4): 1, (0, 0): 5}
        # (prevNum, currIdx): currNum
        # prevNum이 같고 인덱스가 자기보다 더 큰데 숫자는 더 작다? => 경우의수에 추가
        # ex) (0,0): 5, (0,4):1, (0,5):2, (0,6): 3
        # => prevNum이 0일때 인덱스가 0인 숫자 5를 집는것은 항상 옳다.
        # => 근데 prevNum이 0일때 인덱스가 4(>0)인 숫자 1(<5)가 존재한다. => 따라서 prevNum이 0일때 숫자 1을 집는것도 항상 옳다.
        # => 이 이후 나타나는 prevNum이 0이고 인덱스가 더 큰 숫자들중에 1보다 작은것은 없으므로 prevNum이 0일때는 5를 집거나 1을 집는 두가지 경우가 있다.
