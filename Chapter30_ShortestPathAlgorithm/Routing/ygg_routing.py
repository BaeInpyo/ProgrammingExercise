import sys
import heapq

push = heapq.heappush
pop = heapq.heappop
def solution(N, noise_dict, start, end):
    distance_heap = []
    visited = {start}
    min_distance_dict = {i:float('inf') for i in range(N)}
    for edge in noise_dict[start]:
        c, to = edge
        push(distance_heap, (edge))
        min_distance_dict[to] = c
    
    while distance_heap:
        min_edge = pop(distance_heap)
        min_c, min_fr = min_edge
        if min_fr == end:
            return min_c
        visited.update([min_fr])
        for c, to in noise_dict[min_fr]:
            if (min_distance_dict[to] <= c*min_c) or (to in visited): # 첫번째 조건 : 이거 안해줘도 민힙이라 상관없는데 민힙 깊이 줄이기위해서 넣어줘 봄
                continue
            push(distance_heap, (c*min_c, to))
            min_distance_dict[to] = c*min_c # 이거 안해줘도 민힙이라 상관없는데 민힙 깊이 줄이기위해서 넣어줘 봄

    return min_distance_dict[end] # 이거 해줘야 start 에서 end로의 간선 하나만 있고 경유간선이 하나도 없을때 처리 가능
if __name__ == '__main__':
    sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline().rstrip())
    for _ in range(C):
        N, M = [int(x) for x in sys.stdin.readline().rstrip().split()]
        noise_dict = {i: [] for i in range(N)}

        for _ in range(M):
            fr, to, c = [x for x in sys.stdin.readline().rstrip().split()]
            fr, to, c = int(fr), int(to), float(c)
            noise_dict[fr].append((c, to))
            #noise_dict[to].append((c, fr))

        print('%.10f' % solution(N, noise_dict, 0, N-1))
