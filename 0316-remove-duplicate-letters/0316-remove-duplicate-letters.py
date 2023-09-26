class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        res, A = [], Counter(s)
        for ch in s:
            A[ch] -= 1
            if ch not in res:
                while res and res[-1] > ch and A[res[-1]]:
                    res.pop()
                res.append(ch)
        return ''.join(res)