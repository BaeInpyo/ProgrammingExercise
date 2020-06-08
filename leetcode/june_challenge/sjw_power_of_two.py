"""
Problem URL: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3354/
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        seed = 1
        while seed < n:
            seed *= 2

        return seed == n