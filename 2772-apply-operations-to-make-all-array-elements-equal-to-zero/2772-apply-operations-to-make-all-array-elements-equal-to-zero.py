class Solution(object):
    def checkArray(self, nums, k):
        sum_, last = 0, 0
        for i, num in enumerate(nums):
            if sum_ > num: return 0
            nums[i] = num - sum_
            sum_ += nums[i]
            if i-k+1 >= 0:
                sum_ -= nums[i-k+1]
        return sum_ == 0