import sys


def solution(n, d, p, A, Q):
    probability = [0] * n
    probability[p] = 1
    degree = [sum(row) for row in A]
    adj_list = []

    # initialize adjacent list
    for row in A:
        adj_list.append([x[0] for x in enumerate(row) if x[1] == 1])

    for _ in range(d):

        new_probability = [0] * n

        for curr in range(n):
            adj_nodes = adj_list[curr]

            for node in adj_nodes:
                new_probability[node] += probability[curr] / degree[curr]   # propagate probability

        probability = new_probability

    return [probability[x] for x in Q]


if __name__ == "__main__":
    # freopen equivalent
    sys.stdin = open("input.txt", "r")

    c = int(sys.stdin.readline().strip())
    answers = []
    for _ in range(c):
        n, d, p = [int(x) for x in sys.stdin.readline().strip().split()]
        A = []

        for __ in range(n):
            A.append([int(x) for x in sys.stdin.readline().strip().split()])

        t = int(sys.stdin.readline().strip())
        Q = [int(x) for x in sys.stdin.readline().strip().split()]

        answers.append(solution(n, d, p, A, Q))

    for a in answers:
        print(' '.join([ str(x) for x in a ]))
