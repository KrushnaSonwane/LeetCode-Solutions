class Solution:
    def removeVowels(self, s: str) -> str:
        A = []
        for ch in s:
            if ch in 'aeiou': continue
            A.append(ch)
        return ''.join(A)