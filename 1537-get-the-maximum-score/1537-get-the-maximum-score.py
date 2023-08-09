class Solution:
    def maxSum(self, N1: List[int], N2: List[int]) -> int:
        A, B = {val: i for i, val in enumerate(N1)}, {val: i for i, val in enumerate(N2)}
        mod = 10**9+7
        @cache
        def dfs(i, f):
            if f and len(N1) == i: return 0
            if not f and len(N2)==i: return 0
            if f:
                res = N1[i] + dfs(i+1, f)
                if N1[i] in B:
                    res = max(res, N1[i] + dfs(B[N1[i]] + 1, False))
            else:
                res = N2[i] + dfs(i+1, f)
                if N2[i] in A:
                    res = max(res, N2[i] + dfs(A[N2[i]] + 1, True))
            return res
        return max(dfs(0, False), dfs(0, True)) % mod