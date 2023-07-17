class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        c, res = '', 0
        while len(b) >= len(c):
            res += 1
            c += a
            if b in c: return res
        c += a
        if b in c: return res+1
        return -1