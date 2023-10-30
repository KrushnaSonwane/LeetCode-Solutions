class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def dfs(x, y):
            if x == len(word1):
                return len(word2) - y
            if y == len(word2):
                return len(word1) - x
            if word1[x] == word2[y]:
                res = dfs(x + 1, y + 1)
            else:
                res = min(dfs(x, y+1), dfs(x+1, y), dfs(x+1, y+1)) + 1
            return res
        return dfs(0, 0)