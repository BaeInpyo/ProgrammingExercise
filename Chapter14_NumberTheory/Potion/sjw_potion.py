import sys
import os
from functools import reduce

# freopen equivalent
abs_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")
sys.stdin = open(abs_path, "r")

"""
i) find gcd of ri, i.e, ri = g * ri'
ii) find max(pi / ri')
iii) find minimum integer greater than or equal to result of ii)
iv) then answer ai = result of iii) / g * ri
"""


def solution(n, r, p):
    def gcd(a, b):
        a, b = max(a, b), min(a, b) # assert a >= b
        return (a if b == 0 else gcd(b, a % b))

    gcd_of_all_numbers = r[0]
    for i in range(1, n):
        gcd_of_all_numbers = gcd(gcd_of_all_numbers, r[i])

    max_k = max([p[i] / r[i] * gcd_of_all_numbers for i in range(n)])
    # find minimal integer >= max(pi / ri')
    max_k = int(max_k) if int(max_k) == max_k else int(max_k + 1)
    answer = [max_k * r[i] // gcd_of_all_numbers - p[i] for i in range(n)]
    answer = [str(x) for x in answer]
    return " ".join(answer)

if __name__ == "__main__":
    c = int(sys.stdin.readline().strip())
    for _ in range(c):
        n = int(sys.stdin.readline().strip())
        r = [int(x) for x in sys.stdin.readline().strip().split()]
        p = [int(x) for x in sys.stdin.readline().strip().split()]
        print(solution(n, r, p))