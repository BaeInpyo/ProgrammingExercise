"""
Problem URL: https://leetcode.com/problems/word-search/
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        for idx in range(m):
            for jdx in range(n):
                if self.search(board, idx, jdx, word, 0):
                    return True

        return False

    def search(self, board, idx, jdx, word, widx):
        """Return if word[widx:] is found from board[idx][jdx]"""
        # end of word found
        if widx == len(word):
            return True

        # out of board
        m, n = len(board), len(board[0])
        if not (0 <= idx  < m and 0 <= jdx < n):
            return False

        # first alphabet is different
        if board[idx][jdx] != word[widx]:
            return False

        # mark boad[idx][jdx] as visited
        origin = board[idx][jdx]
        board[idx][jdx] = "#"

        # down, right, up, left
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        for (dx, dy) in directions:
            if self.search(board, idx+dx, jdx+dy, word, widx+1):
                board[idx][jdx] = origin
                return True

        # cannot search from all directions
        board[idx][jdx] = origin
        return False