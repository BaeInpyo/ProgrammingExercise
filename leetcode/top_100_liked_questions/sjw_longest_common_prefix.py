"""
Problem URL: https://leetcode.com/problems/longest-common-prefix/
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        for (idx, chars) in enumerate(zip(*strs)):
            if len(set(chars)) > 1:
                # prefix breaks
                return strs[0][:idx]

        else:
            # shortest string is prefix
            return min(strs)
