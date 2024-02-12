class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        A = set(wordDict)
        @cache
        def dfs(i):
            if i == len(s): return True
            res = False
            for j in range(i, min(len(s), i + 20)):
                if s[i: j+1] in A:
                    res = res or dfs(j+1)
            return res
        res = dfs(0)
        return res