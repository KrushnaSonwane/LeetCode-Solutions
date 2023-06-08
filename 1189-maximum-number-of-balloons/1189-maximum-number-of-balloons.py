class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashT = defaultdict(int)
        for ch in text: hashT[ch] += 1
        res = float("inf")
        for ch in "ban":
            res = min(hashT[ch], res)
        return min(hashT['l'] // 2, hashT['o'] // 2, res)