class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        hashT = {}
        sum_ = 0
        res = -inf
        for num in nums:
            sum_ += num
            if num + k in hashT:
                res = max(res, sum_ - hashT[num+k])
            if num - k in hashT:
                res = max(res, sum_ - hashT[num-k])
            if num in hashT:
                hashT[num] = min(hashT[num], sum_-num)
            else:
                hashT[num] = sum_ - num
        return res if res != -inf else 0