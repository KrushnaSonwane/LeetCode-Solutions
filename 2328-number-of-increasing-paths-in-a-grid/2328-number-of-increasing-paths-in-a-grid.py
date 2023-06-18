class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        @cache
        def dfs(i, j):
            if i in [-1, m] or j in [-1, n]: return 0
            res = 1
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if x in [-1, m] or y in [-1, n] or grid[x][y] <= grid[i][j]: continue
                res += dfs(x, y)
            return res
        ans = 0
        for r in range(m):
            for c in range(n):
                ans += dfs(r, c)
        return ans % 1000000007