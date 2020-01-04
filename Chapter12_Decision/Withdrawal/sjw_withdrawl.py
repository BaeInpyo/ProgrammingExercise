import sys, os

# freopen equivalent
abs_path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(abs_path, "input.txt"), "r")


def solution(n, k, r, c):
    sum_r, sum_c = 0, 0
    remained = set(zip(r, c))
    for _ in range(k):
        # find (ri,ci) that makes sum_r / sum_c minumum
        candidates = [(sum_r + ri, sum_c + ci) for (ri, ci) in remained]
        min_pair = min(candidates, key=lambda x: x[0] / x[1])
        ri = min_pair[0] - sum_r
        ci = min_pair[1] - sum_c
        remained.remove((ri, ci))
        sum_r += ri
        sum_c += ci

    answer = round(sum_r / sum_c, 10)
    return answer


if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())
    answers = []
    for _ in range(T):
        n, k = [int(x) for x in sys.stdin.readline().strip().split()]
        line = [int(x) for x in sys.stdin.readline().strip().split()]
        r = [x for (i, x) in enumerate(line) if i % 2 == 0]
        c = [x for (i, x) in enumerate(line) if i % 2 == 1]
        answers.append(solution(n, k, r, c))

    for answer in answers:
        print(answer)