class Solution:
    def maximumSubsequenceCount(self, text: str, p: str) -> int:
        x, y = text.count(p[0]), text.count(p[1])
        res, a = y, y
        for ch in text:
            a -= ch == p[1]
            if ch == p[0]:
                res += a
        res2, a = x, x
        for ch in text[::-1]:
            a -= ch == p[0]
            if ch == p[1]:
                res2 += a
        return max(res, res2)