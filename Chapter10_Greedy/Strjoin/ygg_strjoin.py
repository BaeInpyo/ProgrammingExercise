import sys
import heapq
def solution(numbers):
    heapq.heapify(numbers)
    result = 0
    while len(numbers) > 1:
        min1, min2 = heapq.heappop(numbers), heapq.heappop(numbers)
        result += min1 + min2
        heapq.heappush(numbers, min1+min2)
    return result
    
if __name__ == '__main__':
    #sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline().rstrip())
    for _ in range(C):
        n = int(sys.stdin.readline().rstrip())
        numbers = list(map(int, sys.stdin.readline().rstrip().split()))
        print(solution(numbers))


