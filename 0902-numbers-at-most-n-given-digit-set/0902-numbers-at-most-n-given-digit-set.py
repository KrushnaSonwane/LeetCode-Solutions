class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        A = str(n)
        @cache
        def dfs(i, start, tight):
            if i == len(A): return 1 if start else 0
            res = 0
            if not start:
                res = dfs(i+1, start, False)
            for d in digits:
                if tight and d > A[i]: continue
                res += dfs(i+1, True, tight and d == A[i])
            return res
        return dfs(0, False, True)