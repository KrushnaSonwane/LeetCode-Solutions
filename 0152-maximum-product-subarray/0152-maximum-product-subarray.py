class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res, curr = max(nums), 1
        for num in nums:
            curr *= num
            if num == 0:
                curr = 1
                continue
            res = max(res, curr)
        curr = 1
        for num in nums[::-1]:
            curr *= num
            if num==0:
                curr = 1
                continue
            res = max(res, curr)
        return res