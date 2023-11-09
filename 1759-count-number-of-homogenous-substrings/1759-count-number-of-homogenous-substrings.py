class Solution:
    def countHomogenous(self, s: str) -> int:
        last, res, MOD = '', 0, 10**9+7
        for ch in s:
            if last != ch:
                count, last = 0, ch
            count += 1
            res = (res + count) % MOD
        return res