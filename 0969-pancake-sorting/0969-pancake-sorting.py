class Solution:
    def pancakeSort(self, nums: List[int]) -> List[int]:
        A, res = sorted(nums), []
        n, i= len(A), len(A)-1
        while i >= 0:
            if A[i] != nums[i]:
                j = nums.index(A[i])
                nums = nums[:j+1][::-1] + nums[j+1:]
                nums = nums[:i+1][::-1] + nums[i+1:]
                res.extend([j+1, i+1])
            i -= 1
        return res