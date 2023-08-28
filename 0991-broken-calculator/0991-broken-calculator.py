class Solution:
    def brokenCalc(self, start: int, end: int) -> int:
        res = 0
        while end > start:
            if end%2:
                end += 1
            else:
                end //= 2
            res += 1
        return res + start - end