"""
Problem URL: https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/545/week-2-july-8th-july-14th/3388/
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2:].rjust(32, "0")  # binary expression
        binary = binary[::-1]   # reverse
        return int(binary, 2)   # revert to int
        