import math
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        @cache
        def dfs(nums, k):
            if not nums: return 0
            res = 0
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    rem = nums[:i] + nums[i+1:j] + nums[j+1:]
                    res = max(res, math.gcd(nums[i], nums[j]) * k + dfs(tuple(rem), k + 1))
            return res
        return dfs(tuple(nums), 1)