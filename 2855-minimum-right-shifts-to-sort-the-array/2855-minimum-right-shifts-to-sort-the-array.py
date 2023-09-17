class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        res = 1
        if nums ==sorted(nums): return 0
        for i in range(len(nums)-1,-1,-1):
            A = nums[i:] + nums[:i]
            if A == sorted(A):
                return res
            res +=1
        return -1