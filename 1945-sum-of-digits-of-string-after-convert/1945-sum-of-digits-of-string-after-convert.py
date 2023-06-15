class Solution:
    def getLucky(self, s: str, k: int) -> int:
        res = ''
        for ch in s:
            res += str(ord(ch) - 96)
        res = int(res)
        while k:
            temp = 0
            while res:
                temp += res % 10
                res //= 10
            res = temp
            k -= 1
        return res