import os
import sys
from itertools import permutations
from collections import deque

# freopen equivalent
abs_dir = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(abs_dir, "input.txt"), "r")


# do bfs search to find dst_state from src_state
def solution(src_state, dst_state):
    visited = dict()
    def get_next_state(src_state):
        """ return adjacent state """
        result = []
        for (col1, col2) in permutations(range(4), 2):
            if not src_state[col1]:
                continue

            # if col2 is empty or top disk in col2 is bigger than col1
            # then we can move disk from col1 to col2
            if not src_state[col2] or src_state[col1][-1] < src_state[col2][-1]:
                new_state = [list(row) for row in src_state]    # copy src_state
                new_state[col2].append(new_state[col1].pop())   # move col1 to col2
                new_state = tuple(tuple(x) for x in new_state)  # convert to tuple
                result.append(new_state)

        return result

    # do bfs
    src_state = tuple(tuple(x) for x in src_state)  # convert to tuple
    dst_state = tuple(tuple(x) for x in dst_state)  # convert to tuple
    queue = deque([(src_state, 0)])   # (state, distance)
    while queue:
        curr_state, curr_distance = queue.popleft()
        next_state = get_next_state(curr_state)
        for state in next_state:
            if state == dst_state:
                print(curr_distance + 1)
                return

            state_tuple = tuple(tuple(x) for x in state)
            if state_tuple not in visited:
                visited[state_tuple] = True
                queue.append([state, curr_distance+1])

    print("no answer")
    return


def readline():
    return sys.stdin.readline()

if __name__ == "__main__":
    for _ in range(int(readline())):
        n = int(readline())
        src_state = [[] for _ in range(4)]
        dst_state = [[] for _ in range(4)]
        for idx in range(4):
            # store disk only
            src_state[idx] = [int(x) for x in readline().split()][1:]
        for idx in range(4):
            # sotre disk only
            dst_state[idx] = [int(x) for x in readline().split()][1:]

        solution(src_state, dst_state)