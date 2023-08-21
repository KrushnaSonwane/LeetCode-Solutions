class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        i = 0
        for word in words:
            if i == len(s): return 0
            if s[i]==word[0]:
                i += 1
            else: return 0
        return i == len(s)