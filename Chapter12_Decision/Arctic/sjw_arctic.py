import sys, os
import math

# freopen equivalent
abs_path = os.path.abspath(os.path.dirname(__file__))
sys.stdin = open(os.path.join(abs_path, 'input.txt'), 'r')

def canCommunicate(points, radius):
    def distance(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))

    def reachable(remained, selected):
        for p1 in remained:
            for p2 in selected:
                if distance(p1, p2) <= radius:
                    return p1

        return None

    remained = points.copy()
    selected = set()
    selected.add(remained.pop())

    while remained:
        point = reachable(remained, selected)
        if point:
            remained.remove(point)
            selected.add(point)
        else:
            break

    return len(remained) == 0

    return len(remained) == 0

def solution(points):
    low, high = 0, 1000 * math.sqrt(2)
    for _ in range(20):
        mid = (low + high) / 2
        if canCommunicate(points, mid):
            high = mid
        else:
            low = mid

    answer = round(high, 2)
    print(answer)

def read_input():
    N = int(sys.stdin.readline().strip())
    points = set()
    for _ in range(N):
        x, y = tuple(float(x) for x in sys.stdin.readline().strip().split())
        points.add((x, y))

    return points

if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        points = read_input() # read input
        solution(points)
