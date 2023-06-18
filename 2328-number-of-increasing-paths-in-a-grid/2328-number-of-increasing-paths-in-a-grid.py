class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        dp = {}
        m, n = len(grid), len(grid[0])
        def dfs(i, j):
            if i in [-1, m] or j in [-1, n]: return 0
            if (i, j) not in dp:
                res = 1
                for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if x in [-1, m] or y in [-1, n] or grid[x][y] <= grid[i][j]: continue
                    res += dfs(x, y)
                dp[(i, j)] = res
            return dp[(i, j)]
        ans = 0
        for r in range(m):
            for c in range(n):
                ans += dfs(r, c)
        return ans % 1000000007