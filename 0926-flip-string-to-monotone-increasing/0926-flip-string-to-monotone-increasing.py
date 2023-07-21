class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        l, r = 0, s.count('0')
        res = r
        for ch in s:
            r -= ch == '0'
            l += ch == '1'
            res = min(res, r+l)
        return res