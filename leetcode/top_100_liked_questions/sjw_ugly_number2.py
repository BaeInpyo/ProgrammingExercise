"""
Problem URL: https://leetcode.com/problems/ugly-number-ii/
"""

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]

        # We compare ugly[two]*2, ugly[three]*3, ugly[five]*5
        two, three, five = 0, 0, 0

        while len(ugly) < n:
            nextUglyNumber = min(ugly[two]*2, ugly[three]*3, ugly[five]*5)
            ugly.append(nextUglyNumber)

            # Use if instead of elif to avoid adding same ugly number multiple
            # times, e.g, 6 = 2*3 = 3*2
            if nextUglyNumber == ugly[two]*2:
                two += 1
            if nextUglyNumber == ugly[three]*3:
                three += 1
            if nextUglyNumber == ugly[five]*5:
                five += 1

        print(ugly)
        return ugly[-1]