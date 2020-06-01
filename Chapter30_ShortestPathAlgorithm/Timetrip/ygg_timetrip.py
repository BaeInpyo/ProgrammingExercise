import sys

def calc_reachable(V, adj_matrix):
    # 인접행렬 바로 이용
    for k in range(V):
        for i in range(V):
            if adj_matrix[i][k]: # 최적화
                for j in range(V):
                    adj_matrix[i][j] = adj_matrix[i][j] or (adj_matrix[i][k] and adj_matrix[k][j])

    return adj_matrix

def solution(V, edges, adj_matrix):
    upper_dict = {i: float('inf') for i in range(V)}
    lower_dict = {i: -float('inf') for i in range(V)}
    upper_dict[0] = 0
    lower_dict[0] = 0

    reachable = calc_reachable(V, adj_matrix)

    updated = True
    for _ in range(V-1):
        if not updated: # relax가 안일어났으면 바로 통과
            break
        updated = False
        for a, b, d in edges:
            if upper_dict[b] > upper_dict[a] + d:
                upper_dict[b] = upper_dict[a] + d
                updated = True
            if lower_dict[b] < lower_dict[a] + d:
                lower_dict[b] = lower_dict[a] + d
                updated = True


    # 사이클 체크 (updated가 True 일때만)
    if updated:
        for a, b, d in edges:
            if type(upper_dict[1]) != str and upper_dict[b] > upper_dict[a] + d: # V번째에 relax가 가능하면 (음수) 사이클
                if reachable[0][a] and reachable[a][1]: # 지구에서 사이클을 거쳐서 안드로메다로 가는 경로가 있으면 infinity
                    upper_dict[1] = "INFINITY"
            if type(lower_dict[1]) != str and lower_dict[b] < lower_dict[a] + d: # V번째에 relax가 가능하면 (양수) 사이클
                if reachable[0][a] and reachable[a][1]: # 지구에서 사이클을 거쳐서 안드로메다로 가는 경로가 있으면 infinity
                    lower_dict[1] = "INFINITY"

    if upper_dict[1] == float('inf') or lower_dict[1] == -float('inf'):
        return "UNREACHABLE"

    return ' '.join([str(upper_dict[1]), str(lower_dict[1])])
    
if __name__ == '__main__':
    sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline().rstrip())
    for _ in range(C):
        V, W = [int(x) for x in sys.stdin.readline().rstrip().split()]
        adj_matrix = [[i==j for i in range(V)] for j in range(V)]
        edges = []
        for _ in range(W):
            a, b, d = [int(x) for x in sys.stdin.readline().rstrip().split()]
            edges.append((a,b,d))
            adj_matrix[a][b] = True
            adj_matrix[b][a] = True
        print(solution(V, edges, adj_matrix))
