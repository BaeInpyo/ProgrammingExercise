"""
Problem URL: https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/548/week-5-july-29th-july-31st/3405/
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.dynamic_programming(prices)
    
    def dynamic_programming(self, prices):
        if not prices:
            return 0

        n = len(prices)

        """
        All of these kinds of state is from state-transition-diagram
        (https://github.com/BaeInpyo/ProgrammingStudy/blob/master/leetcode/july_challenge/best_time_to_buy_and_sell_stock_with_cooldown/leetcode_309_image_1.pdf)
        have[i] = last state at day i is having stock
            1. buy stock at ith day
            2. bought stock before ith day and do nothing
        nonhave[i] = last state at day i is free, which is enalbed to both
        idle and buying stock
            1. sell stock on (i-1)th day
            2. (i-1)th day was nonhave too and do nothing
        cooldown[i] = sell stock on ith day
            1. sell stock on ith day
        """
        have, nonhave, cooldown = [0]*n, [0]*n, [0]*n
        have[0] = -prices[0]
        for idx in range(1, n):
            have[idx] = max(have[idx-1], nonhave[idx-1] - prices[idx])
            nonhave[idx] = max(nonhave[idx-1], cooldown[idx-1])
            cooldown[idx] = have[idx-1] + prices[idx]
        
        # buy cannot be last state because we pay when buying
        return max(cooldown[n-1], nonhave[n-1])
