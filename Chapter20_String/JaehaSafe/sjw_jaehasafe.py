import sys
import os


abs_dir = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(abs_dir, "input.txt"), "r")


def solution(n, states):

    answer = 0
    for idx in range(n):
        src = states[idx]
        dst = states[idx + 1]

        if idx % 2 == 0:
            # clock wise
            string = dst * 2
            pattern = src
        else:
            # counter-clock wise
            string = src * 2
            pattern = dst

        for jdx in range(1, len(string)):
            if string[jdx:jdx+len(pattern)] == pattern:
                answer += jdx
                break

    print(answer)
    return


if __name__ == "__main__":
	C = int(input())
	for _ in range(C):
		N = int(input())
		states = [None] * (N + 1)
		for idx in range(N + 1):
			state = input()
			states[idx] = state

		solution(N, states)
