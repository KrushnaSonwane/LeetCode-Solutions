class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        res, sum_ = 0, 0
        for num in nums:
            sum_ += num
            res += sum_ == 0
        return res