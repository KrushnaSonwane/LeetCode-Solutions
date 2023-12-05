class Solution:
    def numberOfMatches(self, n: int) -> int:
        res = 0
        while n != 1:
            res += n // 2
            n = ceil(n / 2)
        return res