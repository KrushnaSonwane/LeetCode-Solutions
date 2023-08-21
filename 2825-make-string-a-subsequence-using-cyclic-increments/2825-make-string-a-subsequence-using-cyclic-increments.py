class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        hashT = {}
        for i in range(97, 122):
            hashT[chr(i)] = chr(i+1)
        hashT['z'] = 'a'
        i = 0
        for ch in str1:
            if ch == str2[i]:
                i += 1
            elif hashT[ch]==str2[i]:
                i += 1
            if len(str2) == i: return 1
        return 0