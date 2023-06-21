class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = {}
        def dfs(i):
            if i not in dp:
                if i == n: return True
                res = False
                if i + 1 < n and nums[i] == nums[i + 1]:
                    res = dfs(i + 2)
                if i + 2 < n and nums[i] == nums[i + 1] == nums[i + 2]:
                    res = res or dfs(i + 3)
                if i + 2 < n and nums[i] == nums[i + 1] - 1 == nums[i + 2] - 2:
                    res = res or dfs(i + 3)
                dp[i] = res
            return dp[i]
        return dfs(0)