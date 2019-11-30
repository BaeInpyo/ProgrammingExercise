import sys

def initProbs(probs, N):
    for l in range(4):
        for i in range(N):
            probs[l][i] = 0

def solution(K, L, T, N):

    bf_1min_probs = [[0]*N for _ in range(4)]
    currProbs = [[0]*N for _ in range(4)]

    bf_1min_probs[L[0]-1][0] = 1

    for k in range(1,K+1):
        for i in range(N):
            for l in range(0,L[i]):
                if l == L[i]-1:
                    remain_1min_prob = bf_1min_probs[0]
                    tempResult = 0
                    for bf_i in range(N):
                        tempResult += remain_1min_prob[bf_i] * T[bf_i][i]
                    currProbs[l][i] = tempResult
                else:
                    currProbs[l][i] = bf_1min_probs[(l+1)][i]
        temp = bf_1min_probs
        bf_1min_probs = currProbs
        currProbs = temp

    return bf_1min_probs
    
if __name__ == '__main__':
    #sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline().rstrip())
    for _ in range(C):
        N, K, M = list(map(int,sys.stdin.readline().rstrip().split()))
        L = list(map(int,sys.stdin.readline().rstrip().split()))
        T = [list(map(float,sys.stdin.readline().rstrip().split())) for _ in range(N)]
        favoriteSongs = list(map(int,sys.stdin.readline().rstrip().split()))
        probs = solution(K, L, T, N)
        result = []
        for i in range(N):
            temp = 0.0
            for l in range(4):
                temp += probs[l][i]
            result.append(temp)
        print(list(map(lambda x: result[x], favoriteSongs)))


