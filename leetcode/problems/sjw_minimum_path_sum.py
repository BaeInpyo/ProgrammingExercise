"""
Problem URL: https://leetcode.com/problems/minimum-path-sum/

We have to consider all possible cases, i.e, this is not greedy problem.
Also, we can think of DP.
"""

from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # dp[a][b] = min path sum from (a, b) to (m-1, n-1)
        dp = [[None] * (n) for _ in range(m)]
        dp[m-1][n-1] = grid[m-1][n-1]
        for idx in reversed(range(n-1)):
            dp[m-1][idx] = dp[m-1][idx+1] + grid[m-1][idx]
        for idx in reversed(range(m-1)):
            dp[idx][n-1] = dp[idx+1][n-1] + grid[idx][n-1]

        # fill dp table
        for idx in reversed(range(m-1)):
            for jdx in reversed(range(n-1)):
                dp[idx][jdx] = min(dp[idx+1][jdx], dp[idx][jdx+1]) + grid[idx][jdx]

        return dp[0][0]

s = Solution()
s.minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
])