class Solution:
    def maxScore(self, s: str) -> int:
        left, right = [0]*len(s), [0]*len(s)
        count = 0
        for i, ch in enumerate(s):
            count += ch == '0'
            left[i] = count
        count = 0
        for i in range(len(s)-1, -1, -1):
            count += s[i] == '1'
            right[i] = count
        res = 0
        for i in range(1, len(s), 1):
            res = max(left[i-1] + right[i], res)
        return res