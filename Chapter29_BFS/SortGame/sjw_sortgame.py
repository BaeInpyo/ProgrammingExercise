"""
중복이 없는 길이가 n인 string을 중간 순서를 바꾸어 만들 수 있는 모든 string의
갯수는 n!이다. 이 n!개의 string을 node로 생각하고 중간의 순서를 뒤집는 것을 edge
로 생각하여 임의의 시작점 "01234567"로부터 모든 경우(n!)의 순서 뒤집기 횟수를
bfs search를 통하여 구하면 (DP에서의 cache를 채우는것과 유사함) 주어진 입력을
sorted string으로 바꾸는데에 필요한 뒤집기 횟수를 바로 알 수 있다.
"""

import sys
import os
from collections import deque

# # freopen equivalent
# abs_dir = os.path.dirname(os.path.abspath(__file__))
# sys.stdin = open(os.path.join(abs_dir, "input.txt"), "r")

def solution(n, sequence):
    idx = [x for x in range(n)]
    idx.sort(key=lambda x: sequence[x])
    idx.extend(range(n, 8))
    answer = cache["".join([str(x) for x in idx])]
    sys.stdout.write(str(answer) + "\n")

def readline():
    return sys.stdin.readline()

if __name__ == "__main__":

    # init cache
    cache = dict()  # key : sequence, value: distnace
    SORTED = "01234567"

    # do bfs to fill cache
    cache[SORTED] = 0
    queue = deque([(SORTED, 0)])    # start from sorted sequence
    while queue:
        curr_sequence, distance = queue.popleft()
        for start in range(7):
            for end in range(start+2, 9):
                next_sequence = "".join([
                    curr_sequence[:start], curr_sequence[start:end][::-1],
                    curr_sequence[end:]])
                if next_sequence not in cache:
                    cache[next_sequence] = distance + 1
                    queue.append((next_sequence, distance+1))

    # read input
    for _ in range(int(readline())):
        N = int(readline())
        sequence = [int(x) for x in readline().split()]
        solution(N, sequence)
