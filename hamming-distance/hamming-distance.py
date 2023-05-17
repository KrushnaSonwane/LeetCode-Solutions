from itertools import zip_longest
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xx, yy = '', ''
        while x:
            xx = str(x % 2) + xx
            x //= 2
        while y:
            yy = str(y % 2) + yy
            y //= 2
        res = 0
        xx, yy = xx[::-1], yy[::-1]
        for x, y in zip_longest(xx, yy, fillvalue = '0'):
            res += int(x != y)
        return res