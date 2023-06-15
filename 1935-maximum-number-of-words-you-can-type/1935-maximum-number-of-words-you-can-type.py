class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        res = text.split()
        ans = 0
        for word in res:
            for ch in word:
                if ch in brokenLetters: break
            else: ans += 1
        return ans