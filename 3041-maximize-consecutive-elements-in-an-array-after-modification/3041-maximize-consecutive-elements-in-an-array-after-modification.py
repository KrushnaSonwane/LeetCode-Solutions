class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        dp = Counter()
        nums.sort()
        ans = 0
        for num in nums:
            dp[num+1] = dp[num] + 1
            dp[num] = dp[num-1] + 1
            ans = max(ans, dp[num+1], dp[num])
        return ans