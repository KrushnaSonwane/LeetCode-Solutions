class Solution:
    def distinctSequences(self, n: int) -> int:
        MOD = 10**9+7
        @lru_cache(None)
        def dfs(i, a, b):
            if i == n: return 1
            res = 0
            for num in range(1, 7):
                if gcd(num, a) == 1 and num not in [a, b]:
                    res += dfs(i+1, num, a)
            res %= MOD
            return res
        res = 0
        for num in range(1, 7):
            res += dfs(1, num, -1)
            res %= MOD
        return res