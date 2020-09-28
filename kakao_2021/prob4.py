def solution(n, s, a, b, fares):
    """
    1. Find n x n shortest path
    2. For all k in range [1, n], try s -> k -> (a, b)
    """

    table = [[float("inf")]*n for _ in range(n)]
    for (c, d, f) in fares:
        table[c-1][d-1] = f
        table[d-1][c-1] = f

    for idx in range(n):
        table[idx][idx] = 0

    # do floyd to find all shortest paths
    for kdx in range(n):
        for idx in range(n):
            for jdx in range(n):
                table[idx][jdx] = min(table[idx][jdx], table[idx][kdx] + table[kdx][jdx])
    
#    for row in table:
#        print(row)
    
    answer = table[s-1][a-1] + table[s-1][b-1]
 #   print("seperate:", answer)
    for idx in range(n):
 #       print("idx 경유:", idx, table[s-1][idx] + table[idx][a-1] + table[idx][b-1])
        answer = min(answer, table[s-1][idx] + table[idx][a-1] + table[idx][b-1])

  #  print("answer:", answer)
    return answer
        
solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])