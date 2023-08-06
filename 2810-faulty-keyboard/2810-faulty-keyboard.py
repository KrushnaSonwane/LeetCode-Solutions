class Solution:
    def finalString(self, s: str) -> str:
        res = ''
        for ch in s:
            if ch == 'i':
                res = res[::-1]
            else:
                res += ch
        return res