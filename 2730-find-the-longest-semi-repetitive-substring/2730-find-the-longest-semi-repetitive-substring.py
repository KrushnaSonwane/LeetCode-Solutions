class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        res = 1
        n = len(s)
        for i in range(n):
            flag = False
            for j in range(i + 1, n):
                if s[j] == s[j - 1]:
                    if flag == True:
                        res = max(res, j - i)
                        break
                    flag = True
                res = max(res, j - i + 1)
        return res