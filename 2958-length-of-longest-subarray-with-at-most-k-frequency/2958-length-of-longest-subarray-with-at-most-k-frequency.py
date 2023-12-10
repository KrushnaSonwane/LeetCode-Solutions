class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        res = 0
        hashT = defaultdict(int)
        i = 0
        for j in range(len(nums)):
            num = nums[j]
            hashT[num] += 1
            while hashT[num] > k:
                hashT[nums[i]] -= 1
                i += 1
            res = max(res, j - i + 1)
        return res