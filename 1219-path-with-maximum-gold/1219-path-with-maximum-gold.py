class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        def dfs(r, c):
            if r in [-1, m] or c in [-1, n] or not grid[r][c]: return 0
            temp, grid[r][c] = grid[r][c], 0
            max_ = max(dfs(r-1,c), dfs(r+1,c), dfs(r,c-1), dfs(r,c+1)) + temp
            grid[r][c] = temp
            return max_
        return max(dfs(i, j) for i in range(m) for j in range(n))