"""
Problem URL: https://leetcode.com/problems/spiral-matrix/
"""

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
            
        m, n = len(matrix), len(matrix[0])
        left = (0, -1)
        right = (0, 1)
        top = (-1, 0)
        bottom = (1, 0)
        next_ = {
            right: bottom,
            bottom: left,
            left: top,
            top: right
        }

        answer = []
        x, y = 0, 0
        curr_direction = right
        while True:
            answer.append(matrix[x][y])
            matrix[x][y] = "#"  # mark as visited
            dx1, dy1 = curr_direction
            next_direction = next_[curr_direction]
            dx2, dy2 = next_direction

            # check current direction
            if 0 <= x+dx1 < m and 0 <= y+dy1 < n and matrix[x+dx1][y+dy1] != "#":
                x, y = x+dx1, y+dy1

            # check next direction
            elif 0 <= x+dx2 < m and 0 <= y+dy2 < n and matrix[x+dx2][y+dy2] != "#":
                x, y = x+dx2, y+dy2
                curr_direction = next_direction

            # terminate search
            else:
                break

        return answer

s = Solution()
print(s.spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]))
print(s.spiralOrder([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]))
#print(s.spiralOrder())
