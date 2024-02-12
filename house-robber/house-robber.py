class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dfs(i):
            if i >= len(nums): return 0
            return max(dfs(i+1), dfs(i+2) + nums[i])
        return dfs(0)