class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashT = Counter(text)
        hashT['l'] //= 2; hashT['o'] //= 2
        return min(hashT[ch] for ch in 'balon')