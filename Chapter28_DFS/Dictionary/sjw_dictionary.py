import os
import sys
from collections import defaultdict
import string

# freopen equivalent
abs_dir = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(abs_dir, "input.txt"), "r")

def dfs(graph, visited, curr, tpsort_lst):
    visited.add(curr)
    for _next in graph[curr]:
        if _next not in visited:
            dfs(graph, visited, _next, tpsort_lst)

    tpsort_lst.append(curr)
    return True

def solution(words):
    # key: alphabet, value: set of alplabet which has lower priority
    graph = defaultdict(lambda: set())

    # init graph
    for idx in range(len(words)-1):
        curr_word = words[idx]
        next_word = words[idx+1]
        jdx = 0
        while jdx < len(curr_word) and \
              jdx < len(next_word) and \
              curr_word[jdx] == next_word[jdx]:
            jdx += 1

        # curr_word[jdx] precedes next_word[jdx]
        if jdx < len(curr_word) and jdx < len(next_word):
            graph[curr_word[jdx]].add(next_word[jdx])

    visited = set()
    tpsort_lst = list()

    # do dfs
    for curr in graph:
        if curr not in visited:
            dfs(graph, visited, curr, tpsort_lst)

    tpsort_lst = tpsort_lst[::-1]   # reverse
    # check invalid hypothesis
    for curr in graph:
        curr_idx = tpsort_lst.index(curr)
        for _next in graph[curr]:
            next_idx = tpsort_lst.index(_next)
            if curr_idx > next_idx:
                sys.stdout.write("INVALID HYPOTHESIS\n")
                return

    for alpha in string.ascii_lowercase:
        if alpha not in tpsort_lst:
            tpsort_lst.append(alpha)

    sys.stdout.write("".join(tpsort_lst) + "\n")

def read():
    """ read input """
    return sys.stdin.readline().strip()

if __name__ == "__main__":
    for _ in range(int(read())):
        N = int(read())
        words = [None] * N
        for idx in range(N):
            words[idx] = read()

        solution(words)