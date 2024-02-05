class Solution:
    def wordPatternMatch(self, p: str, s: str) -> bool:
        def dfs(i, j, A, C):
            if i == len(p):
                return j == len(s)
            if len(s) == i: return False
            res = False
            B = A.copy()
            D = C.copy()
            if p[i] in B :
                if s[j:].startswith(B[p[i]]):
                    res = res or dfs(i+1, j + len(A[p[i]]), B.copy(), D.copy())
            else:
                for k in range(j, len(s)):
                    if s[j: k+1] not in D:
                        D.add(s[j: k+1])
                        B[p[i]] = s[j: k+1]
                        res = res or dfs(i+1, k + 1, B.copy(), D.copy())
                        D.discard(s[j: k+1])
            return res
        return dfs(0, 0, {}, set())