import sys
import os
from collections import defaultdict

# freopen equivalent
abs_dir = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(abs_dir, "input.txt"), "r")

class DisjointSet:
    def __init__(self, n):
        """
        n is total number of elements
        self.arr[x] = parent of x
        """
        self.arr = [{ "rank": 1, "parent": x, "side": None} for x in range(n)]
        self.group_idx = 1

    def union(self, a, b):
        """
        Union a and b
        """
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return

        rank_a = self.arr[a]["rank"]
        rank_b = self.arr[b]["rank"]
        if rank_b > rank_a:
            a, b = b, a

        # now a has bigger rank
        self.arr[b]["parent"] = a

        # set rank
        if rank_a == rank_b:
            self.arr[a]["rank"] += 1

        return

    def find(self, a):
        """ return root of a"""
        if self.arr[a]["parent"] == a:
            return a

        # apply path compression
        parent = self.arr[a]["parent"]
        self.arr[a]["parent"] = self.find(parent)
        return self.arr[a]["parent"]

    def ack(self, a, b):
        """ return True if ACK is possible else return False """
        root_a, root_b = self.find(a), self.find(b)

        # if either a or b has no side, they can be merged
        if self.arr[root_a]["side"] is None or self.arr[root_b]["side"] is None:
            self.union(a, b)
            return True

        # a and b has same side
        if self.arr[root_a]["side"] == self.arr[root_b]["side"]:
            return True

        # a and b has different side, i.e, contradict
        return False

    def dis(self, a, b):
        """ return True is DIS is possible else return False """
        root_a, root_b = self.find(a), self.find(b)
        if root_a == root_b:
            return False

        side_a = self.arr[root_a]["side"]
        side_b = self.arr[root_b]["side"]
        if side_a is None and side_b is None:
            # set arbitrary side
            self.arr[root_a]["side"] = self.group_idx
            self.arr[root_b]["side"] = -self.group_idx
            self.group_idx += 1
            return True
        if side_a is None:
            # set counter side
            self.arr[root_a]["side"] = -side_b
            return True
        if side_b is None:
            # set counter side
            self.arr[root_b]["side"] = -side_a
            return True
        # now, both a and b has side
        if side_a == side_b:
            # contradict
            return False

        # both a and b has side which is different each other
        return True

    def get_max_party_size(self):
        count_dict = defaultdict(int) # key: side, value: count
        for num in range(len(self.arr)):
            root = self.find(num)
            side = self.arr[root]["side"]
            print("num: {}, root: {}, side: {}".format(num, root, side))
            count_dict[side] += 1

        # print(count_dict)
        max_party_size = 0
        for key, value in count_dict.items():
            if key is not None:
                side1 = count_dict.get(key, 0)
                side2 = count_dict.get(-key, 0)
                max_party_size += max(side1, side2)

        max_party_size //= 2
        max_party_size += count_dict.get(None, 0)
        return max_party_size

def input():
    return sys.stdin.readline().strip()

if __name__ == "__main__":
    for _ in range(int(input())):
        N, M = [int(x) for x in input().split()]
        ds = DisjointSet(N)
        has_contradict = False
        for comment_num in range(1, M+1):
            if has_contradict:
                input()
                continue

            command, a, b = input().split()
            a, b = int(a), int(b)
            if command == "ACK":
                result = ds.ack(a, b)
            elif command == "DIS":
                result = ds.dis(a, b)

            if result is False:
                sys.stdout.write("CONTRADICTION AT {}\n".format(comment_num))
                has_contradict = True

        if not has_contradict:
            party_size = ds.get_max_party_size()
            sys.stdout.write("MAX PARTY SIZE IS {}\n".format(party_size))

