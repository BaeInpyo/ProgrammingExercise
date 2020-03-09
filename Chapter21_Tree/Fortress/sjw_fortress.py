import sys
import os

# freopen equivalent
abs_dir = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(abs_dir, "input.txt"), "r")


class Node:
    def __init__(self, wall_info):
        self.wall_info = wall_info
        self.children = []

def solution(n, walls):
    def is_child(wall1, wall2):
        """
        return if wall2 can be parent of wall1
        """

        x1, y1, r1 = wall1
        x2, y2, r2 = wall2

        if r1 >= r2:
            return False

        dist = (x2-x1)**2 + (y2-y1)**2
        return dist <= (r2-r1)**2

    def build_tree(walls):
        """
        build tree and return root of tree
        """

        walls = [Node(wall_info) for wall_info in walls]
        walls.sort(key=lambda x: x.wall_info[2])    # sort by r ASC
        root = walls[-1]    # root node of tree

        # iterate except outer wall to build tree
        for idx in range(n - 1):
            node1 = walls[idx]
            for jdx in range(idx + 1, n):
                node2 = walls[jdx]

                # node2 is parent of node1
                if is_child(node1.wall_info, node2.wall_info):
                    node2.children.append(node1)
                    break

            else:
                # there is no parent of node1
                # this is unexpected error
                print("ERORORORO")

        return root

    def get_height(root):
        """
        1. return height of tree with given root
        2. renew longest path while finding height (global LONGEST)
        """
        heights = sorted([get_height(child) for child in root.children])

        # there is no child
        if not heights:
            return 0

        if len(heights) >= 2:
            # set longest path if there are more than 2 children
            global LONGEST
            LONGEST = max(LONGEST, 2 + heights[-1] + heights[-2])

        # height of root is max(heights of children) + 1
        return heights[-1] + 1

    root = build_tree(walls)
    height = get_height(root)
    print(max(height, LONGEST))
    return


if __name__ == "__main__":
    for _ in range(int(input())):
        LONGEST = 0
        N = int(input())
        walls = [0] * N
        for idx in range(N):
            xi, yi, ri = [int(x) for x in input().strip().split()]
            walls[idx] = (xi, yi, ri)

        solution(N, walls)