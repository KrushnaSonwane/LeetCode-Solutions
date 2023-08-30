class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        last, res = inf, 0
        for num in nums[::-1]:
            if last >= num:
                last = num
            else:
                c = ceil(num / last)
                res += c - 1
                last = num // c
        return res