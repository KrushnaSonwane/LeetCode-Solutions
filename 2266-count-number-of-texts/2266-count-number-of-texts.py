class Solution:
    def countTexts(self, A: str) -> int:
        hashT = {'1': 1, '2': 3, '3': 3, '4': 3, '5': 3, '6': 3, '7': 4, '8': 3, '9': 4}
        MOD = 10**9+7
        @cache
        def dfs(i, num, count):
            if count > hashT[num]: return 0
            if i == len(A): return 1
            res = dfs(i+1, A[i], 1)
            if A[i] == num:
                res += dfs(i+1, num, count+1)
            return res % MOD
        return dfs(0, '1', 0)