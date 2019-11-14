import sys
import os

BLACK = '#'
WHITE = '.'

# block can be rotated in 4 directions
# and can be represented as list of relative position of leftmost, topmost
# coordiate
# remove duplicate if rotated block is same with each other
def preprocess_block(block, R, C):
    pass

def solution(board, block, H, W, R, C):
    pass


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
            row = sys.stdin.readline().strip()
            board.append(row)
        block = []
        for _ in range(R):
            row = sys.stdin.readline().strip()
            block.append(row)

    answers.append(solution(board, block, H, W, R, C))
    for a in answers:
        print(a)