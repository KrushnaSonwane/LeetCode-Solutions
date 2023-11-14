class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        for a in range(97, 123):
            a = chr(a)
            i, j = 0, len(s)-1
            while i < len(s) and s[i] != a:
                i += 1
            while j >= 0 and s[j] != a:
                j -= 1
            if len(s) > i:
                hashT = set()
                for k in range(i+1, j):
                    hashT.add(s[k])
                res += len(hashT)
        return res