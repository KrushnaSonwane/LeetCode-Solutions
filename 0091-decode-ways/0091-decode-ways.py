class Solution:
    def numDecodings(self, s: str) -> int:
        hashT = {}
        for i in range(97, 123):
            hashT[(str(i-96))] = chr(i)
        @cache
        def dfs(i):
            if i == len(s): return 1
            res = 0
            if s[i] in hashT:
                res += dfs(i+1)
            if i+1 < len(s) and s[i:i+2] in hashT:
                res += dfs(i+2)
            return res
        return dfs(0)