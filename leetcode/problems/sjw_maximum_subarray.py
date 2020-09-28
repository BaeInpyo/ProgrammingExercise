"""
Problem URL: https://leetcode.com/problems/maximum-subarray/
"""

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        # dp[i] = maximum sum ending with nums[i]
        dp = [0] * n
        dp[0] = nums[0]
        for idx in range(1, n):
            # quit previous sum if prev sum is negative
            dp[idx] = max(dp[idx-1] + nums[idx], nums[idx])

        return max(dp)

s = Solution()
print(s.maxSubArray([1]))
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))