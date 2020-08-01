"""
Problem URL: https://leetcode.com/explore/featured/card/july-leetcoding-challenge/548/week-5-july-29th-july-31st/3407/

We can easily find that f(n) = f(n-1) + f(n-2), i.e, fibonacci
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0], dp[1] = 1, 1
        for idx in range(2, len(dp)):
            dp[idx] = dp[idx-1] + dp[idx-2]

        return dp[n]