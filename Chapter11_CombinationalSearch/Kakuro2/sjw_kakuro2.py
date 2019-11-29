import sys, os
from itertools import combinations
from collections import defaultdict


# freopen equivalent
abs_path = os.path.abspath(os.path.dirname(__file__))
sys.stdin = open(os.path.join(abs_path, 'input.txt'), 'r')


'''
Strategy
Search from (0, 0) to (N-1, N-1) with giving priority to horizontal direction.
At each white cell (y, x), find possible numbers to place and call recursive function starts at next of (y, x).

To find possible numbers to locate at (y, x), we can consider
1. hints that can affect (y, x), especially, possible combinations of numbers to satisfy hint
2. picked numbers before (y, x)

For example, when we find possible numbers at (2, 2) we need to look hints in (0, 2) whose sum is 30 and (2, 0) whose sume is 17.
Hint 17 can be made with 2 numbers: (8, 9)
Hint 30 can be made with 4 numbers: (6, 7, 8, 9)
This is not good example because only 9 is possible at (2, 2).
But anyway, in general cases, you also need to consider numbers in (2, 1) and (1, 2) to avoid same number in single hint.

NOTES
- COMB_DICT is a dictionary that is pre-calculated to find possible combinations of numbers when (count, sum) is given.
- I used hint_dict to represent hint well
'''


COMB_DICT = defaultdict(list)  # key: (sum, count), value: list of combinations
BLACK, WHITE = 0, 1


'''
Initialize COMB_DICT. This function is executed only once.
'''
def init_combdict():
    global COMB_DICT
    numbers = range(1, 10)
    for count in range(1, 10):
        combs = combinations(numbers, count)
        for comb in combs:
            _sum = sum(comb)
            COMB_DICT[(count, _sum)].append(set(comb))

'''
Return next position of (y, x)
'''
def get_next_point(y, x, N):
    next_x = (x + 1) % N
    next_y = y + (x + 1) // N
    return next_y, next_x


'''
Return list of numbers that can be placed in (y, x)
As stated in Strategy at the top of this file, this function will check both (count, sum) of dependent hint and picked numbers previously
:param board:               board to fill
:param coordinate_to_hint:  dictionary whose key is (y, x) and value is list of hints that can affect (y, x)
:param y:                   coordinate of y
:param x:                   coordinate of x
:return:                    set of numbers that can be placed in (y, x)
'''
def get_candidates(board, coordinate_to_hint, y, x):
    result = set(range(1, 10))

    # there can be atmost 2 hints
    for hint in coordinate_to_hint[(y, x)]:
        _result = set()
        for comb in hint['possible_sum_combinations']:
            """
            Comb must be a superset of picked numbers.
            E.g, in case of hint in (0, 6) whose count is 2 and sum is 12,
            (3, 9), (4, 8), (5, 7) is possible combination.
            If we select 9 first, then we only can use 3 as second number.
            """
            if set.issubset(hint['picked'], comb):
                _result.update(comb - hint['picked'])

        result = set.intersection(result, _result)

    return result


'''
Recursive function to search. Return true if answer is found.
:param board:               board to fill
:param coordinate_to_hint:  dictionary whose key is (y, x) and value is list of hints that can affect (y, x)
:param curr_y:              coordinate of y
:param curr_x:              coordinate of x
:return:                    boolean value whether answer is found
'''
def recur(board, coordinate_to_hint, curr_y, curr_x):
    N = len(board)

    # arrive at the end of block
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


def solution(board, hint):
    coordinate_to_hint = preprocess(board, hint)
    _ = recur(board, coordinate_to_hint, 0, 0)  # _ must be true because answer always exists
    for row in board:
        print(' '.join([str(x) for x in row]))

    return


'''
1. Convert hint to hint_dict
2. Make dictionary whose key is (y, x) of white cell and value is list of hints that can affect (y, )

hint_dict = {
  'y': y
  'x': x
  'direction': direction
  'sum': sum
  'count': number of white points to cover
  'possible_sum_combinations': list of set which represents combination of nubmers
  'picked': set of picked numbers previously
}

:param board:   2d list which represents board
:param hint:    (y, x, direction, sum) of input hint
:return:        coordinate_to_hint dict
'''
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

        count = len(white_points)
        hint_dict['count'] = count
        hint_dict['possible_sum_combinations'] = COMB_DICT[(count, _sum)]

        for (y, x) in white_points:
            coordinate_to_hint[(y, x)].append(hint_dict)

    return coordinate_to_hint


'''
Function to read input
:return:    (board, hint)
'''
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
