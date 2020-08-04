"""
Problem URL: https://leetcode.com/problems/sort-colors/
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, 0
        for num in nums:
            if num == 0:
                red += 1
            elif num == 1:
                white += 1
            elif num == 2:
                blue += 1

        for idx in range(red):
            nums[idx] = 0

        for idx in range(red, red+white):
            nums[idx] = 1

        for idx in range(red+white, red+white+blue):
            nums[idx] = 2

        return