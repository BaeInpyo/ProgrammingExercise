import sys
import os
import itertools

BLOCK_TYPES = [
    [[0,0], [0,1]],
    [[0,0], [1,0]],
    [[0,0], [1,0], [1,1]],
    [[0,0], [0,1], [1,1]],
    [[0,0], [0,1], [1,0]],
    [[0,0], [1,-1], [1,0]]
]

PICK_TYPES = ['.', '#']

# (x,y)에 주어진 block_type의 block을 둘 수 있는지 확인
def is_possible(board, x, y, block_type):
    candidates = [[e[0]+x, e[1]+y] for e in BLOCK_TYPES[block_type]]
    for c in candidates:
        curr_x, curr_y = c
        if 0 <= curr_x < len(board) and 0 <= curr_y < len(board) and board[curr_x][curr_y] == '.':
            continue
        else:
            return False
    return True

# 주어진 board에서 둘 수 있는 모든 경우의 list를 return
def get_next_picks(board):
    results = []    # (x, y, block_type)
    for i in range(len(board)):
        for j in range(len(board)):
            for t in range(len(BLOCK_TYPES)):
                if is_possible(board, i, j, t):
                    results.append((i, j, t))

    return results

# board에 주어진 pick을 놓거나 물리는 함수
def do(board, pick, pick_type):
    x, y, block_type = pick
    for point in BLOCK_TYPES[block_type]:
        curr_x, curr_y = x + point[0], y + point[1]
        board[curr_x][curr_y] = PICK_TYPES[pick_type]

def board_to_int(board):
    flattend = list(itertools.chain.from_iterable(board))
    result = 0
    for i in range(len(flattend)):
        if flattend[i] == '#':
            result += pow(2, i)
    return result

def get_result(board, cache):
    # key = board_to_int(board)
    # if key in cache:
    #     return cache[key]
    flattend = list(itertools.chain.from_iterable(board))
    key = tuple(flattend)
    if key in cache:
        return cache[key]

    next_picks = get_next_picks(board)
    if not next_picks:
        cache[key] = 0  # LOSE
        return 0

    for pick in next_picks:
        do(board, pick, 1)  # block을 놓음
        result = get_result(board, cache)   # 상대방의 결과
        do(board, pick, 0)  # block을 뺌
        if result == 0:
            cache[key] = 1
            return 1

    cache[key] = 0
    return 0

# 0: LOSE, 1: WIN
def solution(board):
    cache = dict()  # key: board, value: 0 or 1
    result = get_result(board, cache)
    results = ['LOSING', 'WINNING']
    return results[result]

if __name__ == '__main__':
    # freopen equivalent
    sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r')

    answers = []
    C = int(sys.stdin.readline().strip())

    for _ in range(C):
        board = []
        for _ in range(5):
            row = sys.stdin.readline().strip()
            row = [x for x in row]
            board.append(row)

        answers.append(solution(board))

    for a in answers:
        print(a)