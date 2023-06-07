class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        hashT = defaultdict(int)
        for word in words:
            for ch in word:
                hashT[ch] += 1
        n = len(words)
        for val in hashT.values():
            if val % n: return 0
        return 1