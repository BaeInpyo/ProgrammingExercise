"""
Problem URL: https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/546/week-3-july-15th-july-21st/3397/

1. Stort list of positions for each letter.
2. Start from first character of word, check adjacent letters.
"""

from collections import deque

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True

        # Store starting position of each letter
        start_position = dict()
        for idx in range(len(board)):
            for jdx in range(len(board[idx])):
                letter = board[idx][jdx]
                start_position[letter] = start_position.get(letter, [])
                start_position[letter].append((idx, jdx))

        # Do searching from start position
        for (idx, jdx) in start_position.get(word[0], []):
            # Initialize visited
            visited = []
            for kdx in range(len(board)):
                visited.append([False] * len(board[kdx]))

            # print("Start from:", idx, jdx, word)
            if self.search(board, visited, idx, jdx, 0, word):
                return True

        return False

    def search(self, board, visited, idx, jdx, word_index, word):
        if word[word_index] != board[idx][jdx]:
            return False

        if word_index == len(word)-1:
            # print("End from:", idx, jdx)
            return True

        visited[idx][jdx] = True
        # print("search from:", idx, jdx)
        dirs = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0),
        ]

        for (didx, djdx) in dirs:
            next_idx, next_jdx = idx+didx, jdx+djdx
            # print("next is:", next_idx, next_jdx)
            if 0 <= next_idx < len(board) \
                and 0 <= next_jdx < len(board[idx]) \
                and not visited[next_idx][next_jdx] \
                and self.search(
                    board, visited, next_idx, next_jdx, word_index+1, word):
                return True

        # print("go back from:", idx, jdx)
        visited[idx][jdx] = False
        return False