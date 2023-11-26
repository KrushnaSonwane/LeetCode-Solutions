class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        @cache
        def dfs(i, free):
            if i == len(prices): return 0
            res = dfs(i+1, i+1) + prices[i]
            if free:
                res = min(res, dfs(i+1, free-1))
            return res
        return dfs(0, 0)
                