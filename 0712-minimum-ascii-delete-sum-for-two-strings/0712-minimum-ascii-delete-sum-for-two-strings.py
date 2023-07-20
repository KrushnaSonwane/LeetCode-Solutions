class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        def getSum(r, s):
            return sum(ord(s[k]) for k in range(r, len(s)))
        dp = {}
        def dfs(i, j):
            if (i, j) not in dp:
                if i == len(s1): return getSum(j, s2)
                if j == len(s2): return getSum(i, s1)
                if s1[i] == s2[j]: dp[(i,j)] = dfs(i+1,j+1)
                else: dp[(i,j)] = min(dfs(i+1,j) + ord(s1[i]), dfs(i,j+1) + ord(s2[j]))
            return dp[(i, j)]
        return dfs(0,0)