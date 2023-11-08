class Solution:
    def countInterestingSubarrays(self, nums: List[int], m: int, k: int) -> int:
        A, hashT = [], Counter({0: 1})
        for num in nums:
            A.append(int(num % m== k))
        res, sum_ = 0, 0
        for num in A:
            sum_ = (sum_ + num) % m
            res += hashT[(sum_ - k) % m]
            hashT[sum_] += 1
        return res