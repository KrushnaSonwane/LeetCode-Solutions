class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        @cache
        def dfs(i):
            if i == len(s): return 0
            res = dfs(i+1)
            for j in range(i, len(s)):
                ch = s[i:j+1]
                if j-i+1 >= k and ch == ch[::-1]:
                    res = max(res, dfs(j+1) +1)
                    break
            return res
        return dfs(0)