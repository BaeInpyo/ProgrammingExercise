import sys
import bisect
from collections import OrderedDict
envDict = {}
pickDict = {}
trackingLIS = {}
KLIS = []

def solution(prevNum, currIdx, numList):
    lis = 1
    if envDict.get(currIdx, -1) != -1:
        lis = envDict[currIdx]
        temp = pickDict[prevNum].get(lis, [])
        bisect.insort(temp, numList[currIdx])
        pickDict[prevNum][lis] = temp
        return lis
    for idx in range(currIdx, len(numList)):
        num = numList[idx]
        if numList[currIdx] < num:
            result = solution(numList[currIdx], idx, numList)+1
            if lis <= result:
                lis = result
                envDict[currIdx] = lis
    temp = pickDict[prevNum].get(lis, [])
    bisect.insort(temp, numList[currIdx])
    pickDict[prevNum][lis] = temp
    return lis

# 오늘의 교훈 : recunstruct 과정에서도 캐싱이 필요하다
def getAllLIS(currPrevNum, numList, LIS):
    if envDict.get(currPrevNum, -1) != -1:
        return envDict[currPrevNum]

    if LIS == 0:
        return 1
    currLISDict = pickDict[currPrevNum].get(LIS, -1)
    if currLISDict == -1:
        return 1
    total = 0


    for num in currLISDict:
        trackingLIS[currPrevNum][num] = getAllLIS(num, numList, LIS-1)
        total += trackingLIS[currPrevNum][num]

    envDict[currPrevNum] = total
    return total
    
def getKLIS(K, numList, prevNum):
    currDepthDict = trackingLIS[prevNum]
    for num, numOfLis in currDepthDict.items():
        nextK = K-numOfLis
        if nextK <= 0:
            KLIS.append(str(num))
            return getKLIS(K, numList, num)
        else:
            K=nextK

def initPickDict(x):
    pickDict[int(x)] = {}
    trackingLIS[int(x)] = OrderedDict()
    return int(x)

if __name__ == '__main__':
    #sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline())
    for _ in range(C):
        envDict = {}
        pickDict = {-1:OrderedDict(), 0:OrderedDict()}
        trackingLIS = {-1:OrderedDict(), 0:OrderedDict()}
        KLIS = []
        N, K = list(map(int, sys.stdin.readline().rstrip().split()))
        numList = [0]+list(map(initPickDict, sys.stdin.readline().rstrip().split()))
        LIS = solution(-1, 0, numList)
        print(LIS-1)
        envDict={}
        getAllLIS(-1, numList, LIS)
        #print(trackingLIS)
        getKLIS(K, numList, -1)
        del KLIS[0]
        print(' '.join(KLIS))
        

        #print(sorted(getAllLIS(0))[K-1])

        # pickDict : {(7, 3): 8, (6, 3): 8, (6, 2): 7, (5, 3): 8, (5, 2): 7, (5, 1): 6, (3, 7): 4, (2, 7): 4, (2, 6): 3, (1, 7): 4, (1, 6): 3, (1, 5): 2, (0, 7): 4, (0, 6): 3, (0, 5): 2, (0, 4): 1, (0, 0): 5}
        # (prevNum, currIdx): currNum
        # prevNum이 같고 인덱스가 자기보다 더 큰데 숫자는 더 작다? => 경우의수에 추가
        # ex) (0,0): 5, (0,4):1, (0,5):2, (0,6): 3
        # => prevNum이 0일때 인덱스가 0인 숫자 5를 집는것은 항상 옳다.
        # => 근데 prevNum이 0일때 인덱스가 4(>0)인 숫자 1(<5)가 존재한다. => 따라서 prevNum이 0일때 숫자 1을 집는것도 항상 옳다.
        # => 이 이후 나타나는 prevNum이 0이고 인덱스가 더 큰 숫자들중에 1보다 작은것은 없으므로 prevNum이 0일때는 5를 집거나 1을 집는 두가지 경우가 있다.
