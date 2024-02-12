class Solution:
    def numDecodings(self, s: str) -> int:
        hashT = {str(num) for num in range(1, 27)}
        @lru_cache(None)
        def dfs(i):
            if i == len(s): return 1
            if s[i] == '0': return 0
            res = dfs(i + 1)
            if i + 1 < len(s) and s[i: i + 2] in hashT:
                res += dfs(i + 2)
            return res
        return dfs(0)