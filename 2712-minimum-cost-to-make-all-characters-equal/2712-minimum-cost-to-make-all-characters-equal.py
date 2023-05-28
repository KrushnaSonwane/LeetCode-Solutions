class Solution:
    def minimumCost(self, s: str) -> int:
        n = len(s)
        return sum(min(i, n - i) for i in range(1, n) if s[i] != s[i - 1])