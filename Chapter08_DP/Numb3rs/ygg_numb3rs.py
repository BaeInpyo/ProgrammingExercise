import sys
E = []


def matrixMul(A, B):
    result = []
    for r in range(len(A)):
        rowResult = []
        for c in range(len(B[0])):
            elt = 0
            for i in range(len(B)):
                elt += A[r][i]*B[i][c]
            rowResult.append(elt)
        result.append(rowResult)
    return result

def graphToProbMatrix(graph):
    result = [[0]*len(graph) for _ in range(len(graph))]
    for c, row in enumerate(graph):
        p = 1/sum(row)
        for r, elt in enumerate(row):
            if elt == 1:
                result[r][c] = p
    return result

"""
통과버전
NxN 매트릭스의 파워계산이 아닌 NxN * Nx1 계산의 반복
def solution(d, pVector, M):
    result = pVector

    for _ in range(d):
        result = matrixMul(M, result)

    return result
"""

def getNPower(n, M):
    if n == 0:
        return E
    elif n == 1:
        return M

    if n%2 == 0:
        halfM = getNPower(int(n/2), M)
        return matrixMul(halfM, halfM)
    else:
        halfM = getNPower(int(n/2), M)
        return matrixMul(matrixMul(halfM, halfM), M)

# 시간초과버전
# NxN 매트릭스의 파워를 구한 후 결과를 계산
def solution(d, pVector, M):
    MPowerD = getNPower(d, M)
    return matrixMul(MPowerD, pVector)

if __name__ == '__main__':
    sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline())
    for _ in range(C):
        n, d, p = list(map(int, sys.stdin.readline().rstrip().split()))
        graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
        M = graphToProbMatrix(graph)
        t = int(sys.stdin.readline())
        qList = list(map(int, sys.stdin.readline().rstrip().split()))
        pVector = [[0] for _ in range(n)]
        pVector[p][0] = 1
        E = [[1 if j==i else 0 for j in range(len(M))] for i in range(len(M))]
        result = solution(d, pVector, M)
        print(' '.join(list(map(lambda x: str(result[x][0]), qList))))
