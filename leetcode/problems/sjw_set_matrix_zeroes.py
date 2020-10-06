"""
Problem URL: https://leetcode.com/problems/set-matrix-zeroes/
"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # self.sol1(matrix)
        # self.sol2(matrix)
        self.sol3(matrix)
        

    def sol1(self, matrix):
        """ O(mn) space solution. 85% runtime / 9% space """
        m = len(matrix)
        n = len(matrix[0])
        zeroes = []

        # save zeroes
        for idx in range(m):
            for jdx in range(n):
                if matrix[idx][jdx] == 0:
                    zeroes.append((idx, jdx))

        for (idx, jdx) in zeroes:
            # fill row
            for kdx in range(n):
                matrix[idx][kdx] = 0

            # fill column
            for kdx in range(m):
                matrix[kdx][jdx] = 0

        return # end of function

    def sol2(self, matrix):
        """ O(m+n) space solution. 99% runtime / 9% space """
        m = len(matrix)
        n = len(matrix[0])
        rows = set()
        cols = set()
        
        # save rows and cols which need to be zero
        for idx in range(m):
            for jdx in range(n):
                if matrix[idx][jdx] == 0:
                    rows.add(idx)
                    cols.add(jdx)

        # fill rows
        for row in rows:
            for idx in range(n):
                matrix[row][idx] = 0

        # fill columns
        for col in cols:
            for idx in range(m):
                matrix[idx][col] = 0

        return # end of function

    def sol3(self, matrix):
        """ O(1) space solution. Save each row/col's state at first element. 99% runtime / 9% space """
        m = len(matrix)
        n = len(matrix[0])

        # first row / first column
        first_row, first_col = False, False

        # check first row
        for idx in range(m):
            if matrix[idx][0] == 0:
                first_col = True

        # check first column
        for idx in range(n):
            if matrix[0][idx] == 0:
                first_row = True

        # check except first row and first column
        for idx in range(1, m):
            for jdx in range(1, n):
                if matrix[idx][jdx] == 0:
                    # save row's state at first element
                    matrix[idx][0] = 0 
                    # save col's state at first element
                    matrix[0][jdx] = 0

        # check rows and fill zeroes
        for idx in range(1, m):
            if matrix[idx][0] == 0:
                for jdx in range(n):
                    matrix[idx][jdx] = 0

        # check cols and fill zeroes
        for idx in range(1, n):
            if matrix[0][idx] == 0:
                for jdx in range(m):
                    matrix[jdx][idx] = 0

        # use first_row and first_col
        if first_row:
            for idx in range(n):
                matrix[0][idx] = 0

        if first_col:
            for idx in range(m):
                matrix[idx][0] = 0

        return  # end of function