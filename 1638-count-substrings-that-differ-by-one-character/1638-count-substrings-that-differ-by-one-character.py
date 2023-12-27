class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        res = 0
        for i in range(len(s)):
            for j in range(len(t)):
                a, b = i, j
                count = 0
                while a < len(s) and b < len(t) and count <= 1:
                    if s[a] != t[b]:
                        count += 1
                    if count == 1: res += 1
                    a += 1
                    b += 1
        return res