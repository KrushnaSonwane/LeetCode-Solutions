class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            a, b = 0, 0
            for j in range(i, len(s)):
                if s[j] in "aeoui":
                    a += 1
                else:
                    b += 1
                if a == b and (a * b) % k == 0:
                    res += 1
        return res