import sys
env_dict = {}

def rotate90(block):
    result = [['.'] * len(block) for _ in range(len(block[0]))]
    for r, row in enumerate(block):
        for c in range(len(row)):
            result[c][len(block)-1-r] = block[r][c]
    return result

def checkBlock(r,c,board,block):
    for r_offset, row in enumerate(block):
        for c_offset in range(len(row)):
            if r+r_offset >= len(board) or c+c_offset >= len(board[0]) or (board[r+r_offset][c+c_offset]=='#' and block[r_offset][c_offset]=='#'):
                return 0
    for r_offset, row in enumerate(block):
        for c_offset in range(len(row)):
            if block[r_offset][c_offset]=='#':
                board[r+r_offset][c+c_offset] = '#'
    return 1

def removeBlock(r,c,board,block):
    for r_offset, row in enumerate(block):
        for c_offset in range(len(row)):
            if block[r_offset][c_offset]=='#':
                board[r+r_offset][c+c_offset] = '.'

def solution(board, blocks, idx, blockMax):
    if idx >= len(board)*len(board[0]):
        return 0
    result = 0
    key = (tuple(map(lambda x: ''.join(x),board)),idx)
    if env_dict.get(key, -1) != -1:
        return env_dict[key]
    r = idx//len(board[0])
    c = idx%len(board[0])
    for block in blocks:
        check = checkBlock(r,c,board,block)
        result = max(result, check + solution(board, blocks, idx+1, blockMax-check))
        if check == 1:
            removeBlock(r,c,board,block)
        if result == blockMax:
            env_dict[key] = result
            return result
    env_dict[key] = result
    return result


if __name__ == '__main__':
    sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline().rstrip())
    for _ in range(C):
        env_dict = {}
        H, W, R, C = list(map(int,sys.stdin.readline().rstrip().split()))
        board = [list(sys.stdin.readline().rstrip()) for _ in range(H)]
        block = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
        blocks = [block]
        for _ in range(3):
            block = rotate90(block)
            blocks.append(block)
        dotMax = 0
        for row in board:
            for col in row:
                if col == '.':
                    dotMax += 1
        blockDotMax = 0
        for row in block:
            for col in row:
                if col == '#':
                    blockDotMax += 1
        blockMax = dotMax//blockDotMax
        print(solution(board, blocks, 0, blockMax))



