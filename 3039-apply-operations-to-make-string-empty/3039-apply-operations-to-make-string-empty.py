class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        A = Counter(s)
        max_ = max(A.values())
        taken, res = set(), []
        for ch in s[::-1]:
            if A[ch] == max_ and ch not in taken:
                taken.add(ch)
                res.append(ch)
        return ''.join(res[::-1])