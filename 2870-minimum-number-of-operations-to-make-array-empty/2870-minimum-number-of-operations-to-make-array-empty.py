class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums.sort()
        @lru_cache(None)
        def dfs(i):
            if i == len(nums):
                return 0
            res = inf
            if i + 1 < len(nums) and nums[i+1]==nums[i]:
                res = min(res, 1 + dfs(i+2))
            if i + 1 < len(nums) and i + 2 < len(nums) and nums[i] == nums[i+1] == nums[i+2]:
                res = min(res, 1 + dfs(i+3))
            return res
        res = dfs(0)
        return -1 if res == inf else res