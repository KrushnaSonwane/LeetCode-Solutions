class Solution:
    def reverseWords(self, s: str) -> str:
        A = s.split()
        return ' '.join(ch[::-1] for ch in A)