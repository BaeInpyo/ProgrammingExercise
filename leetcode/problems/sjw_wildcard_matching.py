"""
Problem URL: https://leetcode.com/problems/wildcard-matching/
"""

import string

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # (p+1)*(s+1) matrix such that dp[idx][jdx] = isMatch(p[:idx], s[:jdx])
        dp = [[False] * (len(s)+1) for _ in range(len(p)+1)]

        # if both s and p is empty, true
        dp[0][0] = True

        # since s is empty, this can be true only p contains of "*"
        for idx in range(1, len(p)+1):
            dp[idx][0] = True if p[idx-1] == "*" and dp[idx-1][0] else False

        for idx in range(1, len(p)+1):
            for jdx in range(1, len(s)+1):
                if p[idx-1] == "*":
                    dp[idx][jdx] |= dp[idx-1][jdx-1] # "*" consumes 1 char
                    dp[idx][jdx] |= dp[idx][jdx-1]   # "*" consumes more than 1 char
                    dp[idx][jdx] |= dp[idx-1][jdx]   # "*" consumes empty
                elif p[idx-1] == "?":
                    dp[idx][jdx] = dp[idx-1][jdx-1]
                elif p[idx-1] in string.ascii_lowercase:
                    dp[idx][jdx] = dp[idx-1][jdx-1] and p[idx-1] == s[jdx-1]

        return dp[len(p)][len(s)]

s = Solution()
print(s.isMatch("aa", "a")) # false
print(s.isMatch("aa", "*")) # true
print(s.isMatch("cb", "?a"))    # false
print(s.isMatch("adceb", "*a*b"))   # true
print(s.isMatch("acdcb", "a*c?b"))  # false
print(s.isMatch("a", "**")) # true
print(s.isMatch("a", "a*")) # true
print(s.isMatch("ho", "ho**")) # true
print(s.isMatch("aab", "c*a*b")) # false