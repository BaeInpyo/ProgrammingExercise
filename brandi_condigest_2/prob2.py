def read_input():
    N, d = [int(x) for x in input().split()]
    board = []
    for _ in range(N):
        board.append([int(x) for x in input().split()])

    return N, d, board

def solution(N, d, board):
    """
    모든 경우를 다 고려해야 최소경로를 알 수 있음
    대신 한번 구한 경로에 대해서는 DP 적용 가능
    
    dp[i][j] = (0, 0)에서 (i,j)까지의 최소 경로
    """
    
    dp = [[0]*N for _ in range(N)]
    
    # init dp
    dp[0][0] = board[0][0]
    for idx in range(1, N):
        dp[idx][0] = dp[idx-1][0] + board[idx][0]
    for idx in range(1, N):
        dp[0][idx] = dp[0][idx-1] + board[0][idx]
    
    # fill dp
    for idx in range(1, N):
        for jdx in range(1, N):
            dp[idx][jdx] = min(dp[idx-1][jdx], dp[idx][jdx-1]) + board[idx][jdx]
            
    # return answer
    #for row in dp:
    #    print(row)
    answer = d - dp[N-1][N-1]
    answer = max(answer, -1)
    print(answer)


if __name__ == "__main__":
    N, d, board = read_input()
    solution(N, d, board)