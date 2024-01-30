class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        res, curr = 0, 0
        hashT = {ch: i for i, ch in enumerate(keyboard)}
        for ch in word:
            res += abs(hashT[ch] -  curr)
            curr = hashT[ch]
        return res