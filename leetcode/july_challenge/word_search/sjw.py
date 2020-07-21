"""
Problem URL: https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/546/week-3-july-15th-july-21st/3397/

Do DFS search from all positions
"""

from collections import deque

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.m = len(board)
        self.n = len(board[0])
        self.board = board
        self.word = word
        self.dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # (right, down, left, up)

        for idx in range(self.m):
            for jdx in range(self.n):
                if self.dfs(idx, jdx, 0):
                    return True

        return False

    def dfs(self, idx, jdx, wdx):
        """ Do dfs from (idx, jdx) and return if word[wdx:] is feasible """
        # Complete word is made
        if wdx == len(self.word):
            return True

        # If (idx, jdx) is out of board, return False
        if not (0 <= idx < self.m) or not (0 <= jdx < self.n):
            return False

        # If current position does not match word, return False
        if self.board[idx][jdx] != self.word[wdx]:
            return False

        # This is equivalent with remaining "visited" matrix
        letter = self.board[idx][jdx]
        self.board[idx][jdx] = "#"
        for (dx, dy) in self.dirs:
            if self.dfs(idx+dx, jdx+dy, wdx+1):
                return True

        # Recover board
        self.board[idx][jdx] = letter
        return False