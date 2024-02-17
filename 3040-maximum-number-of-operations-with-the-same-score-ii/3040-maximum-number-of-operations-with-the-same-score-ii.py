class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        @cache
        def dfs(i, j, sum_):
            if j <= i:
                return 0
            res = 0
            if nums[i] + nums[i+1] == sum_:
                res = max(res, dfs(i+2, j, sum_) + 1)
            if nums[i] + nums[j] == sum_:
                res = max(res, dfs(i+1, j-1, sum_) + 1)
            if nums[j] + nums[j-1] == sum_:
                res = max(res, dfs(i, j-2, sum_) + 1)
            return res
        res = dfs(2, len(nums)-1, nums[0] + nums[1]) + 1
        res = max(res, dfs(1, len(nums)-2, nums[0] + nums[-1]) + 1)
        res = max(res, dfs(0, len(nums)-3, nums[-1] + nums[-2]) + 1)
        return res