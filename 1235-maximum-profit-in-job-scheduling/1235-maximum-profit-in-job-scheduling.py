class Solution:
    def jobScheduling(self, S: List[int], E: List[int], P: List[int]) -> int:
        A = [[s, e, p] for s, e, p in zip(S, E, P)]
        A.sort(key=lambda x: x[0])
        @cache
        def dfs(i):
            if i >= len(S): return 0
            res = dfs(i+1)
            l, r = i+1, len(A)
            while r > l:
                mid = (r+l)//2
                if A[mid][0] < A[i][1]:
                    l = mid + 1
                else:
                    r = mid
            res = max(res, dfs(r) + A[i][2])
            return res
        return dfs(0)