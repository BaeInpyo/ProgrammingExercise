"""
Problem URL: https://leetcode.com/problems/palindrome-number/
"""

import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return self.withString(x)

    def withInt(self, x):
        if x < 0:
            return False

        if x == 0:
            return True

        length = int(math.log(x, 10)) + 1
        for idx in range(length // 2):
            left = x // pow(10, length-1-2*idx)
            right = x % 10
            if left != right:
                return False

            x -= left * pow(10, length-1-2*idx)
            x //= 10

        return True

    def withString(self, x):
        string = str(x)
        left, right = 0, len(string)-1
        while left <= right:
            if string[left] != string[right]:
                return False

            left += 1
            right -= 1

        return True