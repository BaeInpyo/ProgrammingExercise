"""
Problem URL: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
"""

import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        n = len(matrix)

        # insert every element in matrix to heap
        for idx in range(n):
            for jdx in range(n):
                heapq.heappush(heap, matrix[idx][jdx])

        # pop k times
        while k > 0:
            value = heapq.heappop(heap)
            k -= 1

        return value