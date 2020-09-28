"""
Problem URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # # naive solution
        # idx = 0
        # while idx < len(nums)-1:
        #     if nums[idx] == nums[idx+1]:
        #         nums.pop(idx+1) # pop in-place
        #     else:
        #         idx += 1

        # return len(nums)

        # 2 pointer solution
        idx, start = 0, 0
        while start < len(nums):
            end = start
            while end < len(nums) and nums[start] == nums[end]:
                end += 1

            # start~end-1 has same numbers
            nums[idx] = nums[start]
            idx += 1
            start = end

        return idx