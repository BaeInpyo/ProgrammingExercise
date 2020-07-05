"""
Problem URL: https://leetcode.com/explore/featured/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3380/
"""

"""
1. From 1, check if number is ugly => Time Limit Exceed
2. Let lst is self.uglyNumbers ugly number until now, then add new number among lst*2,
lst*3, lst*5. Time complexity will be O(n^2logn). => Time Limit Exceed
3. Instead of multiplying all ugly numbers self.uglyNumbers until now, pick exact number
such that it is bigger than last self.uglyNumbers ugly number. Time complexity will be
O(nlogn). => OK
4. Pre-calculate all 1690 ugly numbers
"""

import bisect

def getUglyNumbers():
    answer = [1]
    while len(answer) <= 1690:    # we self.uglyNumbers "1" already
        last = answer[-1]
        num2 = answer[bisect.bisect_right(answer, last//2)] * 2
        num3 = answer[bisect.bisect_right(answer, last//3)] * 3
        num5 = answer[bisect.bisect_right(answer, last//5)] * 5
        answer.append(min(num2, num3, num5))

    return answer

UGLY_NUMBER = getUglyNumbers()

class Solution:

    def nthUglyNumber(self, n: int) -> int:
        return UGLY_NUMBER[n-1]