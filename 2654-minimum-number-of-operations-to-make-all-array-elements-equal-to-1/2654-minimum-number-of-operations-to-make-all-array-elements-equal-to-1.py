class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if 1 in nums:
            return sum(1 for num in nums if num != 1)
        min_ = inf
        for i in range(len(nums)):
            val = 0
            for j in range(i, len(nums)):
                val = gcd(nums[j], val)
                if val == 1:
                    min_ = min(min_, j - i)
        return -1 if min_ == inf else min_ + len(nums)-1