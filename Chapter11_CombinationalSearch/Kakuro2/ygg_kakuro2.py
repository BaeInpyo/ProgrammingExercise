import sys

answer = []

def solution(board, horiHintDict, vertiHintDict, boardIdx):

    if boardIdx >= (len(board)-1)**2:
        return True

    currY, currX = boardIdx//(len(board)-1)+1, boardIdx%(len(board)-1)+1 # 최외곽 제외 인덱싱

    if board[currY][currX] == 0:
        return solution(board, horiHintDict, vertiHintDict, boardIdx+1)

    for idx, currHint in enumerate(horiHintDict[currY]): 
        if currHint[0] > currX: # 힌트가 있는자리가 현재 x보다 크면 break
            break
        horiHint = horiHintDict[currY][idx]

    for idx, currHint in enumerate(vertiHintDict[currX]): 
        if currHint[0] > currY: # 힌트가 있는자리가 현재 y보다 크면 break
            break
        vertiHint = vertiHintDict[currX][idx]

        #vertiHint = (y, val, candiDict, colWhite) # 현재 위치에서 가장 가까운 수직힌트

    horiCandi = horiHint[3]
    vertiCandi = vertiHint[3]

    possible = set(horiCandi) & set(vertiCandi)
    if len(possible) == 0: # 선택가능한 경우가 없을때
        return False

    maxCandi = min(getMinCandi(horiHint[1], horiHint[2]), getMinCandi(vertiHint[1], vertiHint[2]))
    minCandi = max(getMaxCandi(horiHint[1], horiHint[2]), getMaxCandi(vertiHint[1], vertiHint[2]))

    # 다 통과했으면 이제 본론
    for candi in possible:
        if candi > maxCandi or candi < minCandi:
            continue
        answer[currY][currX] = candi
        horiHint[1] -= candi 
        horiHint[2] -= 1
        vertiHint[1] -= candi 
        vertiHint[2] -= 1
        horiCandiIdx = horiCandi.index(candi)
        vertiCandiIdx = vertiCandi.index(candi)
        horiCandi.pop(horiCandiIdx)
        vertiCandi.pop(vertiCandiIdx)
        if solution(board, horiHintDict, vertiHintDict, boardIdx+1):
            return True
        # 되돌리기
        answer[currY][currX] = 0
        horiCandi.insert(horiCandiIdx, candi)
        vertiCandi.insert(vertiCandiIdx, candi)
        horiHint[1] += candi 
        horiHint[2] += 1
        vertiHint[1] += candi 
        vertiHint[2] += 1

    return False

    
def getNumOfWhite(y, x, t, N, board):
    count = 0
    if t == 0:
        for i in range(x+1, N):
            if board[y][i] == 0:
                break
            count += 1
    else:
        for i in range(y+1, N):
            if board[i][x] == 0:
                break
            count += 1
    return count
    

def getMinCandi(val, numOfWhite):
    if numOfWhite == 1:
        return val
    minLimit = numOfWhite
    minBase = sum(range(1,numOfWhite))
    for i in range(numOfWhite+1,10):
        if minBase + i > val:
            break
        minLimit = i
    return minLimit

def getMaxCandi(val, numOfWhite):
    if numOfWhite == 1:
        return val
    maxLimit = 10-numOfWhite
    maxBase = sum(range(11-numOfWhite,10))
    for i in range(1, maxLimit+1):
        if maxBase + i >= val:
            return i


def getCandi(val, numOfWhite):
    if numOfWhite == 1:
        return [val]

    minLimit = getMinCandi(val, numOfWhite)
    maxLimit = getMaxCandi(val, numOfWhite)

    return list(range(maxLimit, minLimit+1))

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
            numOfWhite = getNumOfWhite(y-1, x-1, t, N, board)
            if t == 0:
                horiHintDict[y-1] = sorted(horiHintDict.get(y-1, [])+[[x-1, val, numOfWhite, getCandi(val, numOfWhite)]],key=lambda x: x[0])
            else:
                vertiHintDict[x-1] = sorted(vertiHintDict.get(x-1, [])+[[y-1, val, numOfWhite, getCandi(val, numOfWhite)]],key=lambda x: x[0])
        

        solution(board, horiHintDict, vertiHintDict, 0)

        for row in answer:
            print(' '.join(map(str,row)))
        


