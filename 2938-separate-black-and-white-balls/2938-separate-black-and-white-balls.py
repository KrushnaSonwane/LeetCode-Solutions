class Solution:
    def minimumSteps(self, s: str) -> int:
        A = []
        for i, ss in enumerate(s):
            if ss == '1':
                A.append(i)
        i = len(s)-1
        res = 0
        for num in A[::-1]:
            res += (i - num)
            i -= 1
        return res