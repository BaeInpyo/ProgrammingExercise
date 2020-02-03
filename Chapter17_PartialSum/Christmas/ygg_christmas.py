import sys
import math
zeroToISum = {}
candidates = [] # (fr, to) List, fr순으로 정렬
remainderDict = {}
fact = math.factorial

def getPatialSum(fr, to):
    return zeroToISum[to]-zeroToISum[fr-1]

def solution_1(N, K, boxes):
    result = 0
    for remainder, idxList in remainderDict.items():
        if len(idxList) < 2:
            continue
        
        result += fact(len(idxList)) // (fact(2)*fact(len(idxList)-2))

        # idxList 는 들어갈때 이미 정렬되어있음.
        for n in range(len(idxList)):
            if n == len(idxList)-1:
                break
            fr, to = idxList[n]+1, idxList[n+1]
            candidates.append((fr, to)) # 어떤 idx가 fr이 되는 candidates는 해당 remainder의 pool 에서만 발생함. 그중 가장 짧은 candidates쌍인 연속한 fr to들을 candidates로 등록.

    return result
            
def solution_2(coveredTo):
    #***** candidates 는 fr순 으로 정렬되어있고 각 fr에 대한 to는 유니크하게 하나뿐임(가장 짧은 쌍)****
    result = 0

    for currIdx in range(len(candidates)):
        fr, to = candidates[currIdx]
        # 이번 후보의 fr이 지금까지 커버한 to 보다 같거나 작으면
        if fr <= coveredTo: 
            # 그리고 이번 후보의 to가 지금까지 커버한 to 보다 작으면 이번후보의 to로 바꿔줌(더 짧게), result 갯수는 그대로(대체해주는것일 뿐이니까)
            if to < coveredTo:
                coveredTo = to
            # 그렇지않으면 놓지않고(놓지 못하고) continue
        # 이번 후보의 fr이 지금까지 커버한 to보다 커서 놓을수 있으면 result +1하고 coveredTo를 바꿔줌
        else:
            coveredTo = to
            result += 1

    return result


if __name__ == '__main__':
    #sys.stdin = open('input.in', 'r')
    T = int(sys.stdin.readline().rstrip())
    for _ in range(T):
        N, K = [int(elt) for elt in sys.stdin.readline().rstrip().split()]
        boxes = [int(elt) for elt in sys.stdin.readline().rstrip().split()]
        zeroToISum = {-1: 0}
        candidates = []
        remainderDict = {0: [-1]}
        camulativeSum = 0
        for idx, box in enumerate(boxes):
            camulativeSum += box
            zeroToISum[idx] = camulativeSum
            remainder = camulativeSum % K
            if remainderDict.get(remainder, -1) == -1:
                remainderDict[remainder] = [idx]
            else:
                remainderDict[remainder].append(idx)

        result_1 = solution_1(N, K, boxes) % 20091101
        candidates.sort(key=lambda x:x[0]) # fr 순으로 정렬
        result_2 = solution_2(-1)
        print(str(result_1)+' '+str(result_2))
