class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        A, B = [], []
        for i in range(len(s)):
            if i + len(a) <= len(s):
                if s[i: i+len(a)] == a:
                    A.append(i)
            if i + len(b) <= len(s):
                if s[i:i+len(b)] == b:
                    B.append(i)
        res, last = [], inf
        j = 0
        for i in A:
            while j < len(B) and B[j] <= i:
                last = B[j]
                j += 1
            if abs(last-i) <= k or (j < len(B) and abs(B[j]-i) <= k):
                res.append(i)
        return res