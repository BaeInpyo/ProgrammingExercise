import sys
INT_MAX = 2**32
from collections import deque
import time

class logger():
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.func(*args, **kwargs)
        print(f"[{self.func.__name__}] Elapsed time: {time.time()-start}")
        return result

def signal_generator(N):
    curr = 1983
    for _ in range(N):
        yield curr%10000 + 1
        curr = (curr * 214013 + 2531011) % INT_MAX

@logger
def solution(K, N):
    count = 0
    signals = signal_generator(N)
    p_sum = 0
    p_queue = deque([])
    try:
        while True:
            if p_sum == K:
                count += 1
                new = next(signals)
                p_queue.append(new)
                p_sum = p_sum - p_queue.popleft() + new
            elif p_sum > K:
                p_sum -= p_queue.popleft()
            elif p_sum < K:
                new = next(signals)
                p_queue.append(new)
                p_sum += new
    except StopIteration:
        pass

    return count
    


        
if __name__ == '__main__':
    sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline().rstrip())
    for _ in range(C):
        K, N = [int(x) for x in sys.stdin.readline().rstrip().split()]
        print(solution(K, N))

""" results
[solution] Elapsed time: 0.0
1
[solution] Elapsed time: 0.006003618240356445
4
[solution] Elapsed time: 6.845235347747803
1049
"""
