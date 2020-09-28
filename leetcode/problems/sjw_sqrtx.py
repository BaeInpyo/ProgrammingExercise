"""
Problem URL: https://leetcode.com/problems/sqrtx/
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        # return self.naiveSolution(x) # 2020ms, O(sqrt(n))
        return self.binarySearchSolution(x) # 40ms, O(logn)

    def naiveSolution(self, x):
        base = 0
        while base*base <= x:
            base += 1

        return base-1

    def binarySearchSolution(self, x):
        lo, hi = 0, x
        while lo < hi:
            mid = (lo + hi) // 2
            if mid*mid <= x < (mid+1)*(mid+1):
                return mid
            elif mid*mid < x:
                lo = mid + 1
            else:
                hi = mid

        return lo