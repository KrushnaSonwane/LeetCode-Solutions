class Solution:
    def areSentencesSimilar(self, s1: str, s2: str) -> bool:
        A, B = s1.split(), s2.split()
        while A and B and A[0]==B[0]:
            B.pop(0)
            A.pop(0)
        while A and B and A[-1]==B[-1]:
            B.pop()
            A.pop()
        return not A or not B