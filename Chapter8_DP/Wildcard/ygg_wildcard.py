#!/bin/python3

import sys

"""
핵심 : *을 포함한 반복되는 토큰이 있을 시 겹치는 재귀콜(이미 한번 확인한 환경을 다시 확인하는 것)이 발생하게 된다. 
      따라서 한번 실패를 확인한 환경은 기억을 해두도록 구현한다.
"""

envDict = {}

def solution(W, fileName):

    wIdx = 0
    for charIdx in range(len(fileName)):
        if wIdx >= len(W): # 와일드카드 토큰을 다 소모했는데 아직 읽을 문자가 남아있으면 false
            return False

        currChar = fileName[charIdx]
        token = W[wIdx]

        if token == '?' or token == currChar:
            wIdx += 1
            continue
            
        elif token == '*':
            nextW, nextFileName = W[wIdx:], fileName[charIdx+1:]
            # *을 소모하지않는 케이스 먼저 확인. 최대깊이 = 10000? No 100? Yes 
            # but, *이 반복될때 환경이 겹치는 경우가 생기는데 이를 중복해서 계산하게된다. 이것을 기억한다면?
            if envDict.get((nextW, nextFileName), False): # 이미 실패를 확인한 환경이면
                pass
            else:
                if solution(nextW, nextFileName): 
                    return True
                else: # 해당 환경에 대한 콜이 false로 끝났으면 이를 기억
                    envDict[(nextW, nextFileName)] = True

            wIdx += 1 # *을 소모하는 케이스로
            continue 
            
        else: # 토큰과 현재 문자가 같지 않으면 false
            return False

    # 파일네임을 끝까지 봤을때
    if wIdx >= len(W): # 토큰도 모두 소모했다면
        return True
    else: # 토큰이 남아있다면 남아있는 토큰이 모두 *인지 확인
        for restToken in W[wIdx:]:
            if restToken != '*':
                return False
        return True
    


if __name__ == '__main__':
    C = int(sys.stdin.readline())
    for _ in range(C):
        W = sys.stdin.readline().rstrip()
        n = int(sys.stdin.readline())
        currCase = []
        for _ in range(n):
            fileName = sys.stdin.readline().rstrip()
            currCase.append(fileName)
        currCase.sort()
        for fileName in currCase:
            envDict = {}
            if solution(W, fileName):
                print(fileName)

