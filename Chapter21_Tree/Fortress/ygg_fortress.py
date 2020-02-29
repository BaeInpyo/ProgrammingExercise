import sys
import math

longest = 0

class Wall():
    def __init__(self, x,y,r):
        self.x, self.y, self.r = x,y,r
        self.children = []
        
    def set_longest(self, val):
        global longest
        longest = val
    def get_longest(self):
        global longest
        return longest

    #def __str__(self):
    #    return f"x:{self.x}, y:{self.y}, r:{self.r}, children:{self.children}"
    #def __repr__(self):
    #    return self.__str__()

    def contain(self, wall):
        x1, y1, r1 = self.x, self.y, self.r
        x2, y2, r2 = wall.x, wall.y, wall.r
        if r1 >= math.sqrt((x1-x2)**2+(y1-y2)**2) + r2: # wall 이 self 에 속할떄
            return 1 
        elif r2 >= math.sqrt((x1-x2)**2+(y1-y2)**2) + r1: # self 가 wall에 속할때
            return -1
        else:
            return 0 # 두 벽이 포함관계가 없을때

    def insert(self, wall):
        for idx, child in enumerate(self.children):
            check = child.contain(wall)
            if check == 1: # 포함되면 재귀콜
                return child.insert(wall)
            elif check == -1: # 역으로 포함되면 children에서 빼고 역으로 재귀콜
                self.children[idx] = None
                wall.insert(child)
        
        # 지워진(None) 차일드 필터링
        self.children = [child for child in self.children if child]  
        # self의 children들에 포함관계가 없을때 children들과 sibling 으로 등록    
        self.children.append(wall)

    def get_children_depth(self):
        # children들의 뎁스를 각각 리스트로 구하고 그중 가장 긴 리프간의 패스를 longest에 set함(max일때)
        result = [0]
        for child in self.children:
            result.append(1+max(child.get_children_depth()))
        self.get_max_distance(result)
        return result

    def get_max_distance(self, children_depth_list):
        self.set_longest(max(self.get_longest(),sum(sorted(children_depth_list,reverse=True)[0:2])))

def build_wall_tree(walls, root):
    for wall in walls:
        root.insert(wall)
    return

def solution(root):
    return root.get_children_depth()
    
if __name__ == '__main__':
    #sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline().rstrip())
    for _ in range(C):
        longest = 0
        N = int(sys.stdin.readline().rstrip())
        walls = [Wall(*[int(x) for x in sys.stdin.readline().rstrip().split()]) for _ in range(N)]
        root = walls[0]
        del walls[0]
        build_wall_tree(walls, root)
        solution(root)
        print(longest)


