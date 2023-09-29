class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        a, b = 0, 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                a = 1
            if nums[i] < nums[i-1]:
                b = 1
        return a == 0 or b == 0