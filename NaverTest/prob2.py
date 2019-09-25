import bisect
from functools import reduce

def solution(n):
    k = find_k(n)
    numbers = list(range(k+1))
    bst = []
    print('k, n:', k, n)

    for start in range(1, k+1):
        for count in range(2, k-start+2):
            curr = numbers[start:start+count]
            product = reduce(lambda x, y: x * y, curr, 1)
            idx = bisect.bisect_left(bst, product)
            # already exists
            if idx < len(bst) and bst[idx] == product:
                pass
            else:
                bisect.insort_left(bst, product)

    return bst[n-1]

def find_k(n):
    k = 1
    while True:
        if (k-1) * (k-2) > 2*n:
            return k

        k += 1

if __name__ == '__main__':
    for i in range(1, 10):
        print('{}: {}'.format(i, solution(i)))
