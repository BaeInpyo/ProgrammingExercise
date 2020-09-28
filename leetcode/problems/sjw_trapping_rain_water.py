"""
Problem URL: https://leetcode.com/problems/trapping-rain-water/
"""

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        # return self.bruteForce(height)  # O(n^2), 2460ms
        return self.dynamicProgramming(height)  # O(n), 60ms

    def bruteForce(self, height):
        """ In each point, find highest bar in both left and right side """
        answer = 0
        n = len(height)
        for idx in range(1, n-1):
            left_max = max(height[:idx])
            right_max = max(height[idx+1:])
            area = min(left_max, right_max) - height[idx]
            answer += max(area, 0)  # if area < 0, does not add

        return answer

    def dynamicProgramming(self, height):
        """ Instead of find all leftmax and rightmax in bruteForce(), memorize
        it in seperate list which requires O(n) memories """
        if not height:
            # empty height
            return 0

        n = len(height)
        left_max, right_max = [0]*n, [0]*n
        left_max[0] = height[0]
        for idx in range(1, n):
            left_max[idx] = max(left_max[idx-1], height[idx])
        right_max[n-1] = height[n-1]
        for idx in reversed(range(n-1)):
            right_max[idx] = max(right_max[idx+1], height[idx])

        answer = 0
        for idx in range(n):
            area = min(left_max[idx], right_max[idx]) - height[idx]
            area = max(area, 0)
            answer += area

        return answer



s = Solution()
s.trap([0,1,0,2,1,0,1,3,2,1,2,1])