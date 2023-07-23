class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        mod = 10**9+7
        @cache
        def dfs(sum_, count):
            if sum_ == 0: return 1
            if count**x > sum_: return 0
            res = dfs(sum_, count+1)
            res += dfs(sum_ - count**x, count+1)
            return res
        return dfs(n, 1) % mod