import sys, os

# freopen equivalent
abs_path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(abs_path, "input.txt"), "r")


def solution_nsquare(n, k, r, c):
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


def solution_nlogn(n, k, r, c):
    # return if rank is possible with given (n, k, r, c)
    def is_possible(rank):
        candidates = [rank * ci - ri for (ci, ri) in zip(c, r)]
        candidates.sort(reverse=True)
        if sum(candidates[:k]) >= 0:
            return True
        else:
            return False

    start, end = 0, 1

    # 2^35 > 10^10, TODO: whiy 34 fails?
    for _ in range(35):
        mid = (start + end) / 2
        if is_possible(mid):
            end = mid
        else:
            start = mid

    return round(end, 10)


if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())
    answers = []
    for _ in range(T):
        n, k = [int(x) for x in sys.stdin.readline().strip().split()]
        line = [int(x) for x in sys.stdin.readline().strip().split()]
        r = [x for (i, x) in enumerate(line) if i % 2 == 0]
        c = [x for (i, x) in enumerate(line) if i % 2 == 1]
        answers.append(solution_nlogn(n, k, r, c))

    answers = [str(x) for x in answers]
    answer = "\n".join(answers)
    sys.stdout.write(answer)
    sys.stdout.flush()