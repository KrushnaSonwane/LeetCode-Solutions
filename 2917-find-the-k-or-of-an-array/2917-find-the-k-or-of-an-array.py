class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(32):
            cnt = 0
            for num in nums:
                if (num >> i) & 1:
                    cnt += 1
            if cnt >= k:
                res |= (1 << i)
        return res