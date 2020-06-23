"""
Problem URL: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/542/week-4-june-22nd-june-28th/3368/
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # # O(nlogn) time / O(1) space: sort
        # nums = sorted(nums)
        # before, count = nums[0], 0
        # for num in nums:
        #     if num == before:
        #         count += 1
        #     else:
        #         if count == 3:
        #             before = num
        #             count = 1
        #         else:
        #             break

        # return before

        # # O(n) time / O(n) space: dictionary
        # count = dict()
        # for num in nums:
        #     if num in count:
        #         count[num] += 1
        #     else:
        #         count[num] = 1

        # for num in count:
        #     if count[num] != 3:
        #         return num

        # return -1

        # O(n) time / O(1) space: bit operation
        # https://leetcode.com/problems/single-number-ii/discuss/43295/Detailed-explanation-and-generalization-of-the-bitwise-operation-method-for-single-numbers
        x1, x2, mask = 0, 0, 0
        for num in nums:
            x2 ^= x1 & num
            x1 ^= num
            mask = ~(x1 & x2)
            x2 &= mask
            x1 &= mask

        return x1
