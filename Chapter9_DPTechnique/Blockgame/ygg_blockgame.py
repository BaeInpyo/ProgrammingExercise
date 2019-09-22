import sys

env_dict = {}
CASES = [[(0,0),(0,1)], [(0,0),(1,0)], [(0,0),(0,1),(1,0)], [(0,0),(0,1),(1,1)], [(0,0),(1,0),(1,1)], [(0,0),(1,0),(1,-1)]]

def solution(board):
    key = (''.join(map(''.join,board)))

    if env_dict.get(key, -1) != -1:
        return env_dict[key]

    for i in range(25):
        r, c = int(i/5)+1, i%5+1 # 테두리 1 더하기
        if board[r][c] == '#':
            continue
        for case in CASES:
            if sum(map(lambda x: board[r+x[0]][c+x[1]] == '#', case)) == 0: # 놓을수 있으면
                for case_r, case_c in case: # 블럭을 놓음
                    board[r+case_r][c+case_c] = '#'
                if not solution(board): # 상대가 항상 진다면
                    for case_r, case_c in case: # 블럭을 다시 지움(다음 인덱스 재귀콜 위해)
                        board[r+case_r][c+case_c] = '.'
                    env_dict[key] = True
                    return True
                else:
                    for case_r, case_c in case: # 블럭을 다시 지움(다음 인덱스 재귀콜 위해)
                        board[r+case_r][c+case_c] = '.'

    env_dict[key] = False
    return False
            
    
    
if __name__ == '__main__':
    sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline().rstrip())
    for _ in range(C):
        env_dict = {}
        board = [list("#######")]+[list('#'+sys.stdin.readline().rstrip()+'#') for _ in range(5)]+[list("#######")]
        result = solution(board)
        # print(env_dict)
        if result:
            print('WINNING')
        else:
            print('LOSING')
