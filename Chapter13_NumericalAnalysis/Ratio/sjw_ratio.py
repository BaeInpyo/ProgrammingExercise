import sys, os

abs_path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(abs_path, "input.txt"), "r")


def solution(n, m):
    # return if x consecutive wins can raise z more than 1
    def is_possible(x):
        new_z = ((m + x) * 100) // (n + x)
        return (new_z >= z + 1)

    z = (m * 100) // n
    start, end = 0, 2000000000
    for _ in range(32):
        mid = (start + end) // 2
        if is_possible(mid):
            end = mid
        else:
            start = mid

    answer = end if is_possible(end) else -1
    return str(answer)


if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())
    answers = []
    for _ in range(T):
        N, M = [int(x) for x in sys.stdin.readline().strip().split()]
        answers.append(solution(N, M))

    answer = "\n".join(answers)
    sys.stdout.write(answer)
    sys.stdout.flush()