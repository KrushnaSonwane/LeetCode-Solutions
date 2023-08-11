class Solution:
    def minimumDeletions(self, s: str) -> int:
        a = s.count('a')
        res = a
        for ch in s:
            if ch == 'a': a -= 1
            else: a += 1
            res = min(res, a)
        return res