class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        @cache
        def dfs(i, f, l):
            if i == len(words): return 0
            res = float("inf")
            s = words[i]
            
            if f == s[-1]:
                res = min(res, (len(s) - 1) + dfs(i + 1, s[0], l))
            if l == s[0]:
                res = min(res, (len(s) - 1) + dfs(i + 1, f, s[-1]))
            res = min(res, len(s) + dfs(i + 1, f, s[-1]))
            res = min(res, len(s) + dfs(i+1, s[0], l))
            return res
        return dfs(1, words[0][0], words[0][-1]) + len(words[0])
        
            