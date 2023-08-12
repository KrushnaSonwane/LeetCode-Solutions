class Solution:
    def uniquePathsWithObstacles(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        @lru_cache(None)
        def dfs(i, j):
            if i in [-1, m] or j in [-1, n] or A[i][j]: return 0
            if i == m-1 and j == n-1: return 1
            return dfs(i+1, j) + dfs(i, j+1)
        return dfs(0, 0)