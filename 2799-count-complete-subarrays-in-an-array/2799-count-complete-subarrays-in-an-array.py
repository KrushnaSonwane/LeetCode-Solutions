class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        res = 0
        A = {num for num in nums}
        for i in range(len(nums)):
            hashT = set()
            for j in range(i, len(nums)):
                hashT.add(nums[j])
                res += len(A)==len(hashT)
        return res