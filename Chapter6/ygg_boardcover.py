#!/bin/python3

"""
핵심 : 지금 위치는 항상 보드의 제일 왼쪽 제일 위이다. 이자리를 채우는 방법은 네가지 밖에 없다.
즉, 지금 자리의 위쪽이나 왼쪽을 채우게 놓는경우는 생각할 필요가 없다.
또한 만약 이 네가지 방법으로 모두 놓을수 없다면 그 케이스는 더 볼 필요없이 fail case다
"""

import os
import sys

fourWay = [[(0,1), (1,0)],[(0,1),(1,1)],[(1,0),(1,1)],[(1,0),(1,-1)]]

def checkBoard(H,W,board):
    result = sum(list(map(sum, board)))
    if result == H*W + 2*(H+W+2):  # 테두리도 계산해주기
        return 1
    else:
        return 0

def drawBoard(board,block):
    for h, w in block:
        if board[h][w]:
            return False
    for h, w in block:
        board[h][w] = True
    return True

def undoBoard(board,block):
    for h, w in block:
        board[h][w] = False

def getCurrentHW(H,W,current):
    return int(current/W)+1, current%W+1 # 테두리 만든거 +1

def debug(c):
    if c:
        return '#'
    else:
        return '.'

def solution(H,W,board,current):
    result = 0

    #print(current, '\n')
    #for line in board:
    #    print(list(map(debug,line)))
    #print('\n')

    if current == H*W:
        return checkBoard(H,W,board)

    currH, currW = getCurrentHW(H,W,current)

    if board[currH][currW]: # 이미 색칠되어 있는자리면 다음칸으로 이동
        return solution(H,W,board,current+1)

    for way in fourWay:
        block = [(currH,currW),(currH+way[0][0],currW+way[0][1]),(currH+way[1][0],currW+way[1][1])]
        if drawBoard(board,block):
            result += solution(H,W,board,current+1)
            undoBoard(board,block)

    # 색칠 안하고 넘어가는 케이스 - 맨위 핵심대로하면 생각할 필요가 없다
    # result += solution(H,W,board,current+1)

    return result

def boardToBool(c):
    if c == '#':
        return True
    return False

if __name__ == '__main__':
    C = int(input())
    for _ in range(C):
        H, W = list(map(int, input().rstrip().split()))
        board = [[True]*(W+2)]
        for _ in range(H):
            board.append([True]+list(map(boardToBool, input().rstrip()))+[True])
        board.append([True]*(W+2))

        print(solution(H,W,board,0))
