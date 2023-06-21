class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = {}
        def dfs(i, j):
            if (i, j) not in dp:
                if j == n: return m - i
                if i == m: return n - j
                if word1[i] == word2[j]:
                    res = dfs(i + 1, j + 1)
                else:
                    res = min(dfs(i, j + 1), dfs(i + 1, j), dfs(i + 1, j + 1)) + 1
                dp[(i, j)] = res
            return dp[(i, j)]
        return dfs(0, 0)
