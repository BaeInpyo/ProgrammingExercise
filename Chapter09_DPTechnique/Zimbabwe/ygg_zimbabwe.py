import sys
envDict = {}

def solution(e, m, idx, rest, candList, allCase):
    result = 0
    order = len(e) - idx -1

    if envDict.get((allCase,rest, ''.join(map(str,candList))), -1) != -1:
        return envDict[(allCase,rest, ''.join(map(str,candList)))]

    if idx == len(e)-1:
        if candList.index(1)%m == rest:
            result = 1
        else:
            result = 0
    else:
        for cand, count in enumerate(candList):
            if count != 0:
                nextRest = (rest - (int(cand) * 10**order)%m)%m # 다음 콜에서 맞춰야할 나머지 수 = (현재 목표 나머지 - 현재 자릿수의 나머지)%m
                candList[cand] -= 1
                if not allCase:
                    if cand == int(e[idx]):
                        result += solution(e, m, idx+1, nextRest, candList, False)
                    elif cand < int(e[idx]):
                        result += solution(e, m, idx+1, nextRest, candList, True)
                else:
                    result += solution(e, m, idx+1, nextRest, candList, True)
                candList[cand] += 1

    envDict[(allCase,rest, ''.join(map(str,candList)))] = result
    return result

if __name__ == '__main__':
    #sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline())
    for _ in range(C):
        envDict = {}
        e, m = list(map(int, sys.stdin.readline().rstrip().split()))
        candList = [0]*10
        for cand in list(str(e)):
            candList[int(cand)] += 1

        if e%m == 0:
            itSelf = 1
        else:
            itSelf = 0
        print(solution(str(e), m, 0, 0, candList, False)-itSelf)
