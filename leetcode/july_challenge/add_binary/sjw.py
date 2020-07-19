"""
Problem URL: https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/546/week-3-july-15th-july-21st/3395/

Since python provides int() and format(), we can utilize it. Otherwise, we need
to use XOR operator from end to for both a and b.
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)
        return format(a + b, "b")   # return binary string