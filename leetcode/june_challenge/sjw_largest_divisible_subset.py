"""
Problem URL: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3359/

This can be solved similar with LIS problem.

1. Sort nums
2. dp[i] = max length of subset of nums[:i] that contains arr[i]
3. dp[i] = max(dp[k]+1 such that arr[i]%arr[k] = 0, k=0~i-1)
"""


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        nums = sorted(nums, reverse=True)
        dp = [None] * len(nums)
        prev = [None] * len(nums)
        dp[0] = (0, 1)  # (idx, length)
        for idx in range(1, len(nums)):
            candidates = [(None, 1)]
            for jdx in range(0, idx):
                # nums[idx] >= nums[jdx] because it is sorted
                if nums[idx] % nums[jdx] == 0:
                    candidates.append((jdx, dp[jdx]))

            candidates.sort(key=lambda x: x[1], reverse=True) # sort by dp[jdx]
            dp[idx] = candidates[0][1] + 1
            prev[idx] = candidates[0][0]

        _, idx = sorted([(length, idx) for (idx, length) in enumerate(dp)])[0]
        subset = []
        while prev[idx]:
            subset.append(nums[idx])
            idx = prev[idx]

        return reversed(subset)