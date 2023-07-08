class Solution:
    def removeDuplicateLetters(self, S: str) -> str:
        count = collections.Counter(S)
        A, visit = [], set()
        for ch in S:
            count[ch] -= 1
            if ch not in visit:
                visit.add(ch)
                while A and A[-1] > ch and count[A[-1]]: visit.discard(A.pop())
                A.append(ch)
        return ''.join(A)