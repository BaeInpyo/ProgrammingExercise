"""
Problem URL: https://leetcode.com/problems/search-in-rotated-sorted-array/
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find pivot
        lo, hi = 0, len(nums)-1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < nums[hi]:
                hi = mid
            else:
                lo = mid + 1

        # lo is pivot
        pivot = lo

        # binary search in range [0, pivot)
        lo, hi = 0, pivot
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid

        # binary search in range [pivot, len(nums))
        lo, hi = pivot, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid

        # target is not found
        return -1