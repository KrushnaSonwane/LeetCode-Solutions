class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(ch[::-1] for ch in s.split())