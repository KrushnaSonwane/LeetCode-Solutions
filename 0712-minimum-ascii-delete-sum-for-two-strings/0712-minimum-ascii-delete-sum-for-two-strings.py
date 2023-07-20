class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        def getSum(r, s):
            return sum(ord(s[k]) for k in range(r, len(s)))
        @cache
        def dfs(i, j):
            if i == len(s1): return getSum(j, s2)
            if j == len(s2): return getSum(i, s1)
            if s1[i] == s2[j]: return dfs(i+1,j+1)
            return min(dfs(i+1,j) + ord(s1[i]), dfs(i,j+1) + ord(s2[j]))
        return dfs(0,0)