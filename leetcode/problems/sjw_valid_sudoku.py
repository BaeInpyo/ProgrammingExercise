"""
Problem URL: https://leetcode.com/problems/valid-sudoku/
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Rule1: Each row must contain the digits 1-9 without repetition
        for idx in range(9):
            row = [x for x in board[idx] if x != "."]
            if len(set(row)) != len(row):
                return False

        # Rule2: Each column must contain the digits 1-9 without repetition
        for idx in range(9):
            col = [board[row][idx] for row in range(9) if board[row][idx] != "."]
            if len(set(col)) != len(col):
                return False

        # Rule3: Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition
        for idx in range(0, 9, 3):
            for jdx in range(0, 9, 3):
                # (idx, jdx) is top left corner of (3x3) box
                box = [board[row][col] for row in range(idx, idx+3) for col in range(jdx, jdx+3)]
                box = [x for x in box if x != "."]
                if len(set(box)) != len(box):
                    return False

        return True