"""
Problem URL: https://leetcode.com/problems/container-with-most-water/

1. From leftmost and rightmost, move one of line to central dicretion such
that current move of line is bigger than other move of line.
2. If left >= right, break

I'm not sure how to validate this.

After submission, I found that above is wrong answer.
Rather, we can move smaller one every time
"""

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer = 0
        left, right = 0, len(height)-1
        while left < right:
            area = (right - left) * min(height[left], height[right])
            answer = max(answer, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return answer


s = Solution()
testcases = [
    [1,8,6,2,5,4,8,3,7],
    [1,2],
    [2,1],
    [1,2,3],
    [1,3,2,5,25,24,5],
    [3,2,1,20,20]
]

for case in testcases:
    print(s.maxArea(case))