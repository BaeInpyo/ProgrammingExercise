"""
Problem URL: https://leetcode.com/problems/longest-palindromic-substring/

Approach 1: add space padding to original string
- add space padding sothat legnth should be 2n-1
- every 2n-1 positions can be central of palindrome
- time complexity would be O(n^2)

Approach 2: dynamic programming
pd(start, end) is
- if s[start] == s[end], s[start] + pd(start+1, end-1) + s[end]
- else longer one among pd(start+1, end), pd(start, end-1)
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # return self.pd_iter(s)  # 3880ms
        return self.pd_dp(s)    # 6416ms

    def pd_iter(self, s):
        s = " ".join([char for char in s])  # add space padding

        longest_palindrome = ""
        for center in range(len(s)):
            dist = 0
            while center-dist >= 0 and center+dist < len(s):
                # if left and right character is same, go further
                if s[center-dist] == s[center+dist]:
                    dist += 1
                # else stop searching
                else:
                    break

            # compare current one with longest one
            curr_palindrome = s[center-dist+1 : center+dist].replace(" ", "")
            if len(curr_palindrome) > len(longest_palindrome):
                longest_palindrome = curr_palindrome

        return longest_palindrome

    def pd_dp(self, s):
        if not s:
            return ""
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        # string with length 1 is palindrome
        for idx in range(n):
            dp[idx][idx] = True


        max_pd_start = 0   # start index of longest palindrome
        max_length = 1  # lenfth of longest palindrome
        # fill dp table
        for diff in range(1, n):
            for start in range(n-diff):
                end = start+diff
                curr_length = 0
                if s[start] == s[end]:
                    if start+1 == end:
                        dp[start][end] = True
                    else:
                        dp[start][end] = dp[start+1][end-1]
                    curr_length = max(curr_length, diff+1)
                    # print("same, set:", start, end, "->", dp[start][end])
                else:
                    # candidate1 = dp[start+1][end]
                    # candidate2 = dp[start][end-1]
                    dp[start][end] = False
                    # print("diff, set:", start, end, "->", dp[start][end])

                if dp[start][end] and curr_length > max_length:
                    max_pd_start = start
                    max_length = curr_length

        # print("dp size:", len(dp), len(dp[0]))
        # print("start, length:", max_pd_start, max_length)
        return s[max_pd_start : max_pd_start+max_length]