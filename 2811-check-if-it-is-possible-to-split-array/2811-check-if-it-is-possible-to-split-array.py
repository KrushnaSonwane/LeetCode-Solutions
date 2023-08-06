class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        if len(nums)<=2: return True
        for i in range(len(nums)-1):
            if nums[i+1]+nums[i]>=m: return 1
        return 0