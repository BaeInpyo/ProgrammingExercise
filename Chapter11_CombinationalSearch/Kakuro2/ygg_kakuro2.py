import sys

answer = []

def solution(board, horiHintDict, vertiHintDict, idx):

    if idx >= (len(board)-1)**2:
        return True

    currY, currX = idx//(len(board)-1)+1, idx%(len(board)-1)+1 # 최외곽 제외 인덱싱

    if board[currY][currX] == 0:
        return solution(board, horiHintDict, vertiHintDict, idx+1)

    for x, val, candiDict in horiHintDict[currY]: 
        if x > currX: # 힌트가 있는자리가 현재 x보다 크면 break
            break
        horiHint = (x, val, candiDict) # 현재 위치에서 가장 가까운 수평힌트
    for y, val, candiDict in vertiHintDict[currX]: 
        if y > currY: # 힌트가 있는자리가 현재 y보다 크면 break
            break
        vertiHint = (y, val, candiDict) # 현재 위치에서 가장 가까운 수직힌트

    horiCandi = horiHint[2]
    vertiCandi = vertiHint[2]

    filledCount = 0
    filledSumHori = 0
    for x in range(horiHint[0]+1, len(board)):
        if board[currY][x] == 0:
            break
        if answer[currY][x] != 0:
            filledCount += 1
            filledSumHori += answer[currY][x]
        rightMostWhite = x
    horiNumOfWhite = rightMostWhite - horiHint[0] - filledCount

    if sum(horiCandi[:horiNumOfWhite])+filledSumHori > horiHint[1] or sum(horiCandi[-horiNumOfWhite:])+filledSumHori < horiHint[1]: # 제일큰거 n개나 제일작은거 n개 선택해도 만족못하면
        return False

    filledCount = 0
    filledSumVerti = 0
    for y in range(vertiHint[0]+1, len(board)):
        if board[y][currX] == 0:
            break
        if answer[y][currX] != 0:
            filledCount += 1
            filledSumVerti += answer[y][currX]
        bottomMostWhite = y
    vertiNumOfWhite = bottomMostWhite - vertiHint[0] - filledCount

    if sum(vertiCandi[:vertiNumOfWhite])+filledSumVerti > vertiHint[1] or sum(vertiCandi[-vertiNumOfWhite:])+filledSumVerti < vertiHint[1]: # 제일큰거 n개나 제일작은거 n개 선택해도 만족못하면
        return False

    possible = set(horiCandi) & set(vertiCandi)
    if len(possible) == 0: # 선택가능한 경우가 없을때
        return False

    # 다 통과했으면 이제 본론
    for candi in possible:
        if horiNumOfWhite == 1 and filledSumHori+candi != horiHint[1]: # 마지막 자리면
            continue
        if vertiNumOfWhite == 1 and filledSumVerti+candi != vertiHint[1]: # 마지막 자리면
            continue
        if candi >= horiHint[1] or candi >= vertiHint[1]: # 고른놈이 조건보다 더 크면
            continue

        answer[currY][currX] = candi
        horiIdx = horiCandi.index(candi)
        horiCandi.pop(horiIdx)
        vertiIdx = vertiCandi.index(candi)
        vertiCandi.pop(vertiIdx)
        if solution(board, horiHintDict, vertiHintDict, idx+1):
            return True
        # 되돌리기
        answer[currY][currX] = 0
        horiCandi.insert(horiIdx, candi)
        vertiCandi.insert(vertiIdx, candi)

    return False

    

    
if __name__ == '__main__':
    #sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline().rstrip())
    for _ in range(C):
        N = int(sys.stdin.readline().rstrip())
        answer = [[0] * N for _ in range(N)]
        board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
        Q = int(sys.stdin.readline().rstrip())
        horiHintDict = {}
        vertiHintDict = {}
        for _ in range(Q):
            y, x, t, val = list(map(int, sys.stdin.readline().rstrip().split()))
            if t == 0:
                horiHintDict[y-1] = sorted(horiHintDict.get(y-1, [])+[(x-1, val, [1,2,3,4,5,6,7,8,9])],key=lambda x: x[0])
            else:
                vertiHintDict[x-1] = sorted(vertiHintDict.get(x-1, [])+[(y-1, val, [1,2,3,4,5,6,7,8,9])],key=lambda x: x[0])
        

        solution(board, horiHintDict, vertiHintDict, 0)

        for row in answer:
            print(' '.join(map(str,row)))
        


