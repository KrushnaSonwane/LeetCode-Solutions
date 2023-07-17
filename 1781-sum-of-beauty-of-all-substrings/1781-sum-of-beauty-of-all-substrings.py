class Solution:
    def beautySum(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            hashT = defaultdict(int)
            for j in range(i, len(s)):
                hashT[s[j]] += 1
                res += max(hashT.values())-min(hashT.values())
        return res