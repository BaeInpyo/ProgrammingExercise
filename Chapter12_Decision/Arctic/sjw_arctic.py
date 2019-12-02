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

    remained = points.copy()
    selected = set()
    selected.add(remained.pop())
    while remained:
        for p1 in remained:
            for p2 in selected:
                if distance(p1, p2) <= radius:
                    remained.remove(p1)
                    selected.add(p1)
                    break

            # end for-loop without break
            else:
                continue
            # end for-loop with break
            break

        # no points in remained can communicate with points in selected
        else:
            break

    return len(remained) == 0

def solution(points):
    low, high = 0, 1000 * math.sqrt(2)
    for _ in range(30):
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
