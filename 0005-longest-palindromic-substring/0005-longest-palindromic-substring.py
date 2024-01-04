class Solution:
    def longestPalindrome(self, s: str) -> str:
        def solve(i, j):
            res = 0
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
                res += 2
            return res, i, j
        res, k = 1, 0
        for i in range(len(s)-1):
            size, a, b = solve(i, i)
            if res < size-1:
                res, k = size-1, a+1
            size, a, b = solve(i, i+1)
            if res < size:
                res, k = size, a+1
        return s[k: k+res]