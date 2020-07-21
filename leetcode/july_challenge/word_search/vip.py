class Solution:
    def dfs(self, board: List[List[str]], word: str, x: int, y: int, c: int) -> bool:
        if c == len(word):
            return True
        
        if (x < 0 or y < 0 or x >= len(board) or y >= len(board[0]) or board[x][y] != word[c]):
            return False
    
        board[x][y] = '-'
        if (self.dfs(board, word, x+1, y, c+1) or
            self.dfs(board, word, x-1, y, c+1) or
            self.dfs(board, word, x, y+1, c+1) or
            self.dfs(board, word, x, y-1, c+1)):
            return True
        board[x][y] = word[c]
        return False
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, i, j, 0):
                    return True
        return False
