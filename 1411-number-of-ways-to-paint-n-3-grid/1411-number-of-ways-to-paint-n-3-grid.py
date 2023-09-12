class Solution:
    def numOfWays(self, n: int) -> int:
        s, mod = 'ryg', 10**9+7
        @lru_cache(None)
        def dfs(i, a, b, c):
            if i == n: return 1
            res = 0
            for r in s:
                if r == a: continue
                for y in s:
                    if y in [r, b]: continue
                    for g in s:
                        if g in [y, c]: continue
                        res += dfs(i+1, r, y, g)
                        res %= mod
            return res
        return dfs(0, '', '', '')