class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        @cache
        def dfs(i, sum_):
            if i == len(rods):
                return 0 if sum_ == 0 else -inf
            res = dfs(i + 1, sum_)
            res = max(res, rods[i] + dfs(i + 1, sum_ + rods[i]))
            res = max(res, dfs(i + 1, sum_ - rods[i]))
            return res
        return dfs(0, 0)