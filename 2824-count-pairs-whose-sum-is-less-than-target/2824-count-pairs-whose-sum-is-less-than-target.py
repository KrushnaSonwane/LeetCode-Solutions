class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                res += target > nums[i]+nums[j]
        return res