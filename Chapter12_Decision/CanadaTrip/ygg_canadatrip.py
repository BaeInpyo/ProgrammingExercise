import sys

def getCount(_from, to, cityFrom, cityTo, cityPeriod):
    _from = _from + (cityFrom - _from)%cityPeriod if cityFrom < _from else cityFrom # 타겟범위가 도시범위보다 바깥이면 타겟범위를 도시의 첫번째 눈금까지 줄이고 도시범위 안쪽이면 가장 안쪽의 눈금으로 당김
    to = to - (to - cityTo)%cityPeriod if cityTo > to else cityTo

    return (to-_from) // cityPeriod + 1


def solution(cities, K, _from, to):
    count = 0
    leftFrom, leftTo = _from, _from + (to-_from)//2
    rightFrom, rightTo = _from + (to-_from)//2+1, to

    if _from == to:
        return to

    # get left half count
    for cityFrom, cityTo, cityPeriod in cities:
        if cityFrom > leftTo or cityTo < leftFrom:
            continue
        count += getCount(leftFrom, leftTo, cityFrom, cityTo, cityPeriod)
        if count >= K:
            return solution(cities, K, leftFrom, leftTo) # 왼쪽 절반의 갯수로 충분하면 왼쪽으로 리커젼
    
    # 왼쪽 절반의 갯수로 부족하면 오른쪽으로 리커젼
    return solution(cities, K-count, rightFrom, rightTo)


        
    
if __name__ == '__main__':
    #sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline().rstrip())
    for _ in range(C):
        N, K = list(map(int, sys.stdin.readline().rstrip().split()))
        cities = []
        for _ in range(N):
            L, M, G = list(map(int, sys.stdin.readline().rstrip().split()))
            cities.append((L-M, L, G)) # from, to, period
        print(solution(cities, K, 0, 8030000))
