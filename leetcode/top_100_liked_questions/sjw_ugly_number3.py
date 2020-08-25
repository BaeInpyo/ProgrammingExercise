"""
Problem URL: https://leetcode.com/problems/ugly-number-iii/
"""

import math

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        lcmab = a*b // math.gcd(a, b)
        lcmbc = b*c // math.gcd(b, c)
        lcmca = c*a // math.gcd(c, a)
        lcmabc = lcmab * c // math.gcd(lcmab, c)

        def _count(x, a, b, c, lcmab, lcmbc, lcmca, lcmabc):
            """ Return number of ugly numbers <= x """
            return x//a + x//b + x//c - x//lcmab - x//lcmbc - x//lcmca + x//lcmabc

        # do binary search to find nth ugly number
        # if x is nth ugly numbers, count(x) = n and count(x-1) < n
        lo, hi = 1, 2*pow(10,9)+1
        while lo < hi:
            mid = (lo+hi) // 2
            if _count(mid, a, b, c, lcmab, lcmbc, lcmca, lcmabc) < n:
                lo = mid + 1
            else:
                hi = mid

        return lo
