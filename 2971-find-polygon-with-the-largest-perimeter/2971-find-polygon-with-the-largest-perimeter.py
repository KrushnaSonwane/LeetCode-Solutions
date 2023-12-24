class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        A = [0]
        for num in nums:
            A.append(num+A[-1])
        A.pop(0)
        res = -1
        for i in range(2, len(nums)):
            if nums[i] < A[i-1]:
                res = max(res, A[i])
        return res