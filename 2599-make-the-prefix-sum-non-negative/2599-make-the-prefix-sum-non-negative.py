class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        res, sum_, A = 0, 0, []
        for i in range(len(nums)):
            num = nums[i]
            if num < 0:
                heappush(A, num)
            sum_ += num
            if sum_ < 0:
                res += 1
                sum_ -= heappop(A)
        return res