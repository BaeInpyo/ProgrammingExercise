"""
Problem URL: https://leetcode.com/problems/permutations/
"""

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.permute_recur(nums)

    def permute_recur(self, nums):
        if not nums:
            return [[]]

        answer = []
        for (idx, num) in enumerate(nums):
            remain = nums[:idx] + nums[idx+1:]
            answer.extend([[num] + x for x in self.permute_recur(remain)])

        # print("nums: ", nums, "return:", answer)
        return answer


# s = Solution()
# s.permute([1,2])
# s.permute([1,2,3])