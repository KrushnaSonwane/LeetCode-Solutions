class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        res =0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                A = nums[:i] + nums[j+1:]
                if A == sorted(set(A)):
                    res += 1
        return res