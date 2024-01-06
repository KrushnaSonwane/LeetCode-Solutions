class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        ans, length = 0, 0
        hashT = set(nums)
        ans = nums[0]
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]+1:
            
                ans += nums[i]
                i += 1
            else:
                break
        while ans in hashT:
            ans += 1
        return ans