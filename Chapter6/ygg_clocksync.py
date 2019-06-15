#!/bin/python3

import os
import sys

"""
핵심 : 스위치를 네번 누르는것은 안누른것과 같고 서로다른 스위치를 누르는 순서는 상관이 없다
"""

switchCount = {
    0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0
}

switches = {
    0: [0, 1, 2],
    1: [3, 7, 9, 11],
    2: [4, 10, 14, 15],
    3: [0, 4, 5, 6, 7],
    4: [6, 7, 8, 10, 12],
    5: [0, 2, 14, 15],
    6: [3, 14, 15],
    7: [4, 5, 7, 14, 15],
    8: [1, 2, 3, 4, 5],
    9: [3, 4, 5, 9, 13]
}

def pushSwitch(clocks, switchIdx, count):
    switch = switches[switchIdx]
    for clockIdx in switch:
        clock = (clocks[clockIdx]+3*count)%12
        if clock == 0:
            clock = 12
        clocks[clockIdx] = clock
    switchCount[switchIdx] = switchCount[switchIdx]+count
    return

def undoSwitch(clocks, switchIdx, count):
    switch = switches[switchIdx]
    for clockIdx in switch:
        clock = (clocks[clockIdx]-3*count)%12
        if clock == 0:
            clock = 12
        clocks[clockIdx] = clock
    switchCount[switchIdx] = switchCount[switchIdx]-count
    return

def checkClocks(clocks):
    return (sum(clocks) == 12*16)

def solution(clocks, switchDepth, currPushCount, minPushCount):
    #print(clocks, switchCount, currPushCount)
    if currPushCount >= minPushCount: # 가지를 줄이기위한 트릭
        return minPushCount

    if checkClocks(clocks):
        return currPushCount

    if switchDepth == 10: # 바닥케이스, 10스위치 모두 작동시켜봤을때 답이안되면
        return minPushCount

    for count in range(4): # 총 가지 갯수는 4^10개, 콜 깊이는 10뎁스
        pushSwitch(clocks, switchDepth, count)
        minPushCount = min(solution(clocks, switchDepth+1, currPushCount+count, minPushCount), minPushCount)
        undoSwitch(clocks, switchDepth, count)

    return minPushCount

if __name__ == '__main__':
    C = int(input())
    for _ in range(C):
        clocks = list(map(int, input().rstrip().split()))
        result = solution(clocks, 0, 0, 31) # 최악의 경우 답은 30, 즉, 31이면 답이없음
        if result == 31:
            print(-1)
        else:
            print(result)
