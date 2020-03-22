from heapq import heappush, heappop

for _ in range(int(input())):
    n, a, b = map(int, input().split())
    val, ret = 1983, 0
    max_heap, min_heap = [], [] # len(max_heap) >= len(min_heap) 
    for _ in range(n):
        if max_heap and val > -max_heap[0]: heappush(min_heap, val)
        else: heappush(max_heap, -val)
        if len(max_heap) > len(min_heap) + 1:
            heappush(min_heap, -heappop(max_heap))
        elif len(min_heap) > len(max_heap):
            heappush(max_heap, -heappop(min_heap))
        ret = (ret - max_heap[0]) % 20090711
        val = (val * a + b) % 20090711
    print(ret)
