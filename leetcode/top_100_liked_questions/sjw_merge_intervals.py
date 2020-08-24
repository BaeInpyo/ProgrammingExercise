"""
Problem URL: https://leetcode.com/problems/merge-intervals/
"""

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # sort by start position
        intervals.sort(key=lambda item: item[0])
        answer = [intervals[0]]
        for idx in range(1, len(intervals)):
            old_lo, old_hi = answer[-1]
            new_lo, new_hi = intervals[idx]

            # append new range
            if new_lo > old_hi:
                answer.append([new_lo, new_hi])

            # extend existing range
            elif new_hi > old_hi:
                answer[-1][1] = new_hi

        print("answer:", answer)
        return answer

s = Solution()
s.merge([[1,3],[2,6],[8,10],[15,18]])
s.merge([[1,4],[4,5]])