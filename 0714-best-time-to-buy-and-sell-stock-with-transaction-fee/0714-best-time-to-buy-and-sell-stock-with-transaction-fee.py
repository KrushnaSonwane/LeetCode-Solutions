class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @cache
        def dfs(i, f):
            if i == len(prices): return 0
            res = dfs(i + 1, f)
            if f:
                res = max(res, dfs(i + 1, False) - prices[i])
            else:
                res = max(res, (prices[i] - fee) + dfs(i + 1, True))
            return res
        return dfs(0, 1)