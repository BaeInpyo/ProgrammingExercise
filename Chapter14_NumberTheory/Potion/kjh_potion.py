from functools import reduce
from operator import add, sub

def euclidian(x, y):
    while y:
        x, y = y, x%y
    return x

def find_gcd(r: list):
    return reduce(euclidian, r[1:], r[0])

def greater_equal(l: list, r: list):
    for x, y in zip(l, r):
        if x < y: return False
    return True

def get_ans(r, p, unit):
    u_r = list(map(lambda x: x // unit, r))
    _r = u_r
    while not greater_equal(_r, p) or not greater_equal(_r, r):
        _r = list(map(add, _r, u_r))
    return list(map(sub, _r, p))

for _ in range(int(input())):
    n = int(input())
    r = list(map(int, input().split()))
    p = list(map(int, input().split()))
    
    unit = find_gcd(r)
    ans = get_ans(r, p, unit)
    print(*ans)
