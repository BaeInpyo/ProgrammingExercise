def solution(string):
    """
    We can count number of adjcent block0 from block1s
    """
    board = [row.split() for row in string.split(";")]
    answer = 0
    m, n = len(board), len(board[0])
    directions = [
        [0, 1],     # right
        [1, 0],     # down
        [-1, 0],    # left
        [0, -1],    # up
    ]
    for idx in range(m):
        for jdx in range(n):
            if board[idx][jdx] == "0":
                continue


            connected = False
            surround = 0
            for (dx, dy) in directions:
                try:
                    adjacent = board[idx+dx][jdx+dy]
                    if adjacent == "0":
                        surround += 1
                    if adjacent == "1":
                        connected = True
                except:
                    pass

            # measure round only if block1 is connected
            if connected:
                answer += surround

    print(answer)

solution("0 0 0 0;0 1 1 0;0 0 1 0;0 0 0 0")