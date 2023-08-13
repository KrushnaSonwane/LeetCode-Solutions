class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        @cache
        def dfs(i, mod):
            if i == len(nums):
                return 0 if mod == 0 else -inf
            res = dfs(i+1, mod)
            res = max(res, nums[i] + dfs(i+1, (nums[i]+mod) % 3))
            return res
        return dfs(0, 0)