import sys
import heapq

push = heapq.heappush
pop = heapq.heappop

def solution(V, fire_stations, edge_dict, fire_spots):
    distance_heap = []
    visited = fire_stations
    result = 0
    
    # 처음 출발 셋을 fire_stations로 잡고 거기 인접 엣지들을 다 업데이트해줌
    for start in fire_stations:
        for edge in edge_dict[start]:
            t, to = edge
            push(distance_heap, (edge))

    while fire_spots:
        min_edge = pop(distance_heap)
        min_t, min_fr = min_edge
        if min_fr in fire_spots:
            result += min_t
            fire_spots.remove(min_fr)
        visited.update([min_fr])
        for t, to in edge_dict[min_fr]:
            if to in visited:
                continue
            push(distance_heap, (t + min_t, to))

    return result
    
if __name__ == '__main__':
    sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline().rstrip())
    for _ in range(C):
        V, E, n, m = [int(x) for x in sys.stdin.readline().rstrip().split()]
        edge_dict = {i:[] for i in range(E)}
        for _ in range(E):
            a, b, t = [int(x) for x in sys.stdin.readline().rstrip().split()]
            edge_dict[a].append((t, b))
            edge_dict[b].append((t, a))
        fire_spots = {int(x) for x in sys.stdin.readline().rstrip().split()}
        fire_stations = {int(x) for x in sys.stdin.readline().rstrip().split()}

        print(solution(V, fire_stations, edge_dict, fire_spots))

