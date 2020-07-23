"""
Problem URL: https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/547/week-4-july-22nd-july-28th/3399/
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # return self.solution1(nums) # 72ms
        return self.solution2(nums) # 100ms

    def solution1(self, nums):
        """Solution using set() in python
        
        Time complexity: O(n), space complexity: O(n)
        """
        set_ = set()
        for num in nums:
            if num in set_:
                set_.remove(num)
            else:
                set_.add(num)

        return list(set_)

    def solution2(self, nums):
        """Solution using XOR operator

        Time complexity: O(n), space complexity: O(1)
        Explanation: https://leetcode.com/problems/single-number-iii/discuss/68901/Sharing-explanation-of-the-solution
        """

        xored = 0

        # xor all numbers
        for num in nums:
            xored ^= num

        # mask only has 1 position as 1, e.g) 0001000
        mask = xored & (-xored)
        num1, num2 = 0, 0

        # partitioning into 2 groups
        for num in nums:
            if num & mask == 0:
                num1 ^= num
            else:
                num2 ^= num

        return [num1, num2]