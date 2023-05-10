class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [[-1, -1] for _ in nums]
        def dfs(i, isEven):
            if i == len(nums): return 0
            if dp[i][isEven] != -1: return dp[i][isEven]
            notTake = dfs(i + 1, isEven)
            take = (nums[i] if isEven else -nums[i]) + dfs(i + 1, not isEven)
            dp[i][isEven] = max(notTake, take)
            return dp[i][isEven]
        return dfs(0, 1)