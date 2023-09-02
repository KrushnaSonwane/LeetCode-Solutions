class Solution:
    def minExtraChar(self, s: str, d: List[str]) -> int:
        A = set(d)
        @lru_cache(None)
        def dfs(i):
            if i == len(s): return 0
            res = 1 + dfs(i+1)
            for j in range(i, len(s)):
                if s[i: j+1] in A:
                    res = min(res, dfs(j+1))
            return res
        return dfs(0)