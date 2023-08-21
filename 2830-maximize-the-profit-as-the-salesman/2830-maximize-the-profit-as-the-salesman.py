class Solution:
    def maximizeTheProfit(self, n: int, A: List[List[int]]) -> int:
        A.sort()
        B = [val for val, _, _ in A]
        @cache
        def dfs(i):
            if i == len(A): return 0
            res = dfs(i+1)
            j = bisect.bisect_right(B, A[i][1])
            res = max(res, dfs(j) + A[i][2])
            return res
        return dfs(0)