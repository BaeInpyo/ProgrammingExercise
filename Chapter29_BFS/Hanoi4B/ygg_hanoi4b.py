import sys
from collections import deque
visit_dict = {}
def is_equal(state1, state2):
    for i in range(4):
        if state1[i] != state2[i]:
            return False
    return True

def next_state_generator(state):
    top_discs = [column[-1] if column != '' else '' for column in state]
    for i in range(4):
        top_i = top_discs[i]
        if top_i == '':
            continue
        for j in range(4):
            if i == j:
                continue
            top_j = top_discs[j]
            if top_i < top_j or top_j == '':
                ret = state[:]
                ret[i] = ret[i][:-2]
                ret[j] += (' ' if top_j != '' else '') + top_i
                yield ret

def solution(start_state, end_state):
    bfs_queue = deque([(start_state, 0, True), (end_state, 0, False)]) # 처음과 끝 양방향에서 출발
    
    while bfs_queue:
        state, count, direction = bfs_queue.popleft()
        state_key = '|'.join(state)
        if visit_dict.get(state_key) != None: # 현 스태이트를 방문했던 기록이 있으면 
            visit_count, visit_dir = visit_dict[state_key]
            if visit_dir == direction: # 현재 방향과 같은 방향에서 방문했던 기록이면 패스
                continue
            else: # 반대쪽 방향에서 방문했던 기록이 있으면 여기가 솔루션 포인트
                return count + visit_count
            
        visit_dict[state_key] = (count, direction)
        
        for next_state in next_state_generator(state):
            bfs_queue.append((next_state, count+1, direction))
        
    
if __name__ == '__main__':
    sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline().strip())
    str_map = {str(i):str(i) for i in range(1, 10)}
    str_map['10'] = 'A'
    str_map['11'] = 'B'
    str_map['12'] = 'C'
    for _ in range(C):
        visit_dict = {}
        n = int(sys.stdin.readline().strip())
        start_state = [' '.join([str_map[i] for i in sys.stdin.readline()[2:].strip().split()]) for _ in range(4)]
        end_state = [' '.join([str_map[i] for i in sys.stdin.readline()[2:].strip().split()]) for _ in range(4)]
       # end_state = ['','','',' '.join([str_map[str(i)] for i in range(1,n+1)][::-1])]
        print(solution(start_state, end_state))
