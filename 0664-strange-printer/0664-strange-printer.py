class Solution:
    def strangePrinter(self, s: str) -> int:
        @cache
        def dfs(i, j):
            if i==j: return 1
            res = inf
            for k in range(i, j, 1):
                res = min(res, dfs(i, k) + dfs(k+1, j))
            return res - int(s[i]==s[j])
        return dfs(0, len(s)-1)