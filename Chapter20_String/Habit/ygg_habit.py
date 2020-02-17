import sys

def solution(K, script):
    count_dict = {}
    for length in range(len(script)-K+1, 0, -1):
        for i in range(len(script)-length+1):
            sub_str = script[i:i+length]
            count_dict[sub_str] = count_dict.get(sub_str, 0) + 1
            if count_dict[sub_str] >= K:
                return length
    
    return 0

    
if __name__ == '__main__':
    #sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline().rstrip())
    for _ in range(C):
        K = int(sys.stdin.readline().rstrip())
        script = sys.stdin.readline().rstrip()
        print(solution(K, script))


