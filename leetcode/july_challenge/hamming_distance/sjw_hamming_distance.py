"""
Problem URL: https://leetcode.com/explore/featured/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3381/
"""

"""
Since Hamming Distance checks bitwise difference, we can use xor operation.
"""
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count(1)