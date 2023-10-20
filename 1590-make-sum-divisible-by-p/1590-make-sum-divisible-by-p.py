class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        hashT = defaultdict(list)
        if sum(nums)%p== 0: return 0
        mod, res = 0, inf
        for i, num in enumerate(nums):
            mod = (mod + num) % p
            if not mod:
                res = min(res, len(nums)-(i+1))
            hashT[mod].append(i)
        mod = 0
        for i in range(len(nums)-1, -1, -1):
            mod = (mod + nums[i]) % p
            if mod == 0:
                res = min(res, i)
            rem = p - mod
            if hashT[rem]:
                l, r = 0, len(hashT[rem])-1
                while r >= l:
                    mid = (r + l) // 2
                    if hashT[rem][mid] >= i:
                        r = mid - 1
                    else:
                        res = min(res, (i - (hashT[rem][mid]))-1)
                        l = mid + 1
        return -1 if res == inf else res