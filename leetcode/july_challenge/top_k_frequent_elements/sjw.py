"""
Problem URL: https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/546/week-3-july-15th-july-21st/3393/

Since build heap is O(n), we can utilize building heap
"""

import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = dict()
        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1

        heap = (-count, num) for (num, count) in count_dict.items()
        heapq.heapify(heap)
        answer = []
        for _ in range(k):
            _, num = heapq.heappop(heap)
            answer.append(num)

        return answer