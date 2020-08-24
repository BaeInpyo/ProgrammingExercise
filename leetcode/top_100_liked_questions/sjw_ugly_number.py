"""
Problem URL: https://leetcode.com/problems/ugly-number/
"""

class Solution:
    def isUgly(self, num: int) -> bool:
        factors = [2, 3, 5]
        for factor in factors:
            while num%factor == 0:
                num //= factor

        return num == 1

s = Solution()
print(s.isUgly(2000000000))