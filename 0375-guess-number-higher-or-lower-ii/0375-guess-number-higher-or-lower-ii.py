class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @cache
        def dfs(l, r):
            if l >= r: return 0
            res = inf
            for i in range(l, r+1):
                res = min(res, max(dfs(l, i-1), dfs(i+1, r)) + i)
            return res
        return dfs(1, n)