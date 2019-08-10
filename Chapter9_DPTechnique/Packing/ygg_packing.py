import sys
stuffList = []
envDict = {}

# 집은 물건 리스트를 계속 새롭게 생성해가며 재귀를 돌면 아슬아슬하게 시간초과가 뜸 (알고스팟 제출했던 오답 확인)
# 책의 풀이처럼 차라리 마지막에 findPickedStuff() 과같은 함수를 통해 결과 캐쉬를 돌며 집은 물건을 역추적하는 방식이 시간초과가 안뜸
def solution(currIdx, remainVolume):
    result = 0

    if envDict.get((currIdx, remainVolume), False):
        return envDict[(currIdx, remainVolume)]

    if currIdx >= len(stuffList):
        return 0

    if remainVolume <= 0:
        envDict[(currIdx, remainVolume)] = 0
        return 0

    currStuff = stuffList[currIdx]
    currVolume, currWish = currStuff[1], currStuff[2]

    if remainVolume >= currVolume:
        addCase = solution(currIdx+1, remainVolume-currVolume) + currWish
        passCase = solution(currIdx+1, remainVolume)
        if addCase > passCase:
            envDict[(currIdx, remainVolume)] = addCase
            return addCase
        else:
            envDict[(currIdx, remainVolume)] = passCase
            return passCase
    # 물건리스트는 무게순으로 정렬되어있음, 현재 물건을 더 담지 못한다면 앞으로도 더 못담음
    else:
        envDict[(currIdx, remainVolume)] = 0
        return 0
    

    return result

def findPickedStuff(currIdx, remainVolume):
    if currIdx >= len(stuffList):
        return []
    if envDict.get((currIdx, remainVolume), -1) == -1 or envDict.get((currIdx, remainVolume), -1) == 0:
        return []

    if envDict.get((currIdx, remainVolume), -1) == envDict.get((currIdx+1, remainVolume), -1):
        return findPickedStuff(currIdx+1, remainVolume)
    else:
        currStuff = stuffList[currIdx]
        currVolume, currName = currStuff[1], currStuff[0]
        return [currName] + findPickedStuff(currIdx+1, remainVolume-currVolume)

if __name__ == '__main__':
    #sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline())
    for _ in range(C):
        stuffList = []
        envDict = {}
        N, W = list(map(int, sys.stdin.readline().rstrip().split()))
        for _ in range(N):
            name, volume, wish = sys.stdin.readline().rstrip().split()
            stuffList.append((name, int(volume), int(wish)))
        stuffList.sort(key=lambda x: x[1])
        result = solution(0, W)
        nameList = findPickedStuff(0, W)
        print(result, len(nameList))
        for name in nameList:
            print(name)
