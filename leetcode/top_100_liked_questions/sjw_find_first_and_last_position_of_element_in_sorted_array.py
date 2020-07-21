"""
Problem URL: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

1. Use python built in module, bisect
2. Since every num is integer, find position of target-e, target+e where e is
small (less than 1) floating number => This does not work if target doest not
exist in nums
3. General algorithm such that find with log scale
"""
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Normal binary search와 똑같이 하되, 만약 nums[mid]가 target이면 기록 후에
        더 좁은 범위에 대해서 binary search 다시 시작
        """
        first, last = -1, -1

        # search first occurence
        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1

            if nums[mid] == target:
                first = mid

        # search last occurence
        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1

            if nums[mid] == target:
                last = mid

        print(first, last)
        return [first, last]

s = Solution()
s.searchRange([1,2,3,3], 1)
s.searchRange([1,2,3,3], 2)
s.searchRange([1,2,3,3], 3)
s.searchRange([1], 1)
s.searchRange([1,1,1,1,1], 1)