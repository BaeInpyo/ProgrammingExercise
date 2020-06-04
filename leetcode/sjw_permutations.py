"""
Problem URL: https://leetcode.com/problems/permutations/
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        
        result = []
        for num in nums:
            remain = [_num for _num in nums if _num != num]
            for _permute in self.permute(remain):
                result.append([num] + _permute)
                
        return result