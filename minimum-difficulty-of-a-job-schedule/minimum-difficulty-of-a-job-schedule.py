class Solution:
    def minDifficulty(self, A: List[int], d: int) -> int:
        dp = {}
        def dfs(i, k):
            if (i, k) not in dp:
                if k < 0: return inf
                if i == len(A):
                    return 0 if k == 0 else inf
                res, max_ = inf, 0
                for j in range(i, len(A)):
                    max_ = max(max_, A[j])
                    res = min(res, dfs(j+1, k-1)+max_)
                dp[(i, k)] = res
            return dp[(i, k)]
        res = dfs(0, d)
        return -1 if res == inf else res