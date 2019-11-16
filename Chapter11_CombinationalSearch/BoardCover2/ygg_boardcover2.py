import sys
#env_dict = {}
globalMax=0
blockMax=0
def rotate90(block):
    result = [['.'] * len(block) for _ in range(len(block[0]))]
    for r, row in enumerate(block):
        for c in range(len(row)):
            result[c][len(block)-1-r] = block[r][c]
    return result

def checkBlock(r,c,board,block):
    count = 0 if board[r][c]=='#' else 1
    for r_offset, row in enumerate(block):
        for c_offset in range(len(row)):
            if r+r_offset >= len(board) or c+c_offset >= len(board[0]):
                return (0, 0)
            elif board[r+r_offset][c+c_offset]=='#' and block[r_offset][c_offset]=='#':
                return (0, 0 if board[r][c]=='#' else 1)
    for r_offset, row in enumerate(block):
        for c_offset in range(len(row)):
            if block[r_offset][c_offset]=='#':
                board[r+r_offset][c+c_offset] = '#'
                if r_offset != 0 or c_offset != 0:
                    count += 1
    return (1,count)

def removeBlock(r,c,board,block):
    for r_offset, row in enumerate(block):
        for c_offset in range(len(row)):
            if block[r_offset][c_offset]=='#':
                board[r+r_offset][c+c_offset] = '.'

def solution(board, blocks, idx, nDot, nBlockDot, currNBlock):
    if idx >= len(board)*len(board[0]):
        return currNBlock

    #key = (tuple(map(lambda x: ''.join(x),board)),idx)
    #if env_dict.get(key, -1) != -1:
    #    return env_dict[key]

    global globalMax
    global blockMax

    r = idx//len(board[0])
    c = idx%len(board[0])

    if currNBlock + nDot//nBlockDot <= globalMax: # 지금까지 놓은 갯수랑 지금부터 더 놓을수있는 이론상 갯수를 합쳐도 현재의 글로벌 맥스보다 작거나 같으면 더 볼 필요없음
        return globalMax

    for block in blocks:
        check, checkDots = checkBlock(r,c,board,block)
        if check == 1:
            globalMax = max(globalMax, currNBlock+check)
            globalMax = max(globalMax, solution(board, blocks, idx+1, nDot-checkDots, nBlockDot, currNBlock+check))
            removeBlock(r,c,board,block)
            if globalMax == blockMax:
                #env_dict[key] = globalMax
                return globalMax
    globalMax = max(globalMax, solution(board, blocks, idx+1, nDot-(0 if board[r][c]=='#' else 1), nBlockDot, currNBlock)) # 안놓는 케이스
    #env_dict[key] = globalMax
    return globalMax


if __name__ == '__main__':
    sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline().rstrip())
    for _ in range(C):
        #env_dict = {}
        globalMax = 0
        H, W, R, C = list(map(int,sys.stdin.readline().rstrip().split()))
        board = [list(sys.stdin.readline().rstrip()) for _ in range(H)]
        block = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
        blocks = [block]
        for _ in range(3):
            block = rotate90(block)
            blocks.append(block)
        nDot = 0
        for row in board:
            for col in row:
                if col == '.':
                    nDot += 1
        nBlockDot = 0
        for row in block:
            for col in row:
                if col == '#':
                    nBlockDot += 1
        blockMax = nDot//nBlockDot
        print(solution(board, blocks, 0, nDot, nBlockDot, 0))



