"""
Problem URL: https://leetcode.com/problems/roman-to-integer/
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        answer = 0
        number = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        for (idx, symbol) in enumerate(s):
            if (idx+1) < len(s) and (
                (symbol == "I" and s[idx+1] in ["V", "X"])
                or (symbol == "X" and s[idx+1] in ["L", "C"])
                or (symbol == "C" and s[idx+1] in ["D", "M"])
            ):
                answer -= number[symbol]
            else:
                answer += number[symbol]

        return answer