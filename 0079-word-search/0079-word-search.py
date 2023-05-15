class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k, board):
            if k == len(word): 
                return True
            if i == m or j == n or j == -1 or i == -1:
                return False 
            if board[i][j] != word[k] or board[i][j] == '*': 
                return False
            temp = board[i][j]
            board[i][j] = '*'
            first = dfs(i + 1, j, k + 1, board)
            second = dfs(i - 1, j, k + 1, board)
            third = dfs(i, j + 1, k + 1, board)
            fourth = dfs(i, j - 1, k + 1, board)
            board[i][j] = temp
            return first or second or third or fourth
        m, n = len(board), len(board[0])
        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]:
                    res = dfs(r, c, 0, board.copy())
                    if res: return 1
        return 0