class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        dp = {}
        for i in range(1, len(nums)): nums[i] += nums[i - 1]
        def dfs(i, k):
            if (i, k) not in dp:
                if i == len(nums): return 0
                if k == 1:
                    sum_ = nums[-1] if i == 0 else nums[-1] - nums[i - 1]
                    size = len(nums) - i
                    return sum_ / size
                res = 0
                for j in range(i, len(nums) - (k - 1)):
                    sum_, size = nums[j] if i == 0 else nums[j] - nums[i - 1], (j - i + 1)
                    res = max(res, (sum_ / size) + dfs(j + 1, k - 1))
                dp[(i, k)] = res
            return dp[(i, k)]
        return dfs(0, k)