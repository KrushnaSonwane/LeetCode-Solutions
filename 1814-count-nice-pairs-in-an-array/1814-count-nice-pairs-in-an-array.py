class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        mod, res, hashT = 10**9+7, 0, defaultdict(int)
        for num in nums:
            diff = num - int(str(num)[::-1])
            res = (res + hashT[diff]) % mod
            hashT[diff] += 1
        return res