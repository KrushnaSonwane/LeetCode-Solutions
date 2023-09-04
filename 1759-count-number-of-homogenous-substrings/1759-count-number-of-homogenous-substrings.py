class Solution:
    def countHomogenous(self, s: str) -> int:
        res, mod = 0, 10**9+7
        last, count = '', 0
        for ch in s:
            if ch == last:
                count += 1
            else: 
                count = 1
            last, res = ch, (res+count) % mod
        return res