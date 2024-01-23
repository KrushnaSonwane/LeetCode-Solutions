class Solution:
    def minSessions(self, A: List[int], S: int) -> int:
        @cache
        def dfs(i, k):
            if i == len(A):
                return len(k)
            B = list(k)
            B.append(S-A[i])
            res = dfs(i+1, tuple(B))
            B.pop()
            for j, num in enumerate(B):
                if A[i] <= num:
                    B[j] -= A[i]
                    res = min(res, dfs(i+1, tuple(sorted(B))))
                    B[j] += A[i]
            return res
        return dfs(0, tuple([S]))