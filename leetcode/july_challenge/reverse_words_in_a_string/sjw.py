"""
Problem URL: https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/546/week-3-july-15th-july-21st/3391/
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split()
        return " ".join(words[::-1])