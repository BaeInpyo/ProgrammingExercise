import sys
import os

# freopen equivalent
abs_dir = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(abs_dir, "input.txt"), "r")


def solution(formula):

    stack = []
    left = ["(", "{", "["]  # left parenthesis
    right = [")", "}", "]"] # right parenthesis
    match = {}  # keep matching parenthesis
    for idx in range(len(left)):
        # we only keep right parenthesis as key
        match[right[idx]] = left[idx]

    for char in formula:
        if char in left:
            stack.append(char)
        elif char in right:
            if not stack or stack[-1] != match[char]:
                # parenthesis is not matched
                return "NO"
            else:
                # parenthesis is matched
                stack.pop()

    # if stack is not empyt, formula is wrong
    if stack:
        return "NO"
    else:
        return "YES"


if __name__ == "__main__":
    answers = []
    C = int(sys.stdin.readline().strip())
    for _ in range(C):
        formula = sys.stdin.readline().strip()
        answers.append(solution(formula))

    sys.stdout.write("\n".join(answers) + "\n")