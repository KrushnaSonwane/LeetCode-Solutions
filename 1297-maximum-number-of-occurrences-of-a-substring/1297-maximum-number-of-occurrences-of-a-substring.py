class Solution:
    def maxFreq(self, s: str, k: int, min_: int, max_: int) -> int:
        hashT = Counter()
        for size in range(min_, max_+1):
            for i in range(len(s)-size+1):
                hashT[s[i:i+size]] += 1
        res = 0
        for ch in hashT:
            if len(set(ch)) <= k:
                res = max(res, hashT[ch])
        return res