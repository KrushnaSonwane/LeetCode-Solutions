class Solution:
    def replaceDigits(self, s: str) -> str:
        res = []
        for i in range(0, len(s), 2):
            res.append(s[i])
            if len(s) > i + 1:
                num = ord(s[i]) + int(s[i + 1])
                res.append(chr(num))
        return ''.join(res)