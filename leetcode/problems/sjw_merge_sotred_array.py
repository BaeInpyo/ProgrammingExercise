"""
Problem URL: https://leetcode.com/problems/merge-sorted-array/
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # self.sol1(nums1, m, nums2, n)
        self.sol2(nums1, m, nums2, n)
        

    def sol1(self, nums1, m, nums2, n):
        """ Naive solution which uses O(m+n) space. """
        left, right = 0, 0
        merged = [None] * (m+n)
        while left < m and right < n:
            if nums1[left] < nums2[right]:
                merged[left+right] = nums1[left]
                left += 1
            else:
                merged[left+right] = nums2[right]
                right += 1

        if left == m:
            while right < n:
                merged[left+right] = nums2[right]
                right += 1
        else:
            while left < m:
                merged[left+right] = nums1[left]
                left += 1

        for idx in range(m+n):
            nums1[idx] = merged[idx]

        return  # end of function

    def sol2(self, nums1, m, nums2, n):
        """ O(1) additional space solution. """
        idx, jdx, kdx = m-1, n-1, m+n-1

        while idx >= 0 and jdx >= 0:
            if nums1[idx] > nums2[jdx]:
                nums1[kdx] = nums1[idx]
                idx -= 1
                kdx -= 1
            else:
                nums1[kdx] = nums2[jdx]
                jdx -= 1
                kdx -= 1

        if idx <= 0:
            # move all numbers in nums2 to nums1
            while jdx >= 0:
                nums1[kdx] = nums2[jdx]
                jdx -= 1
                kdx -= 1

        return  # end of function