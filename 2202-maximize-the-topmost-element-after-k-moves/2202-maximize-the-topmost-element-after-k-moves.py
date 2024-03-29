class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if k == 0: return nums[0]
        if len(nums)==1:
            if k%2: return -1
            return nums[0] 
        if k == 1: return nums[1]
        if len(nums)==k: return max(nums[:-1])
        if len(nums) > k: return max(nums[k], max(nums[:k-1]))
        if k >= len(nums): return max(nums)
        return max(nums[:k])