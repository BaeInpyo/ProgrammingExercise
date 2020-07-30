"""
Problem URL: https://leetcode.com/explore/featured/card/july-leetcoding-challenge/548/week-5-july-29th-july-31st/3406/
"""

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.s = s
        self.wordDict = set(wordDict)
        dp = dict()
        self.dp(0, dp)
        return dp[0]

    def dp(self, idx: int, dp: dict) -> None:
        """Fill dp"""
        if idx >= len(self.s):
            return [""]

        if idx in dp:
            return dp[idx]

        answer = []
        for jdx in range(idx+1, len(self.s)+1):
            curr = self.s[idx:jdx]
            if curr in self.wordDict:
                sentences = [curr + " " + word if word else curr for word in self.dp(jdx, dp)]
                answer.extend(sentences)

        # fill dp
        dp[idx] = answer
        return answer

# s = Solution()
# s.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])
# s.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"])
# s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])
# s.wordBreak("aaaaa", ["a","aa","aaa"])