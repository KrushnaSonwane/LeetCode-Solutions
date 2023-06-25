class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        c = nums.count(1)
        if c == 1 or c == 0: return c
        ptr = nums.index(1)
        n = len(nums)
        res, mod = 1, 10 ** 9 + 7
        while c >= 1:
            curr = 1
            while nums[ptr] == 0:
                ptr += 1
                curr += 1
            res *= curr
            res %= mod
            ptr += 1
            c -= 1
        return res