import sys
import os
import math

# freopen equivalent
abs_dir = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(abs_dir, "input.txt"), "r")


# return pre-calculated list which list[i] = number of factors of integer i
# about 25 seconds to end
def solution_complex():
    MAX = 10000001
    min_factor = list(range(MAX))
    min_factor_count = [1] * MAX
    num_factors = [2] * MAX

    for i in range(2, MAX):
        # i is prime number
        if min_factor[i] == i:
            for j in range(i * i, MAX, i):
                if min_factor[j] == j:
                    min_factor[j] = i

        # i is not prime number
        else:
            temp = i // min_factor[i]

            # can be divided more times
            if temp % min_factor[i] == 0:
                min_factor_count[i] = min_factor_count[temp] + 1
            # cannot be divided anymore
            else:
                min_factor_count[i] = 1

            num_factors[i] = num_factors[temp] * \
                (min_factor_count[i] + 1) // min_factor_count[i]

    return num_factors

# about 14 seconds to end
def solution_simple():
    MAX = 10000001
    num_factors = [2] * MAX
    sqrtn = int(math.sqrt(MAX))
    for i in range(2, sqrtn + 1):
        for j in range(i * i, MAX, i):
            num_factors[j] += (1 if j == i * i else 2)

    return num_factors

def solution(n, low, high, num_factors):
    return len([count for count in num_factors[low:high+1] if count == n])

if __name__ == "__main__":
    num_factors = solution_simple()

    c = int(sys.stdin.readline().strip())
    answers = []
    for _ in range(c):
        n, low, high = [int(x) for x in sys.stdin.readline().strip().split()]
        answers.append(solution(n, low, high, num_factors))

    for a in answers:
        print(a)