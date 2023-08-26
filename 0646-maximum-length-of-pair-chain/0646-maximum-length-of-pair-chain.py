class Solution:
    def findLongestChain(self, A: List[List[int]]) -> int:
        A.sort()
        @lru_cache(None)
        def dfs(i, last):
            if i == len(A): return 0
            res = dfs(i+1, last)
            if A[i][0] > last:
                res = max(res, 1 + dfs(i+1, A[i][1]))
            return res
        return dfs(0, -1001)