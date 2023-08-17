class Solution:
    def findLongestWord(self, s: str, A: List[str]) -> str:
        A.sort(key  = lambda x: (-len(x), x))
        for word in A:
            i = 0
            for ch in word:
                while i < len(s) and s[i] != ch:
                    i += 1
                if len(s) == i: break
                i += 1
            else: return word
        return ''