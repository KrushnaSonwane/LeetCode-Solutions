class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        hashT = {0: -1}
        sum_, res = 0, 0
        for i, num in enumerate(nums):
            sum_ += num
            key = k - sum_
            if key in hashT:
                res = max(res, i - hashT[key])
            if -sum_ not in hashT:
                hashT[-sum_] = i
        return res  