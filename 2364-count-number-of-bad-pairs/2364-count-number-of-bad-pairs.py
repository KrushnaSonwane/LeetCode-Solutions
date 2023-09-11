class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        N, res, hashT = len(nums), 0, defaultdict(int)
        for i, num in enumerate(nums):
            diff = -num+i
            res += hashT[diff]
            hashT[diff] += 1
        N = (N * (N+1) // 2) - N
        return N - res