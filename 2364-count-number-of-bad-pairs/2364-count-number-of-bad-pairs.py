class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        res, n = 0, len(nums)
        hashT = defaultdict(int)
        for i, num in enumerate(nums):
            diff = i - num
            res += hashT[diff]
            hashT[diff] += 1
        return (n * (n-1) // 2) - res