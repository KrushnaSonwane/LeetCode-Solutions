class Solution:
    def longestIncreasingPath(self, A: List[List[int]]) -> int:
        m, n, dp = len(A), len(A[0]), {}
        def dfs(i, j):
            if (i, j) not in dp:
                res = 1
                for x, y in [(i+1,j), (i-1,j), (i,j-1), (i,j+1)]:
                    if x in [-1, m] or y in [-1, n] or A[i][j] >= A[x][y]: continue
                    res = max(res, dfs(x, y) + 1)
                dp[(i, j)] = res
            return dp[(i, j)]
        return max(dfs(r,c) for r in range(m) for c in range(n))