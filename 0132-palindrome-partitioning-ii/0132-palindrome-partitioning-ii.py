class Solution:
    def minCut(self, s: str) -> int:
        dp = [[False for _ in s] for _ in s]
        def solve(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                dp[i][j] = True
                i -= 1
                j += 1
        dp[-1][-1] = True

        for i in range(len(s)-1):
            solve(i, i)
            solve(i, i+1)
        
        @cache
        def dfs(i, j):
            if i == len(s):
                return 0
            if j == len(s): return inf
            res = dfs(i, j+1)
            if dp[i][j]:
                res = min(res, 1 + dfs(j+1, j+1))
            return res
        return dfs(0, 0)-1