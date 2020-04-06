def solution(case_num, digits):
    answer = ""
    maximum = 0
    for digit in digits:
        digit = int(digit)
        remain_paren = digit
        idx = 0
        for idx in reversed(range(len(answer))):
            curr = answer[idx]
            if curr == ")":
                if remain_paren > 0:
                    remain_paren -= 1
                else:
                    break
            else:
                break

        # now, we can insert to indext at (idx+1)
        string_to_insert = "(" * remain_paren + str(digit) + ")" * remain_paren
        answer = answer[:idx+1] + string_to_insert + answer[idx+1:]

    print("Case #{}: {}".format(case_num, answer))


if __name__ == "__main__":
    T = int(input())
    for case_num in range(1, T+1):
        digits = input()
        solution(case_num , digits)