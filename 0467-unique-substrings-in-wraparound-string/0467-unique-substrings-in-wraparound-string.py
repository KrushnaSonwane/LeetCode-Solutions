class Solution:
    def findSubstringInWraproundString(self, S: str) -> int:
        res = 0
        for ch in range(97, 123, 1):
            ch, count, i = chr(ch), 0, 0
            while len(S) > i:
                if S[i] == ch:
                    t = 1
                    while i + 1 < len(S):
                        if S[i] != 'z':
                            if ord(S[i]) + 1 != ord(S[i+1]):
                                break
                        else:
                            if S[i+1] != 'a' or S[i] != 'z':
                                break
                        t, i = t + 1, i + 1
                    count = max(count, t)
                i += 1
            res += count
        return res