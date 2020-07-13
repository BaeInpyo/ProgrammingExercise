import sys
import collections
def FF(capacity, flow, total_flow):
    while True:
        parent = {}
        queue = collections.deque(['source'])
        while len(queue) > 0 and (parent.get('sink', None) == None): # bfs 증가경로 찾기
            fr = queue.popleft()
            for to, cap in capacity[fr]:
                res = cap - flow.get((fr, to), 0)
                if res > 0 and (parent.get(to, None) == None): # 유량을 더 흘려보낼수 있고 and 아직 방문하지 않음
                    queue.append(to)
                    parent[to] = (fr, res)
        
        if parent.get('sink', None) == None: # 더이상 증가경로가 없으면
            break

        # 증가경로가 있으면
        curr = 'sink'
        flow_amount = 10000
        while parent.get(curr, None) != None: # 해당 증가경로를 통해 흘려보낼수 있는 최대 유량을 찾음
            p, res = parent[curr]
            flow_amount = min(flow_amount, res)
            curr = p            

        curr = 'sink'
        while parent.get(curr, None) != None: # 해당 최대 유량만큼 흘려보내줌
            p, _ = parent[curr]
            flow[(p, curr)] = flow.get((p, curr), 0) + flow_amount
            flow[(curr, p)] = flow.get((curr, p), 0) - flow_amount
            curr = p

        total_flow += flow_amount

    return flow, total_flow

def solution(capacity, N, M, minWin, maxWin):
    flow = {}
    total_flow = 0
    for m in range(M+1):
        flow, total_flow = FF(capacity, flow, total_flow)
        if total_flow == M: # 현재의 capacity 상태로 모든 유량(매치) 를 소화할 수 있으면 정답
            if capacity['p0'][0][1] != flow.get(('p0', 'sink'), 0): # 단, 이때 p0 to sink 는 항상 가득차있어야한다는 믿음이 깨지면 오답
                return -1
            else:
                return minWin + m
        for n in range(N): # 소화할수없으면 플레이어 to sink cap을 1씩 다 증가시켜줌
            _, cap = capacity['p'+str(n)][0]
            capacity['p'+str(n)][0] = ('sink', cap+1)

    return -1 # 플레이어 to sink capacity를 M번까지 증가시켜봐도 p0가 우승할수 없으면
    
if __name__ == '__main__':
    sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline().rstrip())
    for _ in range(C):
        N, M = [int(x) for x in sys.stdin.readline().rstrip().split()]
        wins = [int(x) for x in sys.stdin.readline().rstrip().split()]
        matches = [[int(x) for x in sys.stdin.readline().rstrip().split()] for _ in range(M)]
        capacity = {'source': [('m'+str(m), 1) for m in range(M)]} # 소스 to 매치 간선
        p0_cnt = 0 # 플레이어 0의 매치 수
        for m, match in enumerate(matches): # 매치 to 플레이어 간선
            p1, p2 = match
            if p1 == 0 or p2 == 0:
                p0_cnt += 1
            capacity['m'+str(m)] = [('p'+str(p1), 1), ('p'+str(p2), 1)]         
        minWin = wins[0] # 초기 0번플레이어의 승리 수
        maxWin = minWin + p0_cnt # 0번 플레이어의 최대 승리 수
        capacity['p0'] = [('sink', 0)] # 최초에는 플레이어0이 한번도 더 안이기고 우승이 가능한지 봐야함
        for n in range(1, N): # 플레이어 to 싱크 간선
            capacity['p'+str(n)] = [('sink', minWin - wins[n] - 1)]
        capacity['sink'] = []
        print(solution(capacity, N, M, minWin, maxWin))


