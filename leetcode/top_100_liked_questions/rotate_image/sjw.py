"""
Problem URL: https://leetcode.com/problems/rotate-image/
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        matrix[:] = [[row[k] for row in matrix][::-1] for k in range(n)]
        return