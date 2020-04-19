# cycle 고려하기

import os
import sys


# freopen equivalent
abs_dir = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(abs_dir, "input.txt"), "r")


def print_graph(graph):
    print("graph below~")
    for key, value in graph.items():
        print("key:", key, "value:", value)

def build_graph(words):
    """
    return tuple (indegrees, outdegrees, graph)
    indegrees => key: alphabet, value: indegree
    outdegrees => key: alphabet, value: outdegree
    graph => key: alphabet, value: set of words stating with alphabet
    """
    indegrees, outdegrees, graph = dict(), dict(), dict()
    for word in words:
        first, last = word[0], word[-1]
        # set graph
        if first in graph:
            graph[first].add(word)
        else:
            graph[first] = { word } # set
        if last in graph:
            pass
        else:
            graph[last] = set()
        # set indegrees
        if first in indegrees:
            pass
        else:
            indegrees[first] = 0
        if last in indegrees:
            indegrees[last] += 1
        else:
            indegrees[last] = 1
        # set outdegrees
        if first in outdegrees:
            outdegrees[first] += 1
        else:
            outdegrees[first] = 1
        if last in outdegrees:
            pass
        else:
            outdegrees[last] = 0

    return indegrees, outdegrees, graph

def find_start_point(indegrees, outdegrees, graph):
    """
    We can think of 3 cases
    1. If Euiler path exists, return any point
    2. If Euiler trail exists, return start point
    3. If not 1 and not 2, return -1
    """
    all_nodes = list(graph.keys())
    positive_one, negative_one = 0, 0
    start_point = None
    for alphabet in all_nodes:
        diff = outdegrees[alphabet] - indegrees[alphabet]
        if diff == 0:
            continue
        elif diff == 1:
            positive_one += 1
            start_point = alphabet
        elif diff == -1:
            negative_one += 1
        else:
            return -1   # we only allow 0, +1, -1

    if (positive_one, negative_one) not in [(0, 0), (1, 1)]:
        return -1

    # if start_point not set, it means we have Euiler path thus we can start
    # from any node
    start_point = all_nodes[0] if start_point is None else start_point
    return start_point

def get_euiler(graph, start, euiler):
    """ return euiler path/trail from start """
    words = graph[start]
    while len(words):
        word = words.pop()  # pick any next node
        end = word[-1]
        get_euiler(graph, end, euiler)  # find from end
        euiler.insert(0, word) # add to path
    return euiler   # return path until now

def solution(words):
    indegrees, outdegrees, graph = build_graph(words)
    start_point = find_start_point(indegrees, outdegrees, graph)
    if start_point == -1:
        sys.stdout.write("IMPOSSIBLE\n")
        return

    # now we have either euiler path or trail
    path = get_euiler(graph, start_point, [])
    answer = " ".join(path) + "\n"
    sys.stdout.write(answer)
    return


def read():
    return sys.stdin.readline().strip()

if __name__ == "__main__":
    for _ in range(int(read())):
        N = int(read())
        words = [None] * N
        for idx in range(N):
            words[idx] = read()

        solution(words)