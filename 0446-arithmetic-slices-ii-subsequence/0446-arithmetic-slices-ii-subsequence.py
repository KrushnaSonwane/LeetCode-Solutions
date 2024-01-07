class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        A, res = Counter(), 0
        for i in range(1, len(nums)):
            for j in range(0, i):
                diff = nums[i] - nums[j]
                A[(i, diff)] += A[(j, diff)] + 1
                res += A[(j, diff)]
        return res