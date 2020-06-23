import sys
import math

class Djset():
    def __init__(self, idx):
        self.idx = idx
        self.parent = self
        self.depth = 1

    def get_root(self):
        curr_root = self.parent
        while curr_root != curr_root.parent:
            curr_root = curr_root.parent
        self.parent = curr_root  # 최적화, 루트를 찾을때마다 새 루트로 자기 부모를 갱신해줌
        return curr_root
    
    def set_parent(self, parent):
        self.parent = parent

    def contains(self, other):
        return self.get_root() == other.get_root()

    @staticmethod
    def union(a, b):
        a_root, b_root = a.get_root(), b.get_root()
        if a_root.depth > b_root.depth: # 뎁스가 더 큰쪽에 작은쪽을 붙임 -> 전체 뎁스 최적화
            b_root.set_parent(a_root)
        else:
            a_root.set_parent(b_root)

def get_dist(a, b):
    a_x, a_y = a
    b_x, b_y = b
    return math.sqrt((a_x-b_x)**2 + (a_y-b_y)**2)

def solution(djset_dict, num_djset, distances):
    result = 0
    # 모든 컴포넌트가 합쳐질때까지 돌림
    for distance, fr, to in distances:
        if num_djset <= 1:
            break
        if not djset_dict[fr].contains(djset_dict[to]):  # 포함되면 이미 두 정점이 한 컴포넌트 안에있음, 스킵해도됨
            Djset.union(djset_dict[fr], djset_dict[to]) # 두 정점을 한 컴포넌트로 합쳐줌
            num_djset -= 1
            result += distance

    return result

if __name__ == '__main__':
    sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline().rstrip())
    for _ in range(C):
        N, M = [int(x) for x in sys.stdin.readline().rstrip().split()]
        x_list = [int(x) for x in sys.stdin.readline().rstrip().split()]
        y_list = [int(x) for x in sys.stdin.readline().rstrip().split()]
        buildings = list(zip(x_list, y_list))

        djset_dict = {i:Djset([i]) for i in range(N)}
        num_djset = N

        distances = []
        for i in range(N):
            for j in range(i+1, N):
                distance = get_dist(buildings[i], buildings[j])
                distances.append((distance, i, j))
        distances.sort()

        for _ in range(M):
            fr, to = [int(x) for x in sys.stdin.readline().rstrip().split()]
            if not djset_dict[fr].contains(djset_dict[to]): # 포함되면 이미 두 정점이 한 컴포넌트 안에있음, 스킵해도됨
                Djset.union(djset_dict[fr], djset_dict[to]) # 두 정점을 한 컴포넌트로 합쳐줌
                num_djset -= 1



        print(solution(djset_dict, num_djset, distances))


