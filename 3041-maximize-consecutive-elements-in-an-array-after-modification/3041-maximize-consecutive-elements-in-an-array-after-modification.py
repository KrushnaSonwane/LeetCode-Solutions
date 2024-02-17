class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        dp = Counter()
        for num in sorted(nums):
            dp[num+1] = dp[num] + 1
            dp[num] = dp[num-1] + 1
        return max(dp.values())