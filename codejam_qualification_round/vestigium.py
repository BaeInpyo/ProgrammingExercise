def solution(case_num, n, matrix):
    trace = 0
    repeated_rows = 0
    repeated_cols = 0
    sum_one_to_n = (n * (n+1)) // 2

    # calculate trace
    for idx in range(n):
        trace += matrix[idx][idx]

    for idx in range(n):
        row = matrix[idx]
        col = [_row[idx] for _row in matrix]
        if len(set(row)) < n:
            repeated_rows += 1
        if len(set(col)) < n:
            repeated_cols += 1

    print("Case #{}: {} {} {}".format(case_num, trace, repeated_rows, repeated_cols))

if __name__ == "__main__":
    T = int(input())
    for case_number in range(1, T+1):
        N = int(input())
        matrix = [0] * N
        for idx in range(N):
            row = [int(x) for x in input().split()]
            matrix[idx] = row

        solution(case_number, N, matrix)