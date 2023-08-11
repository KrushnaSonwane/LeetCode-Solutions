class Solution:
    def minimumDeletions(self, s: str) -> int:
        a, b = s.count('a'), 0
        res = a
        for ch in s:
            if ch == 'a': a -= 1
            else: b += 1
            res = min(res,a+b)
        return res