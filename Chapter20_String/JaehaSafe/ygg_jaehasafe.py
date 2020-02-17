import sys

def get_ticks(current, next_config, direction):
    current *= 2
    count = 1
    if direction: # 시계방향
        for i in range(1, len(next_config)):
            if current[len(next_config)-i:-i] == next_config:
                return count
            count += 1
    else:
        for i in range(1, len(next_config)):
            if current[i:len(next_config)+i] == next_config:
                return count
            count += 1
    return count

def solution(current, configs, direction):
    if configs == []:
        return 0
    return get_ticks(current, configs[0], direction) + solution(configs[0], configs[1:], not direction)
    
if __name__ == '__main__':
    sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline().rstrip())
    for _ in range(C):
        N = int(sys.stdin.readline().rstrip())
        current = sys.stdin.readline().rstrip()
        configs = [sys.stdin.readline().rstrip() for _ in range(N)]
        print(solution(current, configs, True))

