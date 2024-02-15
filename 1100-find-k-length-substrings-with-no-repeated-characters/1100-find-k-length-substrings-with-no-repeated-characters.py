class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if k > 26 or len(s) < k: return 0
        res = 0
        for i in range(len(s)):
            visit = set()
            for j in range(i, min(len(s), i + k)):
                visit.add(s[j])
            res += len(visit) == k
        return res