class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        a = s1.count('x')+s2.count('x')
        b = s1.count('y')+s2.count('y')
        if a % 2 or b % 2: return -1
        A = defaultdict(int)
        for ch1, ch2 in zip(s1, s2):
            if ch1 != ch2:
                A[ch1+ch2] += 1
        return sum(ceil(A[ch]/2) for ch in A)