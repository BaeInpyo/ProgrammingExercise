"""
Problem URL: https://leetcode.com/problems/unique-paths/
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.sol1(m, n)
        # return self.sol2(m, n)

    def sol1(self, m, n):
        """Combinational solution with O(m+n) time"""
        return self._factorial(m+n-2) // (self._factorial(m-1) * self._factorial(n-1))

    def _factorial(self, n):
        """ Return n! """
        answer = 1
        for num in range(2, n+1):
            answer *= num

        return answer

    def sol2(self, m, n):
        """Dynamic programming solution with O(mn) time"""
        dp = [[1] * (n) for _ in range(m)]  # m*n matrix
        for idx in range(1, m):
            for jdx in range(1, n):
                dp[idx][jdx] = dp[idx-1][jdx] + dp[idx][jdx-1]

        return dp[m-1][n-1]