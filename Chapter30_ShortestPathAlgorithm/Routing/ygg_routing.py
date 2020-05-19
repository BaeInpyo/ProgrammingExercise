import sys
import heapq

push = heapq.heappush
pop = heapq.heappop
def solution(N, noise_dict, start, end):
    distance_heap = []
    visited = {start}
    for edge in noise_dict[start]:
        push(distance_heap, (edge))
    
    while True:
        min_edge = pop(distance_heap)
        min_c, min_fr = min_edge
        if min_fr == end:
            return min_c
        visited.update([min_fr])
        for c, to in noise_dict[min_fr]:
            #if to in visited:
            #    continue
            push(distance_heap, (c*min_c, to))

    return -1
if __name__ == '__main__':
    sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline().rstrip())
    for _ in range(C):
        N, M = [int(x) for x in sys.stdin.readline().rstrip().split()]
        noise_dict = {i: [] for i in range(N)}

        for _ in range(M):
            fr, to, c = [float(x) for x in sys.stdin.readline().rstrip().split()]
            noise_dict[fr].append((c, to))
            #noise_dict[to].append((c, fr))

        print('%.10f' % solution(N, noise_dict, 0, N-1))
