class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        res, hashT = 1, defaultdict(int)
        l = 0
        for i, num in enumerate(nums):
            curr, count, t = num, 0, []
            while curr:
                if curr & 1:
                    hashT[count] += 1
                    if hashT[count] > 1:
                        t.append(count)
                count += 1
                curr //= 2
            for c in t:
                while hashT[c] > 1 and i - l + 1 > 1:
                    curr, count = nums[l], 0
                    while curr:
                        if curr & 1:
                            hashT[count] -= 1
                        curr //= 2
                        count += 1
                    l += 1
            res = max(res, i - l + 1)
        return res