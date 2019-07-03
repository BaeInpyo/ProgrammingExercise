import sys


def quantization(arr, s):
    pass


if __name__ == '__main__':
    # freopen equivalent
    sys.stdin = open('input.txt', 'r')

    C = int(sys.stdin.readline().strip())
    answers = []

    for _ in range(C):
        N, S = map(int, sys.stdin.readline().strip().split())
        arr = map(int, sys.stdin.readline().strip().split())
        answers.append(quantization(arr, S))

    for a in range(answers):
        print(a)