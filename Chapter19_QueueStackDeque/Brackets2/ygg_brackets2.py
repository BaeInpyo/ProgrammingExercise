import sys
opening = {')': '(', '}': '{', ']': '['}

def solution(formula):
    stack = ['Empty']
    for c in formula:
        if c in ['(', '{', '[']:
            stack.append(c)
        else:
            if stack.pop() != opening[c]:
                return 'NO'
    if stack.pop() == 'Empty':
        return 'YES'
    else:
        return 'NO'
    
if __name__ == '__main__':
    sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline().rstrip())
    for _ in range(C):
        formula = sys.stdin.readline().rstrip()
        print(solution(formula))


