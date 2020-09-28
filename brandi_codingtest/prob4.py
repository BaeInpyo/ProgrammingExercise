"""
모든 0(물)인 지점에 대해 거리 d 만큼의 bfs를 실행한 후 물이 퍼진 거리를 확인
"""

from collections import deque

def read_input():
    N, d = [int(x) for x in input().split()]
    board = []
    for _ in range(N):
        row = [int(x) for x in input().split()]
        board.append(row)

    return N, d, board

def bfs(board, row, col, distance):
    """ (row, col)에서 최대 distance만큼 BFS 수행한 후 물의 퍼진 갯수를 return"""
    N = len(board)
    queue = deque([(row, col, 0)])  # (row, col, distance)
    directions = [
        [0, 1],     # right
        [1, 0],     # bottom
        [-1, 0],    # top
        [0, -1]     # left
    ]
    while queue:
        row, col, dist = queue.popleft()

        if 0 <= row < N and 0 <= col < N and board[row][col] == 0:
            board[row][col] = 2 # mark as water spread

        if dist < distance:
            for (dx, dy) in directions:
                new_row, new_col = row+dx, col+dy
                if 0 <= new_row < N and 0 <= new_col < N and board[new_row][new_col] == 0:
                    queue.append((new_row, new_col, dist+1))

    count = 0
    for row in range(N):
        for col in range(N):
            if board[row][col] == 2:
                count += 1

    return count

def solution(N, distance, board):
    """ 모든 0인 점에 대해 bfs를 시도해보고 각각의 물의 퍼진 갯수 중 최대값을 print """
    answer = 0
    for idx in range(N):
        for jdx in range(N):
            if board[idx][jdx] == 1:
                continue

            # copy board
            new_board = [row[:] for row in board]

            # do bfs
            count = bfs(new_board, idx, jdx, distance)

            # apply to answer
            answer = max(answer, count)

    print(answer)

if __name__ == "__main__":
    N, d, board = read_input()
    solution(N, d, board)