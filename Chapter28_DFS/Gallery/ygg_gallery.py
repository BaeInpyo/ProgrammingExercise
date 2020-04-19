import sys

def solution(curr, parent, edges, visits, safes, resultDict):
    if visits[curr]: # 이미 방문했으면 바로 리턴
        return
    visits[curr] = True

    try:
        del edges[curr][parent] # 나에게서 부모로 가는 엣지 제거
    except KeyError:
        pass
    children = list(edges[curr].keys()) # list로 만들필요 ㅇㅇ

    if parent == -1 and len(children) == 0: # 내가 외딴섬 leaf면 나자신에게 카메라를 달고 리턴
        resultDict[curr] = True

    for child in children:
        solution(child, curr, edges, visits, safes, resultDict)

    # 모든 자식을 다 돌고 나서
    if resultDict.get(curr): # 나에게 카메라가 달렸으면
        safes[curr] = True
        if parent != -1:
            safes[parent] = True
        try:
            del edges[parent][curr] # 부모에게서 나로 오는 엣지 제거
        except KeyError:
            pass
        # 나를 향하는 모든 엣지를 지우고 리턴
        for child in edges[curr].keys():
            safes[child] = True
            try:
                del edges[child][curr]
            except KeyError:
                pass
        return
    elif len(edges[curr].keys()) == 0: # 내가 leaf가 되었으면
        if safes[curr]: # 내가 이미 안전지대면
            try:
                del edges[parent][curr] # 부모에게서 나로 오는 엣지 제거
            except KeyError:
                pass
            return
        else:
            if parent == -1:
                resultDict[curr] = True
            else:
                # 나의 부모에게 카메라를달고 리턴
                resultDict[parent] = True
            return

if __name__ == '__main__':
    sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline().rstrip())
    for _ in range(C):
        G, H = [int(x) for x in sys.stdin.readline().rstrip().split()]
        edges = [{} for _ in range(G)]
        for _ in range(H):
            fr, to = [int(x) for x in sys.stdin.readline().rstrip().split()]
            edges[fr][to] = True
            edges[to][fr] = True

        safes = [False]*G
        visits = [False]*G
        resultDict = {}
        for node in range(G):
            solution(node, -1, edges, visits, safes, resultDict)

        print(len(resultDict))
