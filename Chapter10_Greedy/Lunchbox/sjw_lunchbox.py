import sys
import os

'''
Since total time for warming up all lunch boxes is same,
solutio is only dependent to eating time
'''


def solution(n, ms, es):
    zipped = list(zip(ms, es))
    zipped.sort(key=lambda x: x[1], reverse=True)    # order by eating time desc
    ms = [x[0] for x in zipped]
    es = [x[1] for x in zipped]
    accumulated_ms = []
    for i in range(n):
        if i == 0:
            accumulated_ms.append(ms[i])
        else:
            accumulated_ms.append(accumulated_ms[-1] + ms[i])

    candidates = [accumulated_ms[i] + es[i] for i in range(n)]
    return max(candidates)


if __name__ == '__main__':
    # freopen equivalent
    abs_path = os.path.abspath(os.path.dirname(__file__))
    sys.stdin = open(os.path.join(abs_path, 'input.txt'), 'r')

    C = int(sys.stdin.readline().strip())
    answers = []
    for _ in range(C):
        n = int(sys.stdin.readline().strip())
        ms = [int(x) for x in sys.stdin.readline().strip().split()]
        es = [int(x) for x in sys.stdin.readline().strip().split()]
        answers.append(solution(n, ms, es))

    for a in answers:
        print(a)