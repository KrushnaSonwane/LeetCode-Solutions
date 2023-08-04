class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def dfs(i):
            if i == len(s): return 1
            res = False
            for w in wordDict:
                if i + len(w) <= len(s) and s[i: i+len(w)]==w:
                    res = res or dfs(i+len(w))
            return res
        return dfs(0)