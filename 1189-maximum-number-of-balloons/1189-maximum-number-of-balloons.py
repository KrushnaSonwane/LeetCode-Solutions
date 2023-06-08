class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashT = defaultdict(int)
        for ch in text: hashT[ch] += 1
        hashT['l'] //= 2; hashT['o'] //= 2
        return min(hashT[ch] for ch in 'balon')