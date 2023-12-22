class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n, hashT = len(nums), Counter()
        i, res = 0, 0
        count = 0
        pairs = 0
        for j, num in enumerate(nums):
            count += 1
            pairs += hashT[num]
            hashT[num] += 1
            while  pairs >= k:
                hashT[nums[i]] -= 1
                pairs -= hashT[nums[i]]
                i += 1
                count -= 1
            res += count
        return (n*(n+1) // 2) - res