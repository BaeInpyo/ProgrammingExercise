import sys

def solution(N, move):
    A = list(range(1,N+1))
    result = [0]*N
    for idx in range(N-1, -1, -1):
        result[idx] = A[-(1+move[idx])]
        del A[-(1+move[idx])]
    
    return map(str, result)
    
    
if __name__ == '__main__':
    sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline().rstrip())
    for _ in range(C):
        N = int(sys.stdin.readline().rstrip())
        move = [int(x) for x in sys.stdin.readline().rstrip().split()]
        print(' '.join(solution(N, move)))


