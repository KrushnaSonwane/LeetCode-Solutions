class Solution:
    def countVowelStrings(self, n: int) -> int:
        @lru_cache(None)
        def dfs(i, last):
            if i == n: return 1
            return sum(dfs(i+1, ch) for ch in 'aeiou' if last <= ch)
        return dfs(0, 'a')