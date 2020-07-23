"""
Problem URL: https://leetcode.com/problems/combination-sum/
"""

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = sorted(candidates)
        return self.search([], 0, target)

    def search(self, curr_comb, min_index, remain):
        """Return all combinations from currently selected combination
        
        Args:
            curr_comb: list which represents currently select numbers
            min_index: minimum index of candidates which we can select
            remain: remained sum
        """
        if remain == 0:
            return [curr_comb]

        answer = []
        for idx in range(min_index, len(self.candidates)):
            curr_num = self.candidates[idx]
            if self.candidates[idx] <= remain:
                answer.extend(self.search(curr_comb + [curr_num], idx, remain-curr_num))

        return answer

s = Solution()
print(s.combinationSum([2,3,6,7], 7))
print(s.combinationSum([2,3,5], 8))
