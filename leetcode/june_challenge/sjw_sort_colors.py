"""
Problem URL: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3357/
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # last index of red, white, blue
        red, white, blue = 0, 0, 0
        for color in nums:
            if color==0:
                red += 1
            elif color==1:
                white += 1
            elif color==2:
                blue += 1

        for idx in range(red):
            nums[idx] = 0
        for idx in range(red, red+white):
            nums[idx] = 1
        for idx in range(red+white, red+white+blue):
            nums[idx] = 2

        return