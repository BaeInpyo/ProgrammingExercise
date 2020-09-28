"""
Problem URL: https://leetcode.com/problems/count-and-say/
"""

class Solution:
    def countAndSay(self, n: int) -> str:
        countAndSaySequence = "1"   # base string
        for idx in range(n-1):
            countAndSaySequence = self.getCountAndSaySequence(countAndSaySequence)

        return countAndSaySequence

    def getCountAndSaySequence(self, string):
        """ Return count-and-say sequence from given string """
        result = ""
        idx = 0
        while idx < len(string):
            jdx = idx + 1
            while jdx < len(string):
                if string[idx] != string[jdx]:
                    break

                jdx += 1

            count = jdx - idx   # number of consecutive numbers
            number = string[idx]
            result += str(count) + number
            idx = jdx

        return result

s = Solution()
s.countAndSay(3)
