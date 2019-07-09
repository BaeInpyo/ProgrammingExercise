#!/bin/python3

import sys

resultDict = {}

def checkScore(numbers):
    passMap = [True, True, True, True, True] # 모든 숫자가 같을때, 단조증가, 단조감소, 진동, 등차
    scores = [1,2,2,4,5]
    diffForSeq = abs(numbers[0]-numbers[1])
    for currIdx in range(len(numbers)-1):
        currNum, nextNum = numbers[currIdx], numbers[currIdx+1]
        if passMap[0]: # 지금까지 확인한 모든 숫자가 같을때
            if currNum != nextNum:
                passMap[0]=False
        if passMap[1]: # 지금까지 단조증가
            if currNum != nextNum-1:
                passMap[1]=False
        if passMap[2]: # 지금까지 단조감소
            if currNum != nextNum+1:
                passMap[2]=False
        if passMap[3]: # 지금까지 진동
            if currIdx >= len(numbers)-2:
                pass
            else:
                if currNum != numbers[currIdx+2]:
                    passMap[3]=False
        if passMap[4]: # 지금까지 등차
            if abs(currNum - nextNum) != diffForSeq:
                passMap[4]=False

    try:
        return scores[passMap.index(True)]
    except:
        return 10
        

def solution(numbers, currIdx):

    if resultDict.get(currIdx, False): # 이미 기억하고 있는 결과면 바로 반환
        return resultDict.get(currIdx)

    # base cases
    if currIdx >= len(numbers)-5:
        if currIdx > len(numbers)-3: # 불가능 케이스
            resultDict[currIdx] = 40000
            return 40000
        threeScore = checkScore(numbers[currIdx:currIdx+3])
        if currIdx == len(numbers)-3:
            resultDict[currIdx] = threeScore
            return threeScore
        fourScore = checkScore(numbers[currIdx:currIdx+4])
        if currIdx == len(numbers)-4:
            resultDict[currIdx] = fourScore 
            return fourScore
        fiveScore = checkScore(numbers[currIdx:currIdx+5])
        if currIdx == len(numbers)-5:
            resultDict[currIdx] = fiveScore 
            return fiveScore

    else:
        threeScore = checkScore(numbers[currIdx:currIdx+3])
        fourScore = checkScore(numbers[currIdx:currIdx+4])
        fiveScore = checkScore(numbers[currIdx:currIdx+5])

        result = min([
            threeScore + solution(numbers, currIdx+3),
            fourScore + solution(numbers, currIdx+4),
            fiveScore + solution(numbers, currIdx+5)
        ])
        resultDict[currIdx] = result

        return result


if __name__ == '__main__':
    C = int(sys.stdin.readline())
    for _ in range(C):
        resultDict = {}
        numbers = list(map(int, list(sys.stdin.readline().rstrip())))

        print(solution(numbers, 0))
