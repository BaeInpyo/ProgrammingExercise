"""
Problem URL: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3355/
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sidx, tidx = 0, 0
        while sidx<len(s) and tidx<len(t):
            if s[sidx] == t[tidx]:
                sidx += 1
                tidx += 1
            else:
                tidx += 1

        return sidx == len(s)