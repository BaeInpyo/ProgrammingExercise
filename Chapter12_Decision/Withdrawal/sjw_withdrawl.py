import sys, os

# freopen equivalent
abs_path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(abs_path, "input.txt"), "r")


def solution(n, k, r, c):
    sum_r, sum_c = 0, 0
    selected_index = set()
    for _ in range(k):
        # find (ri,ci) that makes sum_r / sum_c minumum
        min_sum_r, min_sum_c, min_idx = sum_r, sum_c, -1
        for idx in range(n):
            if idx in selected_index:
                continue

            if min_idx == -1:
                min_sum_r += r[idx]
                min_sum_c += c[idx]
                min_idx = idx

            else:
                # the smaller one found
                if (sum_r + r[idx]) / (sum_c + c[idx]) < min_sum_r / min_sum_c:
                    min_sum_r = sum_r + r[idx]
                    min_sum_c = sum_c + c[idx]
                    min_idx = idx

        sum_r = min_sum_r
        sum_c = min_sum_c
        selected_index.add(min_idx)

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