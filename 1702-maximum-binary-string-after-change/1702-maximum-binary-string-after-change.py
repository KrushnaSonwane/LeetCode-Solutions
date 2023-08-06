class Solution:
    def maximumBinaryString(self, s: str) -> str:
        a, b = s.count('1'), s.count('0')-1
        i, x = 0, 0
        while len(s)>i and s[i]=='1':
            x += 1
            i += 1
        return '1'*x + ('1'*b+'0' if b >= 0 else '') + '1'*(a-x)