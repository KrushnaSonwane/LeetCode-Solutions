class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        hashT = defaultdict(list)
        for i,num in enumerate(nums):
            hashT[num].append(i)
        res = 1
        for num in hashT:
            if len(hashT[num]) > 1:
                l, r = 0, 1
                size = 0
                while r < len(hashT[num]):
                    size += hashT[num][r] - hashT[num][r-1] - 1
                    while size > k:
                        size -= hashT[num][l+1] - hashT[num][l] - 1
                        l += 1
                    res = max(res, r - l + 1)
                    r += 1
        return res