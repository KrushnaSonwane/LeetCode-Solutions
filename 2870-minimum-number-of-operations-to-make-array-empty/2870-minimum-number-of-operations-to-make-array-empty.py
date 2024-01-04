class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums.sort()
        @cache
        def dfs(i):
            if i == len(nums): return 0
            res = inf
            if i + 1 < len(nums):
                if nums[i] == nums[i+1]:
                    res = min(res, dfs(i+2) + 1)
            if i + 2 < len(nums):
                if nums[i] == nums[i+1] == nums[i+2]:
                    res = min(res, dfs(i+3)+1)
            return res
        ans = dfs(0)
        if ans == inf: return -1
        return ans