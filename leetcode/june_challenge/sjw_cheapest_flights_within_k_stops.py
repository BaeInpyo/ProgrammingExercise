"""
Problem URL: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3360/
"""

import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        # initialize graph
        graph = dict()
        for u in range(n):
            graph[u] = dict()

        for (u, v, w) in flights:
            graph[u][v] = w

        heap = [(0, src, K+1)]  # (distance, curr_node, remain_stops)
        while heap:
            dist, curr_node, remain = heapq.heappop(heap)
            if curr_node == dst:
                return dist
            if remain > 0 :
                for next_node in graph[curr_node]:
                    heapq.heappush(heap, (dist+graph[curr_node][next_node], next_node, remain-1))

        return -1