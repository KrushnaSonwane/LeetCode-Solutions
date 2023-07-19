class Solution:
    def eraseOverlapIntervals(self, A: List[List[int]]) -> int:
        A.sort()
        B = [a for a, _ in A]
        @cache
        def dfs(i):
            if i >= len(A): return 0
            res = dfs(i+1)
            j = bisect.bisect_right(B, A[i][1]-1)
            res = max(res, dfs(j)+1)
            return res
        return len(A)-dfs(0)