class Solution:
    def numberOfWays(self, s: str) -> int:
        a, b, x, y = 0, 0, s.count('0'), s.count('1')
        res = 0
        for num in s:
            if num == '0':
                x -= 1
                res += b * y
                a += 1
            else:
                y -= 1
                res += x * a
                b += 1
        return res