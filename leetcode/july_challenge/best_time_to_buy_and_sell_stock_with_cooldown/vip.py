class Solution:
    '''
    dp = None
    def maxProfitInternal(self, prices, day, buy_date):
        if day >= len(prices):
            return 0
        
        if self.dp[day][buy_date] >= 0:
            return self.dp[day][buy_date]
        
        result = self.maxProfitInternal(prices, day+1, buy_date)
        if buy_date < len(prices):
            profit = prices[day] - prices[buy_date]
            if profit > 0:
                result = max(result, self.maxProfitInternal(prices, day+2, len(prices)) + profit)
        else:
            result = max(result, self.maxProfitInternal(prices, day+1, day))
            
        self.dp[day][buy_date] = result
        return result
        
    def maxProfit(self, prices: List[int]) -> int:
        self.dp = [[-1 for _ in range(len(prices) + 1)] for _ in range(len(prices))]
        return self.maxProfitInternal(prices, 0, len(prices))
    '''
    '''
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        prev_profit = 0
        curr_profit = 0
        day = 1
        start = 0
        end = 0
        while day < len(prices) and prices[day-1] > prices[day]:
            start = end = day
            day += 1
    
        while day < len(prices):
            while day < len(prices) and prices[day-1] <= prices[day]:
                end = day
                day += 1
            
            prev_profit = prices[end-1] - prices[start]
            curr_profit = prices[end] - prices[start]
            
            while day < len(prices) and prices[day-1] > prices[day]:
                start = day
                day += 1
            
            if day >= len(prices):
                total_profit += curr_profit
                break
        
            if start > end + 1:
                total_profit += curr_profit
            elif start == end + 1:
                profit0 = prices[start + 1] - prices[start]
                profit1 = prices[end] - prices[end - 1]
                profit2 = prices[start + 1] - prices[end - 1]
                
                max_profit = sorted([profit0, profit1, profit2])[2]
                if max_profit == profit0:
                    total_profit += prev_profit
                elif max_profit == profit1:
                    total_profit += curr_profit
                    start += 1
                else:
                    total_profit += max_profit
                    start += 1
        
        return total_profit
    '''
    dp = None
    def maxProfitInternal(self, prices, day):
        start_day = day
        if day >= len(prices) - 1:
            return 0
        
        if self.dp[day] >= 0:
            return self.dp[day]
        
        start = end = day
        while day < len(prices) - 1 and prices[day] > prices[day+1]:
            day += 1
        start = day
        
        while day < len(prices) - 1 and prices[day] <= prices[day+1]:
            day += 1
        end = day

        profit = 0
        profit0 = prices[end] - prices[start]
        profit1 = prices[end - 1] - prices[start]
        while day < len(prices) - 1 and prices[day] > prices[day+1]:
            day += 1
        profit1 = max(profit1, prices[day] - prices[start])
        
        if day == end + 1:
            profit0 += self.maxProfitInternal(prices, day+1)
            profit1 += self.maxProfitInternal(prices, day)
            profit = max(profit0, profit1)
        else:
            profit = profit0 + self.maxProfitInternal(prices, day)
            
        self.dp[start_day] = profit
        return profit
        
    def maxProfit(self, prices: List[int]) -> int:
        self.dp = [-1 for _ in range(len(prices))]
        
        start = 0
        while start < len(prices) - 1 and prices[start] > prices[start + 1]:
            start += 1

        return self.maxProfitInternal(prices, start)
