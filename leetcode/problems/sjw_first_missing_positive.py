"""
Problem URL: https://leetcode.com/problems/first-missing-positive/
"""
from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        existOne = False

        # Only number in range [1, n] is valid. Mark invalid as 1
        for idx in range(n):
            if nums[idx] == 1:
                existOne = True

            if not (1 <= nums[idx] <= n):
                nums[idx] = 1

        # If 1 does not exist, answer is 1
        if not existOne:
            return 1

        # Currently, all number in nums are in range [1, n]
        # Mark nums[idx] as negative if idx+1 exists.
        for idx in range(n):
            index = abs(nums[idx]) - 1
            nums[index] = -1 * abs(nums[index]) # mark as negative

        # nums[idx] is positive only if (idx+1) does not exist
        for idx in range(n):
            if nums[idx] > 0:
                return idx + 1

        # All integer in range [1, n] exists, return (n + 1)
        return n + 1

s = Solution()
s.firstMissingPositive([2])