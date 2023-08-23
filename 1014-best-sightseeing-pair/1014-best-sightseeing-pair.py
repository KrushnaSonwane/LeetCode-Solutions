class Solution:
    def maxScoreSightseeingPair(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dfs(i, f, ff):
            if f and ff: return 0
            if i >= len(nums): return -inf
            res = dfs(i+1, f, ff)
            if not f:
                res = max(res, nums[i]+i + dfs(i+1, True, False))
            else:
                res = max(res, nums[i]-i + dfs(i+1, True, True))
            return res
        return dfs(0, False, False)