from sortedcontainers import SortedList
class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        res, sum_, i = 0, 0, 0
        A = SortedList()
        for i in range(len(nums)):
            num = nums[i]
            if num < 0:
                A.add(num)
            sum_ += num
            if sum_ < 0:
                res += 1
                sum_ -= A.pop(0)
        return res