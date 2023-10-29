class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            hashT = set()
            for j in range(i, len(nums)):
                hashT.add(nums[j])
                res+= len(hashT) ** 2
        return res