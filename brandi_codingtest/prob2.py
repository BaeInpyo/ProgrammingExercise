"""
1. (1, 1)부터 물의 전이를 simulation하고 물이 전이된 곳의 좌표를 저장
2. 1을 k번째 했을 때 모인 점들 중에서 (N, N)까지의 거리가 k가 되면 1을 중지
3. 2에서 구한 k에 대해서, (N,N)으로부터 거리가 k인 모든 점이 물 방지벽 설치의 고려대상이됨
4. 3의 모든 대상에 대해 실제로 방지벽을 설치해보고, 1에서 한 것처럼 물의 전이를 실행하되 가능한한
끝까지 실행한 후 안전지대의 갯수를 구함
5. 4의 결과중 최대값이 정답
"""

from collections import deque

def parse_input():
    """ Parse input and return (N, board) """
    N = int(input())
    board = []
    for idx in range(N):
        row = [int(x) for x in input().split()]
        board.append(row)

    # print("N, board:", N, board)
    return N, board

def bfs(board, row, col, step):
    """ Do BFS from (row, col) and return newly added cells
    0: 흐를 수 있는곳
    1: 흐를 수 없는곳 (벽포함)
    2: 물이 찬곳
    """
    N = len(board)
    directions = [
        [0, 1],     # right
        [1, 0],     # bottom
        [-1, 0],    # left
        [0, -1],    # top
    ]
    new_cells = set()

    for (dx, dy) in directions:
#        print("point:", row+dx, col+dy, board)
        if 0 <= row+dx < N \
            and 0 <= col+dy < N \
            and board[row+dx][col+dy] == 0:
 #           print("add:", row+dx, col+dy)
            new_cells.add((row+dx, col+dy))
            board[row+dx][col+dy] = 2

    return step+1, new_cells

def solution(N, board):
  #  print("init board:", board)
    # copy original board
    new_board = [row[:] for row in board]

    visited = dict()
    reached = False
    queue = deque([(1,1,0)])  # (row, col, step)
    new_board[1][1] = 2
    while queue:
   #     print("queue:", queue)
        row, col, step = queue.popleft()
        new_step, new_cells = bfs(new_board, row, col, step)

        reached = False
        for (row, col) in new_cells:
            if row+col >= 2*N-2-new_step:
    #            print("reach:", row, col, new_step)
                # 2단계 성공
                reached = new_step
                break

            queue.append((row, col, new_step))

        # 2단계가 성공했으면 그 결과를 reached에 저장하고 BFS 중지
        if reached:
            break

    #print("reached:", reached)

    # 3. 방지벽 설치 후보 저장
    candidates = set()
    for idx in range(N-1-reached, N):
        for jdx in range(N-1-reached, N):
            if idx+jdx >= 2*N-2-reached and board[idx][jdx] == 0:
                candidates.add((idx, jdx))

    # 물의 시작점과 홍현이의 시작점에는 방지벽 설치 불가능
    candidates.discard((1, 1))
    candidates.discard((N-1, N-1))

    #print("candidates:", candidates)

    # 4. 3의 방지벽 설치 후보에 대해 실제로 방지벽을 설치해보고 bfs를 끝까지 실행한 후 안전지대 갯수를 구함
    answer = [0]    # 0을 추가함으로써 candidates가 하나도 없는 경우까지 고려
    for (row, col) in candidates:
        new_board = [row[:] for row in board]
        new_board[row][col] = 1 # 방지벽 설치
        queue = deque([(1,1,0)])  # (row, col, step)
        while queue:
            row, col, step = queue.popleft()
            new_step, new_cells = bfs(new_board, row, col, step)
            for (row, col) in new_cells:
                queue.append((row, col, new_step+1))

        # bfs 종료, 안전지대 갯수 구하기
        count = 0
        for row in range(N):
            for col in range(N):
                if (row, col) not in [(1,1), (N-1,N-1)] and new_board[row][col] == 0:
                    count += 1

        answer.append(count)

    # 5. 4의 결과중 최대값이 정답
    print(max(answer))

if __name__ == "__main__":
    N, board = parse_input()
    solution(N, board)