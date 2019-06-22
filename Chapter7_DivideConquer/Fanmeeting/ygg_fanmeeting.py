#!/bin/python3

import sys

# case가 'MMMMMMMMM' , 'MMMMMMMMMMMMMMMMM' 이런거일때 결국 n제곱..
def solution(members, maleFans, totalCase):
    result = 0
    failCaseDict = {}
    for memberIdx in range(len(members)):
        member = members[memberIdx]
        if member == 'F':
            continue
        else:
            for maleFanIdx in maleFans:
                caseIdx = maleFanIdx - memberIdx
                if not(caseIdx < 0 or caseIdx >= totalCase):
                    failCaseDict[caseIdx] = 1

    result = totalCase - sum(failCaseDict.values())
    return result


if __name__ == '__main__':
    C = int(sys.stdin.readline())
    for _ in range(C):
        members = sys.stdin.readline().rstrip()
        fans = sys.stdin.readline().rstrip()
        maleFans = []
        for idx in range(len(fans)):
            fan = fans[idx]
            if fan == 'M':
                maleFans.append(idx)

        totalCase = len(fans)-len(members)+1
        print(solution(members, maleFans, totalCase))

