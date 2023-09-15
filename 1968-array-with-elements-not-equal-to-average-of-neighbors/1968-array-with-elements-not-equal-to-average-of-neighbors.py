class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        res, f = [], 1
        while nums:
            res.append(nums.pop(0 if f else -1))
            f = not f
        return res