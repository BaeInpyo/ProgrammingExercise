import sys
import os
from collections import deque

# freopen equivalent
abs_dir = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(abs_dir, "input.txt"), "r")




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
        
    # with open("temp.json", "w") as f:
    #     import json
    #     json.dump(cache, f, sort_keys=True, indent=4)

    # read input
    for _ in range(int(readline())):
        N = int(readline())
        sequence = [int(x) for x in readline().split()]
        solution(N, sequence)
