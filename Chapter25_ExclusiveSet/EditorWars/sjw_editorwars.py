import os
import sys

# freopen equivalent
abs_dir = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(abs_dir, "input.txt"), "r")

class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = list(range(n))
        self.rank = [0] * n
        self.enemy = [-1] * n
        self.size = [1] * n

    def find(self, u):
        if self.parent[u] == u:
            return u
        root = self.find(self.parent[u])
        self.parent[u] = root
        return root

    def union(self, u, v):
        if u == -1 or v == -1:
            return max(u, v)
        u, v = self.find(u), self.find(v)
        if u == v:
            return u
        if self.rank[u] > self.rank[v]:
            u, v = v, u
        if self.rank[u] == self.rank[v]:
            self.rank[v] += 1
        self.parent[u] = v
        self.size[v] += self.size[u]
        return v

    def dis(self, u, v):
        u, v = self.find(u), self.find(v)
        if u == v:
            return False
        a = self.union(u, self.enemy[v])
        b = self.union(v, self.enemy[u])
        self.enemy[a] = b
        self.enemy[b] = a
        return True

    def ack(self, u, v):
        u, v = self.find(u), self.find(v)
        if self.enemy[u] == v:
            return False
        a = self.union(u, v)
        b = self.union(self.enemy[u], self.enemy[v])
        self.enemy[a] = b
        if b != -1:
            self.enemy[b] = a
        return True

    def maxParty(self):
        # self.debug_print()
        ret = 0
        for node in range(self.n):
            if self.parent[node] == node:
                enemy = self.enemy[node]
                if enemy > node:
                    continue
                mySize = self.size[node]
                enemySize = 0 if enemy == -1 else self.size[enemy]
                # print("node, mySize, enemySize:", node, mySize, enemySize)
                ret += max(mySize, enemySize)

        return ret

    def debug_print(self):
        print("parent, enemy, size")
        print(self.parent)
        print(self.enemy)
        print(self.size)


def readline():
    return sys.stdin.readline().strip()


if __name__ == "__main__":
    for _ in range(int(readline())):
        N, M = [int(x) for x in readline().split()]
        uf = UnionFind(N)
        has_contradict = False
        for comment_num in range(1, M+1):
            command, a, b = [x for x in readline().split()]
            a, b = int(a), int(b)

            if has_contradict:
                continue

            if command == "ACK":
                result = uf.ack(a, b)
            elif command == "DIS":
                result = uf.dis(a, b)

            # if uf.enemy[-1] != -1:
            #     print("set last enemy:", command, a, b)
            if not result:
                has_contradict = True
                sys.stdout.write("CONTRADICTION AT {}\n".format(comment_num))

        if not has_contradict:
            sys.stdout.write("MAX PARTY SIZE IS {}\n".format(uf.maxParty()))

