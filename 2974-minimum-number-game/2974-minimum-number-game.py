class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        for i in range(1, len(nums), 2):
            res.append(nums[i])
            res.append(nums[i-1])
        return res