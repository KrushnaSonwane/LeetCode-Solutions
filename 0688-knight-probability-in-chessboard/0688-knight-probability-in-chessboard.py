class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        @cache
        def dfs(i, j, k):
            if k == 0:
                return int(0 <= i < n and 0 <= j < n)
            if 0 > i or 0 > j or j >= n or i >= n: return 0
            res = 0
            for x, y in [(i-2,j+1),(i-1,j+2),(i+1,j+2),(i+2,j+1),(i+2,j-1),(i+1,j-2),(i-1,j-2),(i-2,j-1)]:
                res += dfs(x,y,k-1)
            return res
        res = dfs(row, column, k)
        return res / (8**k)