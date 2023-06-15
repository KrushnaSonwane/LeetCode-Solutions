class Solution:
    def maxProduct(self, s: str) -> int:
        @cache
        def dfs(i, a, b):
            if i == len(s):
                if a == a[::-1] and b == b[::-1]:
                    self.res = max(self.res, len(b) * len(a))
                return
            dfs(i + 1, a, b)
            dfs(i + 1, a + s[i], b)
            dfs(i + 1, a, b + s[i])
        self.res = 0
        dfs(0, '', '')
        return self.res