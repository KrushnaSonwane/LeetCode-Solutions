class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        @cache
        def dfs(i, j):
            if i == n: return 0
            res = inf
            for x in [j-1, j, j+1]:
                if x >= 0 and x < n:
                    res = min(res, dfs(i+1, x) + matrix[i][x])
            return res
        res = inf
        for i in range(n):
            res = min(res, dfs(0, i))
        return res