class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        res, sum_ = -1, nums[0]+nums[1]
        for i in range(2, len(nums)):
            if nums[i] < sum_:
                res = max(res, sum_ + nums[i])
            sum_ += nums[i]
        return res