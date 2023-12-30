class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        hashT = defaultdict(int)
        for w in words:
            for ch in w:
                hashT[ch] += 1
        for ch in hashT:
            if hashT[ch] % len(words) != 0: 
                return 0
        return 1