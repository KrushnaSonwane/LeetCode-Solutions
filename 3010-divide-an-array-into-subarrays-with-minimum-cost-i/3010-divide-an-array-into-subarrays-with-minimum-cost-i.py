class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        res = inf
        for j in range(1, len(nums)):
                for k in range(j+1, len(nums)):
                    res = min(res, nums[k] + nums[j] +nums[0])
        return res