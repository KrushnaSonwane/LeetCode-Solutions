class Solution:
    def totalNQueens(self, n: int) -> int:
        self.res = 0
        queen = [['.' for _ in range(n)] for _ in range(n)]
        def isValid(r, c, grid):
            for i in range(n):
                if grid[r][i] == 'Q': return False
                if grid[i][c] == 'Q': return False
            queue = [[r, c, 1],[r, c, 2],[r, c, 3],[r, c, 4]]
            while queue:
                rr, cc, val = queue.pop(0)
                if grid[rr][cc] == 'Q': return False
                if val == 1:
                    if rr + 1 != n and cc + 1 != n:
                        queue.append([rr + 1, cc + 1, 1])
                if val == 2:
                    if rr - 1 != -1 and cc - 1 != -1:
                        queue.append([rr - 1, cc - 1, 2])
                if val == 3:
                    if rr + 1 != n and cc - 1 != -1:
                        queue.append([rr + 1, cc - 1, 3])
                if val == 4:
                    if rr - 1 != -1 and cc + 1 != n:
                        queue.append([rr - 1, cc + 1, 4])
            return True


        def dfs(i, okay):
            if i == n:
                self.res += 1
                return
            for j in range(n):
                if isValid(i, j, okay.copy()):
                    okay[i][j] = "Q"
                    dfs(i + 1, okay.copy())
                    okay[i][j] = '.'
        dfs(0 , queen)
        return self.res