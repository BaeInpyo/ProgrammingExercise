import sys
import os
import heapq


'''
String that appears in front will be counter more
Therefore, we need to sort strings
'''

def solution(n, ls):
    heap = ls[:]
    heapq.heapify(heap)
    result = 0

    while len(heap) >= 4:
        a, b, c ,d = [heapq.heappop(heap) for _ in range(4)]
        if a + b > d:
            # (a,b) + (c,d)
            result += (a + b + c + d)
            heapq.heappush(heap, a + b)
            heapq.heappush(heap, c + d)
        else:
            # (a,b) + (a+b,c)
            result += a + b
            heapq.heappush(heap, a + b)
            heapq.heappush(heap, c)
            heapq.heappush(heap, d)

    if len(heap) == 3:
        n1, n2, n3 = [heapq.heappop(heap) for _ in range(3)]
        result += 2 * n1 + 2 * n2 + n3

    else:
        result += sum(heap)

    return result

if __name__ == '__main__':
    # freopen equivalent
    abs_path = os.path.abspath(os.path.dirname(__file__))
    sys.stdin = open(os.path.join(abs_path, 'input.txt'), 'r')

    def get_line():
        return sys.stdin.readline().strip()

    c = int(get_line())
    answers = []

    for _ in range(c):
        n = int(get_line())
        ls = [int(x) for x in get_line().split()]
        answers.append(solution(n, ls))

    for a in answers:
        print(a)
