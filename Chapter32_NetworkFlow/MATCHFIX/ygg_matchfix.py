import sys
def FF(N, M, capacity, total_flow):
    V = N+M+2
    while True:
        parent = [-1] * V
        queue = [0]
        while queue and parent[1] == -1: # bfs 증가경로 찾기
            fr = queue.pop(0)
            for to, cap in enumerate(capacity[fr]):
                if cap > 0 and parent[to] == -1: # 유량을 더 흘려보낼수 있고 and 아직 방문하지 않음
                    queue.append(to)
                    parent[to] = fr
        
        if parent[1] == -1: # 더이상 증가경로가 없으면
            break

        # 증가경로가 있으면
        curr = 1
        flow_amount = float('inf')
        while curr != 0: # 해당 증가경로를 통해 흘려보낼수 있는 최대 유량을 찾음
            flow_amount = min(flow_amount, capacity[parent[curr]][curr])
            curr = parent[curr]      

        curr = 1
        while curr != 0: # 해당 최대 유량만큼 흘려보내줌
            capacity[parent[curr]][curr] -= flow_amount
            capacity[curr][parent[curr]] += flow_amount
            curr = parent[curr]

        total_flow += flow_amount

    return total_flow

def solution(capacity, N, M, minWin, wins):
    V = N + M + 2
    total_flow = 0

    for m in range(M+1):
        total_flow = FF(N, M, capacity, total_flow)
        if total_flow == M: # 현재의 capacity 상태로 모든 유량(매치) 를 소화할 수 있으면 정답
            if capacity[2+M][1] != 0: # 단, 이때 p0 to sink 는 항상 가득차있어야한다는 믿음이 깨지면 오답
                return -1
            else:
                return minWin + m
        for n in range(N): # 소화할수없으면 플레이어 to sink cap을 1씩 다 증가시켜줌
            capacity[2+M+n][1] += 1

    return -1 # 플레이어 to sink capacity를 M번까지 증가시켜봐도 p0가 우승할수 없으면
    
if __name__ == '__main__':
    sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline().rstrip())
    for _ in range(C):
        N, M = map(int, input().split())
        wins = [int(x) for x in sys.stdin.readline().rstrip().split()]
        V = N + M + 2
        capacity = [[0]*V for _ in range(V)]

        for m in range(M): 
            capacity[0][2+m] = 1
            p1, p2 = map(int, input().split())
            capacity[2+m][2+M+p1] = 1 # 매치 to 플레이어 간선
            capacity[2+m][2+M+p2] = 1

        minWin = wins[0] # 초기 0번플레이어의 승리 수
        maxWin = max(wins[1:])
        bonus = 0 if minWin > maxWin else maxWin - minWin +1 # 최초에는 플레이어0이 한번도 더 안이기고 우승이 가능한지 봐야함, 만약 애초에 다른플레이어의 승수가 더 많다면 그 플레이어를 이길만큼 capa를 가지고 시작
        capacity[2+M][1] = bonus  
        for n in range(1, N): # 플레이어 to 싱크 간선
            capacity[2+M+n][1] = minWin - wins[n] -1 + bonus

        ret = -1
        total_flow = 0
        for m in range(M+1):
            total_flow = FF(N, M, capacity, total_flow)
            if total_flow == M: # 현재의 capacity 상태로 모든 유량(매치) 를 소화할 수 있으면 정답
                if capacity[2+M][1] != 0: # 단, 이때 p0 to sink 는 항상 가득차있어야한다는 믿음이 깨지면 오답
                    pass
                else:
                    ret = minWin + m + bonus
                    break
            for n in range(N): # 소화할수없으면 플레이어 to sink cap을 1씩 다 증가시켜줌
                capacity[2+M+n][1] += 1

        print(ret)


