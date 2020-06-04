"""
Problem URL: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3349/

Try1: Use diffs list
1. Sort costs by diff between cost[i][0] and cost[i][1] in descending order
2. Now we can select from front in a way that pick smaller one if possible
3. Since costs are sorted by diff between 2 costs, this ensures the minimum

"""

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        diffs = [(abs(costs[i][0] - costs[i][1]), i) for i in range(len(costs))]
        diffs.sort(reverse=True)
        total_cost = 0
        count_a, count_b = 0, 0
        for didx, (_, cidx) in enumerate(diffs):
            cost_a, cost_b = costs[cidx]
            if cost_a < cost_b and count_a < n:
                # pick a
                total_cost += cost_a
                count_a += 1
            elif cost_a < cost_b and count_a >= n:
                # pick b
                total_cost += cost_b
                count_b += 1
            elif cost_a >= cost_b and count_b < n:
                # pick b
                total_cost += cost_b
                count_b += 1
            elif cost_a >= cost_b and count_b >= n:
                # pick a
                total_cost += cost_a
                count_a += 1

        return total_cost