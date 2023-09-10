class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        res = [inf]
        empty, full = [], []
        for i in range(3):
            for j in range(3):
                if grid[i][j] > 1: 
                    full.append((i, j))
                elif grid[i][j] == 0:
                    empty.append((i, j))
        
        def isValid(A):
            return not any(False for i in range(3) for j in range(3) if A[i][j] == 0)

        def dfs(i, count):
            if i == len(full):
                if isValid(grid.copy()):
                    res[0] = min(res[0], count)
                return
            xx, yy = full[i]
            if grid[xx][yy] > 1:
                for x, y in empty:
                    if grid[x][y] == 0:
                        grid[x][y] = 1
                        grid[xx][yy] -= 1
                        dfs(i, count+abs(xx-x)+abs(yy-y))
                        grid[x][y] = 0
                        grid[xx][yy] += 1
            else:
                dfs(i+1, count)
        dfs(0, 0)
        return 0 if res[0] == inf else res[0]