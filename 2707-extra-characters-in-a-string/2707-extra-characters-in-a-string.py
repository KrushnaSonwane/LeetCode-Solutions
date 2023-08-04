class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        @cache
        def dfs(i):
            if i == len(s): return 0
            res = dfs(i+1) + 1
            for w in dictionary:
                if i+len(w) <= len(s) and s[i: i+len(w)]==w:
                    res = min(res, dfs(i+len(w)))
            return res
        return dfs(0)