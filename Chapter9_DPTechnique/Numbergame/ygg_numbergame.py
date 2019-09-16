env_dict = {}

def solution(numbers, turn, H_score, S_score):
    length = len(numbers)
    case1 = -99999999 if turn else 99999999
    case2 = -99999999 if turn else 99999999
    if length == 0:
        return H_score - S_score

    if env_dict.get((turn, tuple(numbers)), -1) != -1:
        return env_dict[(turn, tuple(numbers))]

    if turn:
        if length >= 2:
            # 왼쪽 두개 지우기
            case1 = solution(numbers[2:], (turn+1)%2, H_score, S_score)
            # 오른쪽 두개 지우기
            case2 = solution(numbers[:-2], (turn+1)%2, H_score, S_score)
        # 왼쪽 하나 선택 or 오른쪽 하나 선택
        case3 = solution(numbers[1:], (turn+1)%2, H_score+numbers[0], S_score)
        case4 = solution(numbers[:-1], (turn+1)%2, H_score+numbers[-1], S_score)
        result = max(case1,case2,case3,case4)

    else:
        if length >= 2:
            # 왼쪽 두개 지우기
            case1 = solution(numbers[2:], (turn+1)%2, H_score, S_score)
            # 오른쪽 두개 지우기
            case2 = solution(numbers[:-2], (turn+1)%2, H_score, S_score)
        # 왼쪽 하나 선택 or 오른쪽 하나 선택
        case3 = solution(numbers[1:], (turn+1)%2, H_score, S_score+numbers[0])
        case4 = solution(numbers[:-1], (turn+1)%2, H_score, S_score+numbers[-1])
        result = min(case1,case2,case3,case4)

    return result
            
    
    
if __name__ == '__main__':
    C = int(input().rstrip())
    for _ in range(C):
        env_dict = {}
        n = input().rstrip()
        numbers = list(map(int, input().rstrip().split()))
        result = solution(numbers, 1, 0, 0)
        print(result)
