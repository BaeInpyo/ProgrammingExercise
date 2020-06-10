import sys

def solution(adj_matrix, Ti, start, dest):

    return
    
def floyd(adj_matrix, Ti, V):
    W = [row[:] for row in adj_matrix]
    for k in range(V):
        worst_delay, worst_idx = Ti[k]
        for i in range(V):
            for j in range(V):
                # 추가메모리 없이 윈도우 1로
                adj_matrix[i][j] = min(adj_matrix[i][worst_idx] + adj_matrix[worst_idx][j], adj_matrix[i][j])
                W[i][j] = min(adj_matrix[i][worst_idx]+adj_matrix[worst_idx][j]+worst_delay, W[i][j])
    return W

if __name__ == '__main__':
    sys.stdin = open('input.in', 'r')
    V, E = [int(x) for x in sys.stdin.readline().rstrip().split()]
    Ti = sorted([(int(x), idx) for idx, x in enumerate(sys.stdin.readline().rstrip().split())])
    adj_matrix = [[float('inf')]*i + [0] + [float('inf')]*(V-i-1) for i in range(V)]
    for _ in range(E):
        Ai, Bi, Ci = [int(x) for x in sys.stdin.readline().rstrip().split()]
        adj_matrix[Ai-1][Bi-1] = Ci # 0-based로 변환
        adj_matrix[Bi-1][Ai-1] = Ci

    W = floyd(adj_matrix, Ti, V)

    C = int(sys.stdin.readline().rstrip())
    for _ in range(C):
        start, dest = [int(x) for x in sys.stdin.readline().rstrip().split()]
        print(W[start-1][dest-1])

