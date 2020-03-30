import sys
import os
import math
import json
from collections import deque
from collections import defaultdict


max_height = 17 # log2(100000) = 16.xxx

# initialize parent, depth
def init(n, tree, parent, depth):
    root = 1
    queue = deque([root])  # start with root
    visited = defaultdict(lambda x: False)
    depth[root] = 0    # depth of root is 0

    while queue:
        curr = queue.pop()
        visited[curr] = True
        for dst in tree[curr]:
            if not visited.get(dst):
                parent[dst][0] = curr
                depth[dst] = depth[curr] + 1
                queue.appendleft(dst)

    # add 2^k parent
    for k in range(max_height + 1):
        # for node, _depth in sorted(depth.items(), reverse=True):
        for node, _depth in depth.items():
            if node not in parent \
                or k not in parent[node] \
                or parent[node][k] not in parent \
                or k not in parent[parent[node][k]]:
                continue
            else:
                parent[node][k + 1] = parent[parent[node][k]][k]
            # try:
            #     parent[node][k + 1] = parent[parent[node][k]][k]
                
            # except KeyError:
            #     pass



def solution(n, tree, test_cases):
    parent = defaultdict(dict)  # key: node, value: dict whose key is n and value is parent of 2^n
    depth = {}
    init(n, tree, parent, depth)
    answers = [None] * len(test_cases)

    # print(json.dumps(tree, indent=4, sort_keys=True))
    # print(json.dumps(parent, indent=4, sort_keys=True))
    # print(json.dumps(depth, indent=4, sort_keys=True))

    for idx, (node1, node2) in enumerate(test_cases):
        node1_origin = node1
        node2_origin = node2
        if depth[node1] != depth[node2]:
            x = node1 if depth[node1] > depth[node2] else node2
            y = node2 if depth[node1] > depth[node2] else node1
            # x is deeper than y now
            while depth[x] > depth[y]:
                diff = depth[x] - depth[y]
                k = int(math.log(diff, 2))  # log2(diff)
                x = parent[x][k]

            # now x and y has same depth
            node1, node2 = x, y

        if node1 == node2:
            lca = node1
            # print("lca:", lca, node1_origin, node2_origin)
            distance = depth[node1_origin] + depth[node2_origin] - 2 * depth[lca]
            # print("distance:", distance)
            answers[idx] = distance
            continue
        else:

            # now node1 and node2 has same depth
            for k in reversed(range(max_height + 1)):
                if k in parent[node1] and k in parent[node2] and parent[node1][k] != parent[node2][k]:
                    node1 = parent[node1][k]
                    node2 = parent[node2][k]

            lca = parent[node1][0]
            # print("lca:", lca, node1_origin, node2_origin)
            distance = depth[node1_origin] + depth[node2_origin] - 2 * depth[lca]
            # print("distance:", distance)
            answers[idx] = distance

    sys.stdout.write("\n".join([str(x) for x in answers]))

if __name__ == '__main__':
    # read input
    for _ in range(int(input())):
        N, Q = [int(x) for x in sys.stdin.readline().strip().split()]
        nums = [int(x) for x in sys.stdin.readline().strip().split()]
        tree = defaultdict(list)
        for idx, num in enumerate(nums):
            child = idx + 2
            parent = num + 1
            tree[child].append(parent)
            tree[parent].append(child)

        test_cases = [None] * Q
        for idx in range(Q):
            a, b = [int(x) for x in sys.stdin.readline().strip().split()]
            test_cases[idx] = (a+1, b+1)

        # tree = defaultdict(list)
        # for _ in range(N-1):
        #     src, dst = [int(x) for x in sys.stdin.readline().strip().split()]
        #     tree[src].append(dst)
        #     tree[dst].append(src)
        # M = int(sys.stdin.readline().strip())
        # test_cases = []
        # for _ in range(M):
        #     node1, node2 = [int(x) for x in sys.stdin.readline().strip().split()]
        #     test_cases.append((node1, node2))

        solution(N, tree, test_cases)
