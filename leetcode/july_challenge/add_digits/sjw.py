"""
Problem URL: https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/547/week-4-july-22nd-july-28th/3402/
"""

class Solution:
    def addDigits(self, num: int) -> int:
        # return self.solution_with_loop(num)
        return self.solution_without_loop(num)

    def solution_with_loop(self, num):
        while num >= 10:
            sum_ = 0
            while num > 0:
                sum_ += num % 10
                num //= 10
            num = sum_

        return num

    def solution_without_loop(self, num):
        if num == 0:
            return 0
        if num%9 == 0:
            return 9
        return num%9