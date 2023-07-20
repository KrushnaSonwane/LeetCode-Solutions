class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        if n < 10: return n
        A, num = [], n
        while num:
            A.append(num%10)
            num //= 10
        A = A[::-1]
        def check(A, N):
            for i in range(N-1, -1, -1):
                if A[i] > A[i+1]: return 0
            return 1
        if check(A, len(A)-1): return n
        for i in range(len(A)-1, -1, -1):
            A[i-1] -= 1
            A[i] = 9
            if check(A, i-1): break
        return int(''.join(str(ch) for ch in A))