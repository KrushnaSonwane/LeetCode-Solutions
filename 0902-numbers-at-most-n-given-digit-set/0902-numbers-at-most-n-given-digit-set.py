class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        A = str(n)
        @cache
        def dfs(i, start, tight):
            if i == len(A): return start
            res = 0
            if not start:
                res = dfs(i+1, 0, False)
            for d in digits:
                if tight and d > A[i]: continue
                res += dfs(i+1, 1, tight and d == A[i])
            return res
        return dfs(0, 0, True)