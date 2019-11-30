import sys

BLACK = '#'
WHITE = '.'
BLOCKS = [
    [(0, 0), (0, 1), (1, 0)],
    [(0, 0), (1, -1), (1, 0)],
    [(0, 0), (1, 0), (1, 1)],
    [(0, 0), (0, 1), (1, 1)]
]


def inrange(num, end):
    if 0 <= num < end:
        return True
    else:
        return False


def solution(board, fill_once=False):
    H = len(board)
    W = len(board[0])
    ans = 0

    # find first white pane from (x, y)
    x_white, y_white = None, None
    for i in range(H):
        for j in range(W):
            if board[i][j] == WHITE:
                x_white, y_white = i, j
                break

        if x_white is not None and y_white is not None:
            break

    # all board are black
    if x_white is None and y_white is None:
        if fill_once:
            return 1
        else:
            return 0

    for block in BLOCKS:
        p1, p2, p3 = [(x_white+a, y_white+b) for (a, b) in block]

        # skip if block is not in board
        if not (inrange(p1[0], H) and inrange(p1[1], W)
                and inrange(p2[0], H) and inrange(p2[1], W)
                and inrange(p3[0], H) and inrange(p3[1], W)):
            continue

        if board[p1[0]][p1[1]] == WHITE and board[p2[0]][p2[1]] == WHITE and board[p3[0]][p3[1]] == WHITE:
            # fill board
            board[p1[0]][p1[1]] = BLACK
            board[p2[0]][p2[1]] = BLACK
            board[p3[0]][p3[1]] = BLACK

            ans += solution(board, fill_once=True)

            # unfill board
            board[p1[0]][p1[1]] = WHITE
            board[p2[0]][p2[1]] = WHITE
            board[p3[0]][p3[1]] = WHITE

    return ans


if __name__ == '__main__':
    # freopen equivalent
    sys.stdin = open('input.txt', 'r')

    C = int(sys.stdin.readline().strip())
    answers = []

    for _ in range(C):
        H, W = [int(x) for x in sys.stdin.readline().strip().split()]
        board = []
        for _ in range(H):
            line = [x for x in sys.stdin.readline().strip()]
            board.append(line)

        answers.append(solution(board))

    for a in answers:
        sys.stdout.write('{}\n'.format(a))
