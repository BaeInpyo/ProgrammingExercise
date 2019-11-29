import sys, os
from itertools import combinations
from collections import defaultdict


COMB_DICT = defaultdict(list)  # key: (sum, count), value: list of combinations
BLACK, WHITE = 0, 1

# freopen equivalent
abs_path = os.path.abspath(os.path.dirname(__file__))
sys.stdin = open(os.path.join(abs_path, 'input.txt'), 'r')

'''
board를 좌상단에서 우하단으로 돌면서 white block을 채운다.
white block에는 1-9까지가 가능하지만, 좌측 힌트와 상단 힌트를 고려하여 실제로는 더 적은 갯수의 숫자가 가능하다.
'''


"""
COMB_DICT[(sum, count)] = list of possible combinations of numbers in [1, ... 9]
"""
def init_combdict():
    global COMB_DICT
    numbers = range(1, 10)
    for count in range(1, 10):
        combs = combinations(numbers, count)
        for comb in combs:
            _sum = sum(comb)
            COMB_DICT[(_sum, count)].append(set(comb))

# return next position of (y, x)
def get_next_point(y, x, N):
    next_x = (x + 1) % N
    next_y = y + (x + 1) // N
    return next_y, next_x


"""
Return list of numbers that can be placed in (y, x)
This is determined using hints dependent on (y, x)
"""
def get_candidates(board, coordinate_to_hint, y, x):
    result = set(range(1, 10))

    # there can be atmost 2 hints
    for hint in coordinate_to_hint[(y, x)]:
        _result = set()
        for comb in hint['possible_sum_combinations']:
            """
            comb must contain picked
            e.g, in case of hint in (0, 6) whose count is 2 and sum is 12
            if we select 9 first, then we only can use 3 as second
            """
            if set.issubset(hint['picked'], comb):
                _result.update(comb - hint['picked'])

        result = set.intersection(result, _result)

    return result


# return true if success to fill all white cells
def recur(board, coordinate_to_hint, curr_y, curr_x):
    N = len(board)
    # arrive end of block
    if curr_y == N:
        return True

    next_y, next_x = get_next_point(curr_y, curr_x, N)

    # skip black cell
    if board[curr_y][curr_x] == BLACK:
        return recur(board, coordinate_to_hint, next_y, next_x)

    # main
    candidates = get_candidates(board, coordinate_to_hint, curr_y, curr_x)
    for num in candidates:
        # select number and set board and coordinate_to_hint
        board[curr_y][curr_x] = num
        for hint in coordinate_to_hint[(curr_y, curr_x)]:
            hint['picked'].add(num)

        # go deeper
        result = recur(board, coordinate_to_hint, next_y, next_x)

        # answer is found
        if result:
            return True

        # rever selection
        board[curr_y][curr_x] = 1
        for hint in coordinate_to_hint[(curr_y, curr_x)]:
            hint['picked'].remove(num)

    # no answer is found from (curr_y, curr_x)
    return False


"""
main function
"""
def solution(board, hint):
    coordinate_to_hint = preprocess(board, hint)
    _ = recur(board, coordinate_to_hint, 0, 0)  # _ must be true because answer always exists
    for row in board:
        print(' '.join([str(x) for x in row]))

    return


"""
1. Convert hint to hint_dict
2. Make dictionary whose key is (y, x) of white block and value is list of hints dependent

hint_dict = {
  'y': y
  'x': x
  'direction': direction
  'sum': sum
  'count': number of white points to cover
  'possible_sum_combinations': list of set which represents combination of nubmers
  'picked': set of picked numbers
}

:param board:   2d list which represents board
:param hint:    (y, x, direction, sum) of input hint
:return:        coordinate_to_hint dict
"""
def preprocess(board, hint):
    N = len(board)
    coordinate_to_hint = defaultdict(list)
    for h in hint:
        y, x, direction, _sum = h
        y, x = y - 1, x - 1 # convert to zero base
        hint_dict = {
            'y': y,
            'x': x,
            'direction': direction,
            'sum': _sum,
            'count': 0,
            'possible_sum_combinations': [],
            'picked': set(),
        }

        dy, dx = (0, 1) if direction == 0 else (1, 0)
        white_points = set()
        curr_y, curr_x = y + dy, x + dx
        while curr_y < N and curr_x < N:
            if board[curr_y][curr_x] == WHITE:
                white_points.add((curr_y, curr_x))
            else:
                break

            curr_y, curr_x = curr_y + dy, curr_x + dx

        hint_dict['count'] = len(white_points)
        hint_dict['possible_sum_combinations'] = COMB_DICT[(_sum, len(white_points))]

        for (y, x) in white_points:
            coordinate_to_hint[(y, x)].append(hint_dict)

    return coordinate_to_hint


# return board, hint
def read_input():
    N = int(sys.stdin.readline().strip())
    board = []
    for _ in range(N):
        row = [int(x) for x in sys.stdin.readline().strip().split()]
        board.append(row)

    Q = int(sys.stdin.readline().strip())
    hint = []
    for _ in range(Q):
        row = [int(x) for x in sys.stdin.readline().strip().split()]
        hint.append(row)

    return board, hint


if __name__ == '__main__':
    init_combdict()
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        board, hint = read_input() # read input
        solution(board, hint)
