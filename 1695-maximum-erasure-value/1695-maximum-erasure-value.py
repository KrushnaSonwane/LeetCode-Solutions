class Solution(object):
    def maximumUniqueSubarray(self, nums):
        ptr, hashT = 0, defaultdict(int)
        res, sum_ = 0, 0
        for num in nums:
            hashT[num] += 1
            sum_ += num
            while hashT[num] == 2:
                hashT[nums[ptr]] -= 1
                sum_ -= nums[ptr]
                ptr += 1
            res = max(res, sum_)
        return res