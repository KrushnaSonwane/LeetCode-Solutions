class Solution:
    def countMatchingSubarrays(self, nums: List[int], p: List[int]) -> int:
        res = 0
        for i in range(1, len(nums)):
            l, r = i, 0
            while r < len(p) and l < len(nums):
                if p[r] == 1 and nums[l] > nums[l-1]:
                    pass
                elif p[r] == 0 and nums[l] == nums[l-1]:
                    pass
                elif p[r] == -1 and nums[l] < nums[l-1]:
                    pass
                else:
                    break
                l += 1
                r += 1
            if r == len(p):
                res += 1
        return res