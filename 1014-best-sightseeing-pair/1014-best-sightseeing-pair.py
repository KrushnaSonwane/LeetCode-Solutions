class Solution:
    def maxScoreSightseeingPair(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dfs(i, taken, used):
            if taken and used: return 0
            if i >= len(nums): return -inf
            res = dfs(i+1, taken, used)
            if not taken:
                res = max(res, nums[i]+i + dfs(i+1, True, False))
            else:
                res = max(res, nums[i]-i + dfs(i+1, True, True))
            return res
        return dfs(0, False, False)