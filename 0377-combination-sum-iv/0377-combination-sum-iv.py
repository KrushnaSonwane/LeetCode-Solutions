class Solution:
    def combinationSum4(self, A: List[int], target: int) -> int:
        @lru_cache(None)
        def dfs(sum_):
            if sum_ == 0: return 1
            res = 0
            for j in range(len(A)):
                if A[j] <= sum_:
                    res += dfs(sum_-A[j])
            return res
        return dfs(target)