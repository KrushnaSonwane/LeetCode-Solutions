class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9+7
        @cache
        def dfs(i, up, down):
            if i == n: 
                return 1 if up == down == 0 else 0
            if i > n: return 0
            if up == 2 or down == 2: return 0
            res = 0
            if up == 0:
                if down == 0:
                    res = dfs(i+2, 0, 0) + dfs(i+2, 1, 0) + dfs(i+2, 0, 1) + dfs(i+1, 0, 0)
                elif down == 1:
                    res = dfs(i+1, 0, 0) + dfs(i+1, 1, 0)
            elif up == 1:
                if down == 0:
                    res = dfs(i+1, 0, 0) + dfs(i+1, 0, 1)
                elif down == 1:
                    res = dfs(i+1, 0, 0) + dfs(i+1, 0, 1) + dfs(i+1, 1, 0)
            return res % MOD
        return dfs(0, 0, 0)