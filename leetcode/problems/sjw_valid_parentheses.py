"""
Problem URL: https://leetcode.com/problems/valid-parentheses/
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        for char in s:
            if char in ["(", "{", "["]:
                stack.append(char)
            elif char in match.keys():
                if stack and stack[-1] == match[char]:
                    # parenthesis matches
                    stack.pop()
                else:
                    # stack is empty or parenthesis does not match
                    return False

        return not stack