class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @cache
        def dfs(i, j, k):
            if i == len(s1) and j == len(s2) and k == len(s3): return 1
            if k == len(s3): return 0
            if i == len(s1) and j == len(s2): return 0
            res = 0
            if len(s1) > i and s1[i]==s3[k]:
                res = res or dfs(i+1, j, k+1)
            if len(s2) > j and s2[j]==s3[k]:
                res = res or dfs(i, j+1, k+1)
            return res
        return dfs(0, 0, 0)