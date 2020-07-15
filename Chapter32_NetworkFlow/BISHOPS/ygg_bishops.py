import sys

def dfs(l, r_length, adj, l_matches, r_matches, visited):
    if l in visited: # 자리뺏고뺏다가 사이클나면
        return False
    visited.add(l)
    for r in range(r_length):
        if adj[l][r]: # 간선이 존재하면
            if r_matches[r] == -1: # 아직 매칭되지않은 r 이면 바로 증가경로 찾음
                l_matches[l] = r
                r_matches[r] = l
                return True
            elif dfs(r_matches[r], r_length, adj, l_matches, r_matches, visited): # dfs로 찾아들어갔을때 증가경로가 있으면 자리뺏음(역간선 탐색)
                l_matches[l] = r
                r_matches[r] = l
                return True

    return False

def solution():
    pass
    
if __name__ == '__main__':
    sys.stdin = open('input.in', 'r')
    T = int(sys.stdin.readline().rstrip())
    for _ in range(T):
        N = int(sys.stdin.readline().rstrip())
        board = [sys.stdin.readline().rstrip() for _ in range(N)]
        ids = [[[-1]*N for _ in range(N)] for _ in range(2)] # ids[dir][row][col]

        # 각 대각선 마다 아이디를 부여
        curr_l_id, curr_r_id = 0, 0
        for i in range(N):
            for j in range(N):
                curr_row, curr_col = i, j
                while curr_row < N and curr_col < N and board[curr_row][curr_col] == '.' and ids[0][curr_row][curr_col] == -1: # 대각선 오른쪽아래쪽으로 아이디 부여, 빈칸이고 아직 아이디가 없을경우에만
                    ids[0][curr_row][curr_col] = curr_l_id
                    curr_row += 1
                    curr_col += 1

                curr_l_id += 1
                curr_row, curr_col = i, j
                while curr_row < N and curr_col >= 0 and board[curr_row][curr_col] == '.' and ids[1][curr_row][curr_col] == -1: # 대각선 왼쪽아래쪽으로 아이디 부여, 빈칸이고 아직 아이디가 없을경우에만
                    ids[1][curr_row][curr_col] = curr_r_id
                    curr_row += 1
                    curr_col -= 1

                curr_r_id += 1
        
        # 왼쪽대각선 집합과 오른쪽 대각선 집합의 노드들을 잇는 간선을 만들어줌
        adj = [[False]*curr_r_id for _ in range(curr_l_id)]
        for i in range(N):
            for j in range(N):
                if board[i][j] == '.':
                    l_id, r_id = ids[0][i][j], ids[1][i][j]
                    adj[l_id][r_id] = True

        # 첫번째 왼쪽대각선에서 시작해 자리뺏으며 사랑의짝대기 계속 해나감
        l_matches, r_matches = [-1]*curr_l_id, [-1]*curr_r_id
        match_count = 0
        for l in range(curr_l_id):
            if dfs(l, curr_r_id, adj, l_matches, r_matches, set([])): # 증가경로가 있으면
                match_count += 1
        
        print(match_count)
