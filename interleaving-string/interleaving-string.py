class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2): return False
        @cache
        def dfs(i, j, k):
            if k == len(s3): return True
            res = False
            if i < len(s1) and s1[i] == s3[k]:
                res = dfs(i+1, j, k+1)
            if len(s2) > j and s2[j] == s3[k]:
                res = res or dfs(i, j+1, k+1)
            return res
        return dfs(0, 0, 0)