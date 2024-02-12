class Solution:
    def change(self, amount: int, A: List[int]) -> int:
        @cache
        def dfs(i, sum_):
            if sum_ == 0: return 1
            if i == len(A): return 0
            res = dfs(i+1, sum_)
            if A[i] <= sum_:
                res += dfs(i, sum_ - A[i])
            return res
        return dfs(0, amount)