class Solution:
    def minDeletions(self, s: str) -> int:
        hashT, last = Counter(s), inf
        A = sorted([val for val in hashT.values()])[::-1]
        last, res = inf, 0
        for a in A:
            last = max(0, min(a, last-1))
            res += a-last
        return res