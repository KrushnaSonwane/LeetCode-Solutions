class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        hashT = {}
        for i in range(97, 123):
            ch = chr(i)
            j = 0
            while len(s) > j and s[j] != ch:
                j += 1
            if j != len(s):
                hashT[ch] = [j, j-1]
            j = len(s)-1
            while j >= 0 and s[j] != ch:
                j -= 1
            if j != -1:
                hashT[ch][1] = j
        res = -1
        for ch in hashT:
            i, j = hashT[ch]
            res = max(res, (j - i) - 1)
        return res