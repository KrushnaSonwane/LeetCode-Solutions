class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        res, last, count = 0, nums[0], 0
        for num in nums:
            if num > last:
                count += 1
            res += count
            last = num
        return res