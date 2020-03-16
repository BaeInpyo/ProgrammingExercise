import sys
import heapq

def input_generator(N, a, b):
    prev = 1983
    yield prev
    for _ in range(1, N):
        nxt = (prev*a + b) % 20090711
        yield nxt
        prev = nxt
    
def solution2(A,N):
    if N == 1:
        return 1983
    first = next(A)
    second = next(A)
    if first > second:
        max_heap = [-second]
        min_heap = [first]
        result = first + second
    else:
        max_heap = [-first]
        min_heap = [second]
        result = first * 2
    length = 2
    for A_i in A:
        max_top = -heapq.heappop(max_heap)
        min_top = heapq.heappop(min_heap)
        rank = sorted([max_top, A_i, min_top])

        if length % 2 == 1:
            heapq.heappush(max_heap, -rank[0])
            heapq.heappush(min_heap, rank[1])
            heapq.heappush(min_heap, rank[2])
        else:
            heapq.heappush(max_heap, -rank[0])
            heapq.heappush(max_heap, -rank[1])
            heapq.heappush(min_heap, rank[2])

        median = -heapq.heappop(max_heap)
        heapq.heappush(max_heap, -median)
        result += median
        length += 1

    return result % 20090711



if __name__ == '__main__':
    #sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline().rstrip())
    for _ in range(C):
        N, a, b = [int(x) for x in sys.stdin.readline().rstrip().split()]
        #A = input_generator(N, a, b)
        #print(solution(A, N))
        A = input_generator(N, a, b)
        print(solution2(A, N))


