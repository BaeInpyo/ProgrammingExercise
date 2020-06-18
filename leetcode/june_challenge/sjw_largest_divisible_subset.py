"""
Problem URL: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3359/

This problem is similar with LIS (Longest Increasing Subsequence) probem.
"""

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums

        """
        dp[i] means length of largest divisible subset which has nums[i] as
        largest number.
        prev[i] means previous index in nums array such that nums[i] is added to
        current subset . If we track prev, we can re-build divisible subset.
        """
        nums = sorted(nums)
        dp = [1 for _ in range(len(nums))]
        prev = [None for _ in range(len(nums))]

        for idx in range(1, len(nums)):
            for jdx in range(idx):
                if nums[idx]%nums[jdx] == 0 and dp[idx] < dp[jdx]+1:
                    dp[idx] = dp[jdx] + 1
                    prev[idx] = jdx

        # start from index which is largest
        index, _ = sorted(enumerate(dp), key=lambda x: x[1])[-1]
        subset = [nums[index]]
        while prev[index] is not None:
            index = prev[index]
            subset.append(nums[index])

        return sorted(subset)