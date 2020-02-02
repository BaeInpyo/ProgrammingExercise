import sys

def solution(N, K):
    soldiers = [i+1 for i in range(N)]
    idx = 0
    while len(soldiers) > 2:
        del soldiers[idx]
        idx = (idx + K-1) % len(soldiers) 
    return ' '.join([str(elt) for elt in soldiers])
    
if __name__ == '__main__':
    #sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline().rstrip())
    for _ in range(C):
        N, K = [int(x) for x in sys.stdin.readline().rstrip().split()]
        print(solution(N, K))


