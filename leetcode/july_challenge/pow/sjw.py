"""
Problem URL: https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/546/week-3-july-15th-july-21st/3392/
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # return self.pow1(x, n) # 60ms
        return self.pow2(x, n) # 28ms

    def pow1(self, x, n):
        # python native operator
        return x**n

    def pow2(self, x, n):
        # python native module
        import math
        return math.pow(x, n)