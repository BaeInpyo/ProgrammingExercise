"""
Problem link: https://leetcode.com/problems/find-median-from-data-stream/
Use 2 heaps and keep each heap contain balanced number of inputs
"""

import heapq
import math

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minheap = [math.inf]   # dummy which is never picked
        self.maxheap = [math.inf]   # dummy which is never picked

    def addNum(self, num: int) -> None:
        num1, num2 = self.minheap[0], -self.maxheap[0]
        if num > num1:
            heapq.heappush(self.minheap, num)
        else:
            heapq.heappush(self.maxheap, -num)
        
        # balancing heap
        if len(self.minheap) - len(self.maxheap) >= 2:
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
        elif len(self.maxheap) - len(self.minheap) >= 2:
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))

    def findMedian(self) -> float:
        if len(self.minheap) == len(self.maxheap):
            return (self.minheap[0] - self.maxheap[0]) / 2
        elif len(self.minheap) - len(self.maxheap) == 1:
            return self.minheap[0]
        elif len(self.maxheap) - len(self.minheap) == 1:
            return -self.maxheap[0]
        else:
            # maybe balancing was failed...
            return -1
        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()