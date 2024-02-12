class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dfs(i, sum_):
            if sum_ == 0: return 0
            if i == len(coins): return inf
            res = dfs(i+1, sum_)
            if coins[i] <= sum_:
                res = min(res, dfs(i, sum_ - coins[i]) + 1)
            return res
        res = dfs(0, amount)
        return -1 if res == inf else res