"""
Problem URL: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3353/
"""
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}  # key(amount, index), value: # of combinations
        """
        cache[(amount, index)] = cache[(amount, index-1)] + cache[(amount-coins[index], index)]
        """

        # init cache
        for amt in range(amount+1):
            cache[(amt, 0)] = 0
        for idx in range(len(coins)+1):
            cache[(0, idx)] = 1
        

        for amt in range(1, amount+1):
            for idx in range(1, len(coins)+1):
                if amt >= coins[idx-1]:
                    cache[(amt, idx)] = cache[(amt, idx-1)] + cache[(amt-coins[idx-1], idx)]
                else:
                    cache[(amt, idx)] = cache[(amt, idx-1)]

        # print(cache)
        return cache[(amount, len(coins))]