class Solution:
    def partitionString(self, s: str) -> int:
        A, res = set(), 0
        for ch in s:
            if ch not in A:
                A.add(ch)
            else:
                A = {ch}
                res += 1
        return res + 1