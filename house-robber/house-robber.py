class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [-1 for _ in nums]
        def dfs(i):
            if i >= len(nums): return 0
            if dp[i] != -1: return dp[i]
            take = nums[i] + dfs(i + 2)
            notTake = dfs(i + 1)
            dp[i] = max(take, notTake)
            return dp[i]
        return dfs(0)