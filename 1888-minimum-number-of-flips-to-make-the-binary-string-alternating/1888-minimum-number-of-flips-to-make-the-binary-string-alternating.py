class Solution:
    def minFlips(self, s: str) -> int:
        n, s = len(s), s + s
        a, b = 0, 0
        for i in range(n):
            a += i % 2 == 0 and s[i] == '1'
            b += i % 2 == 1 and s[i] == '1'
            
        x, y = ceil(n / 2), n // 2
        res = min((x-a)+b, (a + (y - b)))
        
        for i in range(n, len(s)):
            a -= s[i-n] == '1'
            a, b = b, a
            b += n % 2 == 0 and s[i] == '1'
            a += n % 2 and s[i] == '1'
            res = min(res, (x-a)+b, (a + (y - b)))
            
        return res