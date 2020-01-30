import sys
from itertools import combinations
envDict = {}
masking = [] # i 이면 안들은거, -1이면 들은거


def solution(M, R, C, K, L, semester, passSemester):
    # 학기, 마스킹 리스트로 dp (최소학기수를 기억)
    key = (','.join([str(i) for i in masking]), semester, passSemester)
    if envDict.get(key, -1) != -1:
        return envDict[key]

    if K == 0:
        envDict[key] = semester-passSemester
        return semester-passSemester
    if semester >= M:
        envDict[key] = 99
        return 99

    candidates = []
    for i in masking:
        # 1.해당과목을 이미 들었으면 후보가 아님
        if i == -1: 
            continue

        # 2.선수과목중 하나라도 안들은게 있으면 후보가 아님
        for r in R[i]:
            if masking[r] != -1: 
                break # 하나라도 안들은게 있으면
        else: # 위에서 break로 안 나오면 여기로감 
            # 3.해당과목이 현 학기에 안열리면 후보가 아님
            if not (i in C[semester]):
                continue
            
            # 셋다 아니라면 후보
            candidates.append(i)
        
    result = 99
    # 후보를 가지고 L개짜리 조합을 만듦
    thisL = min(len(candidates), L)
    if thisL == 0: # 후보가 하나도 없으면 안듣고 다음학기로
        result = solution(M, R, C, K, L, semester+1, passSemester+1)
        envDict[key] = result
        return result

    # 후보가 있으면
    for comb in combinations(candidates, thisL):
        # 마스킹
        for i in comb:
            masking[i] = -1
        # L개 듣는 재귀
        result = min(result, solution(M, R, C, K-thisL, L, semester+1, passSemester))
        # 언마스킹
        for i in comb:
            masking[i] = i
        # 0개 듣는 재귀
        result = min(result, solution(M, R, C, K, L, semester+1, passSemester+1))

    envDict[key] = result
    return result
            
    
    
if __name__ == '__main__':
    case = int(sys.stdin.readline().rstrip())
    for _ in range(case):
        envDict = {}
        N, K, M, L = [int(elt) for elt in sys.stdin.readline().rstrip().split()]
        masking = [i for i in range(N)]
        R = []
        for _ in range(N):
            Ri = [int(elt) for elt in sys.stdin.readline().rstrip().split()][1:]
            R.append(Ri)
        C = []
        for _ in range(M):
            Ci = [int(elt) for elt in sys.stdin.readline().rstrip().split()][1:]
            C.append(Ci)

        result = solution(M, R, C, K, L, 0, 0)
        print('IMPOSSIBLE' if result == 99 else result)

