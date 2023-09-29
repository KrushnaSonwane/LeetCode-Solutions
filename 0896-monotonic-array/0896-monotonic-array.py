class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        a, b = False, False
        for i in range(1, len(nums)):
            a = a or nums[i] > nums[i-1]
            b = b or nums[i] < nums[i-1]
        return not a or not b