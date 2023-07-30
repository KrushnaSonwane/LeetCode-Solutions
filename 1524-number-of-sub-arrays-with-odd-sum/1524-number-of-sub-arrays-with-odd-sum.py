class Solution:
    def numOfSubarrays(self, A: List[int]) -> int:
        MOD = 10**9+7
        @cache
        def dfs(i, isOdd, start):
            if i==len(A): return isOdd
            res = isOdd
            if not start:
                res += dfs(i+1, 0, start)
            res += dfs(i+1, (isOdd+A[i])%2, True)
            return res
        return dfs(0, 0, False) % MOD