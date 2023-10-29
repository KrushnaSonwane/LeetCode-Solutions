class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        dp = [[-1 for _ in range(target+1)] for _ in range(len(nums))]
        def dfs(i, sum_):
            if sum_ == 0: return 0
            if i == len(nums): return -inf
            if dp[i][sum_] != -1: return dp[i][sum_]
            res = -inf
            if nums[i] <= sum_:
                res = dfs(i+1, sum_ - nums[i]) + 1
            res = max(res, dfs(i+1, sum_))
            dp[i][sum_] = res
            return res
        res = dfs(0, target)
        return -1 if res == -inf else res