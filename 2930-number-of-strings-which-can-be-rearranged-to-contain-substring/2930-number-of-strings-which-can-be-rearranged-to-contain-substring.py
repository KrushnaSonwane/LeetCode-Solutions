class Solution:
    def stringCount(self, n: int) -> int:
        MOD = 10**9+7
        @cache
        def dfs(i, l, e, t):
            if i == n: 
                return 1 if l == t == 1 and e == 2 else 0
            res = (dfs(i+1, l, e, t) * 23) % MOD
            res = (res +  dfs(i+1, 1, e, t) + dfs(i+1, l, min(2, e + 1), t) + dfs(i+1, l, e, 1)) % MOD
            return res
        return dfs(0, 0, 0, 0)
