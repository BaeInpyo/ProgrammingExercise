import sys, os
import math

# freopen equivalent
abs_path = os.path.abspath(os.path.dirname(__file__))
sys.stdin = open(os.path.join(abs_path, 'input.txt'), 'r')

'''
Summary of decision method
1. Define range of lower and upper bound of optimal value
2. Define function which takes value as argument and test
   if either [vaule, upperbound] or [lowerbound, value] satisfies condition
3. Find optimal value in range [lowerbound, upperbound] using function defined in 2. and binary search

In this Arctic problem, range is [0, 1000 * sqrt(2)] which is min/max value of distance between 2 points
canCommunicate is function for Summary 2.
'''

DIST = None # DIST[i][j] = distance between points[i] and points[j]

'''
Check if given radius will connect all points
time complexity: O(n^2)
'''
def canCommunicate(points, radius):
    N = len(points)
    visited = [0] * N
    queue = []  # index of points
    queue.append(0)
    visited[0] = 1

    while queue:
        curr = queue.pop()
        for i in range(N):
            if visited[i] == 0 and DIST[curr][i] <= radius:
                visited[i] = 1
                queue.append(i)

    return all(visited)

'''
We can define function get_distance(p1, p2) but this will be called too much.
So make matrix for reducing computation
'''
def init_dist(points):
    def distance(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
    global DIST
    N = len(points)
    DIST = [[0] * N for _ in range(N)]  # N x N 2d matrix
    for i in range(N):
        for j in range(N):
            DIST[i][j] = distance(points[i], points[j])
    return

def solution(points):
    init_dist(points)   # init DIST matrix
    low, high = 0, 1000 * math.sqrt(2)
    for _ in range(30):
        mid = (low + high) / 2
        if canCommunicate(points, mid):
            high = mid
        else:
            low = mid

    answer = round(high, 2)
    print("{0:0.2f}".format(answer))

def read_input():
    N = int(sys.stdin.readline().strip())
    points = []
    for _ in range(N):
        x, y = tuple(float(x) for x in sys.stdin.readline().strip().split())
        points.append((x, y))

    return points

if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        points = read_input()
        solution(points)
