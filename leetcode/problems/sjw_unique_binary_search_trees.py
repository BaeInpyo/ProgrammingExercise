"""
Problem URL: https://leetcode.com/problems/unique-binary-search-trees/

F(n) = sum of F(i) * F(n-1-i) for i in range [0, n-1]
In above equation, we consturct left subtree with i nodes, root with 1 node,
right substree with n-1-i nodes.
"""

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for num in range(2, n+1):
            curr = 0
            for idx in range(num):
                curr += dp[idx] * dp[num-1-idx]
                
            dp[num] = curr

        return dp[n]