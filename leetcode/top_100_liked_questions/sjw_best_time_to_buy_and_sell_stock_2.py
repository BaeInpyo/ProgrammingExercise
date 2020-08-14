"""
Problem URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # add dummy to start and end of prices
        prices = [prices[0]+1] + prices + [prices[-1]-1]
        profit = 0
        
        # buy stock at lowest prices
        idx = 0
        while idx < len(prices)-1:
            while idx < len(prices) -1 and prices[idx] >= prices[idx+1]:
                idx += 1

            print("buy:", prices[idx])
            profit -= prices[idx]
            idx += 1

        # sell stock at highest prices
        idx = 0
        while idx < len(prices)-1:
            while idx < len(prices) -1 and prices[idx] <= prices[idx+1]:
                idx += 1

            print("sell:", prices[idx])
            profit += prices[idx]
            idx += 1

        return profit