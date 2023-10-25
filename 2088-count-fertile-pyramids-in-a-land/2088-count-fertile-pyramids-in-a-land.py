class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:
        def dfs(A):
            m, n, ans = len(A), len(A[0]), 0
            res = [[A[i][j] for j in range(n)] for i in range(m)]
            for i in range(m):
                for j in range(n):
                    if A[i][j] and i - 1 >= 0 and j - 1 >= 0 and j + 1 < n:
                        res[i][j] += min(res[i-1][j], res[i-1][j-1], res[i-1][j+1])
                        ans += res[i][j] - 1
            return ans
        return dfs(grid) + dfs(grid[::-1])