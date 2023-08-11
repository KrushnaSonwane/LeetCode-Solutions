class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @lru_cache(None)
        def dfs(i, sum_):
            if sum_ == 0: return 1
            if i == len(coins): return 0
            res = dfs(i+1, sum_) + (dfs(i, sum_-coins[i]) if coins[i] <= sum_ else 0)
            return res
        return dfs(0, amount)