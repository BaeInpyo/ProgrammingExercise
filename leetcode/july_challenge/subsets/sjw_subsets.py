"""
Problem URL: https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/545/week-2-july-8th-july-14th/3387/
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = [[]]
        for num in nums:
            # add num to all subsets found until now
            curr = [subset + [num] for subset in answer]
            answer.extend(curr)

        return answer

    # def subsets_iter(self, nums):
    #     answer = [[]]
    #     for num in nums:
    #         # add num to all subsets found until now
    #         curr = [subset + [num] for subset in answer]
    #         answer.extend(curr)

    #     return answer

    # def subsets_recur(self, nums):
    #     if not nums:
    #         return [[]]

    #     answer = [[]]
    #     for idx in range(len(nums)):
    #         answer += self.subsets_recur(nums[:idx] + nums[idx+1:])