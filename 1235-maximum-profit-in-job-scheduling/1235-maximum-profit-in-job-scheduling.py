class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        A = sorted([[s, e, p] for s, e, p in zip(startTime, endTime, profit)])
        @cache
        def dfs(i):
            if i == len(A): return 0
            res = dfs(i+1)
            l, r = i+1, len(A)-1
            ans = r+1
            while r >= l:
                mid = (r+l) // 2
                s, e, p = A[mid]
                if A[i][1] > s:
                    l = mid  + 1
                else:
                    ans = mid
                    r = mid - 1  
            res = max(res, dfs(ans) + A[i][2])
            return res
        return dfs(0)