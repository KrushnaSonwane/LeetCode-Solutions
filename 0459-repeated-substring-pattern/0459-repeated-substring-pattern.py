class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n // 2 + 1):
            if not n % i:
                p = s[:i] * (n//i)
                if p == s: return True
        return False