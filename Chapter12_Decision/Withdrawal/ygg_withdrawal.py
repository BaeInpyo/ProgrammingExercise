import sys

def check(RCs, K, x):
    return sum(sorted([x*c-r for r, c in RCs], reverse=True)[:K]) >= 0
    
def solution(RCs, K, iter):
    fr, to = 0, 1
    for _ in range(iter):
        mid = (to + fr)/2
        if check(RCs, K, mid):
            to = mid
        else:
            fr = mid 
    return mid

if __name__ == '__main__':
    #sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline().rstrip())
    for _ in range(C):
        N, K = list(map(int,sys.stdin.readline().rstrip().split()))
        RCs = list(map(int,sys.stdin.readline().rstrip().split()))
        RCs = [(RCs[idx], RCs[idx+1]) for idx in range(0, len(RCs), 2)]
        
        print(solution(RCs, K, 100))
