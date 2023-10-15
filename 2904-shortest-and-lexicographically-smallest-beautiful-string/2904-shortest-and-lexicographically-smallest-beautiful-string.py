class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if s.count('1') < k: return ''
        res = '1' * 1000
        for i in range(len(s)):
            count = 0
            for j in range(i, len(s)):
                count += s[j] == '1'
                if count == k:
                    a = s[i: j+1]
                    if len(a) < len(res):
                        res = a
                    elif len(a) == len(res):
                        res = min(res, a)
        return res