class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        def dfs(num):
            if nums[num] == -1: return 0
            t, nums[num] = nums[num], -1
            return 1 + dfs(t)
        res = 0
        for num in nums:
            res = max(res, dfs(num))
        return res