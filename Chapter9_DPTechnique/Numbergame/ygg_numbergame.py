import sys

env_dict = {}

def solution(numbers):
    length = len(numbers)
    case1 = -99999999
    case2 = -99999999
    if length == 0:
        return 0

    if env_dict.get((tuple(numbers)), -1) != -1:
        return env_dict[(tuple(numbers))]

    if length >= 2:
        # 왼쪽 두개 지우기
        case1 = -solution(numbers[2:])
        # 오른쪽 두개 지우기
        case2 = -solution(numbers[:-2])
    # 왼쪽 하나 선택 or 오른쪽 하나 선택
    case3 = numbers[0] - solution(numbers[1:])
    case4 = numbers[-1] - solution(numbers[:-1])
    result = max(case1,case2,case3,case4)

    env_dict[(tuple(numbers))] = result

    return result
            
    
    
if __name__ == '__main__':
    #sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline().rstrip())
    for _ in range(C):
        env_dict = {}
        n = sys.stdin.readline().rstrip()
        numbers = list(map(int, sys.stdin.readline().rstrip().split()))
        result = solution(numbers)
        print(result)
