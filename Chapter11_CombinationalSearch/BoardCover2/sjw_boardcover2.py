import sys
import os

BLACK = '#'
WHITE = '.'
GLOBAL_MAX = 0
H, W, R, C = 0, 0, 0, 0
NUM_BLACK_IN_BLOCK = 0

# block can be rotated in 4 directions
# remove duplicate if rotated block is same with each other
def preprocess_block(block):
    global R, C
    coordinates = []
    for i in range(R):
        for j in range(C):
            if block[i][j] == BLACK:
                coordinates.append((i, j))

    if (i, j) == (0, 0):
        raise "BLOCK is empty"

    # now we have block represented as relative coordinates
    rotates = [
        coordinates[:],                                         # rorate 0
        [(y, C - 1 - x) for (x, y) in coordinates],             # rorate 90
        [(R - 1 - x, C - 1 - y) for (x, y) in coordinates],     # rorate 180
        [(R - 1 - y, x) for (x, y) in coordinates]              # rorate 270
    ]

    for rotate in rotates:
        rotate.sort()

    # remove duplicate
    uniques = []
    for rotate in rotates:
        if rotate not in uniques:
            uniques.append(rotate)

    # convert to relative coordinate
    relatives = []
    for unique in uniques:
        origin_x, origin_y = unique[0]  # first block is origin since block is sorted by (x, y)
        relatives.append([(x - origin_x, y - origin_y) for (x, y) in unique])

    return relatives


# check if block can be set on given coordinate
def can_set_block(board, block, x, y):
    global H, W
    global_coordinates = [(relative_x + x, relative_y + y) for (relative_x, relative_y) in block]
    for (x, y) in global_coordinates:
        # return false if given coordinate is out of board or already BLACK
        if (x < 0 or x >= H) or (y < 0 or y >= W) or (board[x][y] == BLACK):
            return False

    return True

# set block on given (x, y)
def set_block(board, block, x, y, block_idx):
    # print('set block:', block_idx, x, y)
    global_coordinates = [(relative_x + x, relative_y + y) for (relative_x, relative_y) in block]
    for (x, y) in global_coordinates:
        board[x][y] = BLACK

# unset block on given (x, y)
def unset_block(board, block, x, y):
    global_coordinates = [(relative_x + x, relative_y + y) for (relative_x, relative_y) in block]
    for (x, y) in global_coordinates:
        board[x][y] = WHITE

# num_set_blocks: number of block set until now
# num_black_in_block: number of blacks in block
# num_white_in_board: number of whites in board
# upper_bound can be calculated by (num_white_in_board // num_black_in_block)
def recur(board, blocks, x, y, num_set_blocks, num_white_in_board):
    global GLOBAL_MAX, H, W
    upper_bound = num_white_in_board // NUM_BLACK_IN_BLOCK

    # if smaller than already found max, no need to search more
    if num_set_blocks + upper_bound <= GLOBAL_MAX:
        return

    # if end of board, return
    if (x, y) == (H, W):
        return

    next_x, next_y = (x, y + 1) if y + 1 < W else (x + 1, 0)
    # if board is already BLACK, go to next psition
    if board[x][y] == BLACK:
        recur(board, blocks, next_x, next_y, num_set_blocks, num_white_in_board)
        return

    # iterate over rotated blocks
    for block_idx, block in enumerate(blocks):
        if can_set_block(board, block, x, y):
            set_block(board, block, x, y, block_idx)

            # set global max
            if num_set_blocks + 1 > GLOBAL_MAX:
                GLOBAL_MAX = num_set_blocks + 1
            recur(board, blocks, next_x, next_y, num_set_blocks + 1, num_white_in_board - NUM_BLACK_IN_BLOCK)


            unset_block(board, block, x, y)

    # we can skip (i, j)
    recur(board, blocks, next_x, next_y, num_set_blocks, num_white_in_board - 1)

def solution(board, block, H, W, R, C):
    global GLOBAL_MAX, NUM_BLACK_IN_BLOCK
    GLOBAL_MAX = 0  # set GLOBAL_MAX at each test case
    blocks = preprocess_block(block)
    total_white_in_board = sum(board, []).count(WHITE)
    NUM_BLACK_IN_BLOCK = sum(block, []).count(BLACK)
    recur(board, blocks, 0, 0, 0, total_white_in_board)
    return GLOBAL_MAX


if __name__ == '__main__':
    # freopen equivalent
    abs_path = os.path.dirname(os.path.abspath(__file__))
    sys.stdin = open(os.path.join(abs_path, 'input.txt'), 'r')

    answers = []
    T = int(sys.stdin.readline())
    for _ in range(T):
        H, W, R, C = [int(x) for x in sys.stdin.readline().strip().split()]
        board = []
        for _ in range(H):
            row = [x for x in sys.stdin.readline().strip()]
            board.append(row)
        block = []
        for _ in range(R):
            row = [x for x in sys.stdin.readline().strip()]
            block.append(row)

        answers.append(solution(board, block, H, W, R, C))
    for a in answers:
        print(a)