class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        allChar = 'abcdefghijklmnopqrstuvwxyz'
        for ch in allChar:
            l, r = 0, len(s) - 1
            while r > l:
                while r > l and s[l] != ch:
                    l += 1
                while r > l and s[r] != ch:
                    r -= 1
                if r > l: res += len(set(s[l + 1: r]))
                break
        return res