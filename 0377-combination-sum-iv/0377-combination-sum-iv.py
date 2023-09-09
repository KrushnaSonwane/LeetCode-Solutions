class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [-1]*(target+1)
        dp[0] = 1
        def cs(nums, target, dp):
            if dp[target] > -1:
                return dp[target]
            count = 0
            for i in range(len(nums)):
                if nums[i] <= target:
                    count += cs(nums, target-nums[i], dp)
            dp[target] = count
            return count
        return cs(nums, target, dp)