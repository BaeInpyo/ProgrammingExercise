"""
Problem URL: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/543/week-5-june-29th-june-30th/3375/
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        mathematical solution
        """
        # def factorial(num):
        #     answer = 1
        #     for idx in range(1, num+1):
        #         answer *= idx
        #     return answer

        # return factorial(m+n-2) // (factorial(m-1) * factorial(n-1))

        """
        dp solution
        dp[i][j] = number of ways to go i*j grid
        """
        # initialize matrix
        dp = [[0]*(n+1) for _ in range(m+1)]
        for idx in range(1, m+1):
            dp[idx][1] = 1
        for jdx in range(1, n+1):
            dp[1][jdx] = 1

        # fill matrix
        for idx in range(2, m+1):
            for jdx in range(2, n+1):
                dp[idx][jdx] = dp[idx-1][jdx] + dp[idx][jdx-1]

        return dp[m][n]