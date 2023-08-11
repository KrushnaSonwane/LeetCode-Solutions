class Solution:
    def minimumDeletions(self, s: str) -> int:
        a = s.count('a')
        res = a
        for ch in s:
            a += 1 if ch == 'b' else -1
            res = min(res, a)
        return res