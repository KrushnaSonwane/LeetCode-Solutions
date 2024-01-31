class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        A = ''.join(s).split()[::-1]
        i = 0
        for w in A:
            for ch in w:
                s[i] = ch
                i += 1
            if i < len(s):
                s[i], i = ' ', i + 1