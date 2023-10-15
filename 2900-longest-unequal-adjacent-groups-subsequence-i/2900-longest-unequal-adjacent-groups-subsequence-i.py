class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        a, b = [], []
        last = 0
        for i, g in enumerate(groups):
            if g != last:
                last= g
                a.append(words[i])
        last = 1
        for i, g in enumerate(groups):
            if g != last:
                last= g
                b.append(words[i])
        return a if len(a) > len(b) else b