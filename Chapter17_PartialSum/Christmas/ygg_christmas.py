import sys
from collections import OrderedDict
from itertools import islice
zeroToISum = {}
patialSum = {}
candidates = OrderedDict() # key: fr, value: to들
envDict = {}

def getPatialSum(fr, to):
    return zeroToISum[to]-zeroToISum[fr-1]

def solution_1(N, K, boxes):
    result = 0
    for fr in range(N):
        for to in range(fr, N):
            pSum = getPatialSum(fr,to)
            patialSum[(fr,to)] = pSum
            if pSum % K == 0:
                result += 1
                if candidates.get(fr, -1) == -1:
                    candidates[fr] = [to]
                else:
                    candidates[fr].append(to)

    return result
            
def solution_2(coveredTo, candiIdx):
    # candidates 는 fr순 -> to순 으로 정렬되어있음.
    result = 0
    key = (coveredTo, candiIdx)
    if envDict.get(key, -1) != -1:
        return envDict[key]

    # 후보 다 봤으면
    if candiIdx >= len(candidates):
        envDict[key] = 0
        return 0

    # orderedDict.items() 가 subscribable 하지 않아서 편법(그냥 리스트로 바꾸면 메모리초과라서)
    fr, toList = next(islice(candidates.items(), candiIdx, None))

    # 이번 후보의 fr이 지금까지 커버한 to 보다 같거나 작으면 그냥 패스
    if fr <= coveredTo:
        result = solution_2(coveredTo, candiIdx+1)
        envDict[key] = result
        return result
    else:
        for to in toList:
            # 새로운 to 까지 덮고 다음 후보 재귀
            result = max(result, solution_2(to, candiIdx+1))
            result += 1
        # 이번 후보를 그냥 패스하고 다음 후보 재귀
        result = max(result, solution_2(coveredTo, candiIdx+1))
    
    envDict[key] = result
    return result


if __name__ == '__main__':
    T = int(sys.stdin.readline().rstrip())
    for _ in range(T):
        N, K = [int(elt) for elt in sys.stdin.readline().rstrip().split()]
        boxes = [int(elt) for elt in sys.stdin.readline().rstrip().split()]
        zeroToISum = {-1: 0}
        patialSum = {}
        candidates = OrderedDict()
        envDict = {}
        camulativeSum = 0
        for idx, box in enumerate(boxes):
            camulativeSum += box
            zeroToISum[idx] = camulativeSum

        result_1 = solution_1(N, K, boxes) % 20091101

        result_2 = solution_2(-1, 0)
        print(str(result_1)+' '+str(result_2))

