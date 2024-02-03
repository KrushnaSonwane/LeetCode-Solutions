class Solution:
    def selfDivisiblePermutationCount(self, n: int) -> int:
        res = []
        @cache
        def dfs(i, mask):
            if i == n:
                return 1
            res = 0
            for num in range(1, n+1):
                A = [ch for ch in mask]
                if A[num-1] == '0' and gcd(num, i+1) == 1:
                    A[num-1] = '1'
                    res += dfs(i+1, ''.join(A))
                    A[num-1] = '0'
            return res
        return dfs(0, '0'*n)