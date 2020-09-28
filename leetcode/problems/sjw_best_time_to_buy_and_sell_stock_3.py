"""
Problem URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # return self.solutionWithState(prices)   # 2004ms
        return self.solutionWithSplit(prices)   # 2360ms

    def solutionWithSplit(self, prices):
        if not prices:
            return 0

        n = len(prices)
        left, right = [0]*n, [0]*n

        # left[i] = max profit done before ith day
        curr_min = prices[0]
        max_profit = 0
        for (idx, price) in enumerate(prices):
            curr_min = min(curr_min, price)
            max_profit = max(max_profit, price - curr_min)
            left[idx] = max_profit

        # right[i] = max profit done after ith day
        curr_max = prices[-1]
        max_profit = 0
        for (idx, price) in reversed(list(enumerate(prices))):
            curr_max = max(curr_max, price)
            max_profit = curr_max - price
            right[idx] = max_profit

        max_profit = 0
        for idx in range(n):
            max_profit = max(max_profit, left[idx], right[idx], left[idx]+right[idx])

        return max_profit


    def solutionWithState(self, prices):
        """ Solution using state machine """
        buy1 = float("-inf")
        sell1 = 0
        buy2 = float("-inf")
        sell2 = 0

        for price in prices:
            buy1 = max(buy1, -price)
            sell1 = max(sell1, buy1 + price)
            buy2 = max(buy2, sell1 - price)
            sell2 = max(sell2, buy2 + price)

        return max(sell1, sell2)