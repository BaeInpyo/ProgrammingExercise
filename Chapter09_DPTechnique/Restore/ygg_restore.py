import sys

env_dict = {}

def mergeTwoStr(prev, next):
    diff = len(prev) - len(next) +1 if len(prev) - len(next) > 0 else 1
    for start in range(diff, len(prev)):
        if prev[start:] == next[:len(prev)-start]:
            return prev+next[len(prev)-start:]
    return prev+next

def isSub(subs):
    return (lambda x: (sum(map(lambda y: y.find(x) != -1,subs)) == 1))

def preProcSubs(subs):
    subs = list(set(subs)) # 동일한게 있으면 하나만 남김
    return list(filter(isSub(subs), subs)) # 자기가 리스트에 있는 애들중 하나라도 서브스트링인 애들을 제외함

def solution(prev, subs):
    min_len = 15*40 + 1
    result = ''
    key = (prev, ' '.join(subs))
    if env_dict.get(key, -1) != -1:
        return env_dict[key]

    for i in range(len(subs)):
        sub = subs.pop(i) # 제거
        case = mergeTwoStr(sub, solution(sub, subs))
        if min_len > len(case):
            min_len = len(case)
            result = case
        subs.insert(i, sub) # 복구

    env_dict[key] = result
    return result
            
    
    
if __name__ == '__main__':
    #sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline().rstrip())
    for _ in range(C):
        env_dict = {}
        k = int(sys.stdin.readline().rstrip())
        subs = []
        for _ in range(k):
            subs.append(sys.stdin.readline().rstrip())
        print(solution('', preProcSubs(subs)))

